Title: Quand Les "job queue" et les amis "brokers de messages" sont mis au rancart par la stdlib
Date: 2016-04-14 10:00
Author: foxmask
Category: Techno
Tags: TriggerHappy, multiprocessing, activemq, celery, rq
Slug: job-queue-and-messages-broker-out
Status: published


# Intro

Ce post n'est autre qu'un simple retour d'XP sur l'utilisation et tests de diverses solutions (almost)ready-to-use de job queue et brokers de messages.


# Présentation de l'archi du projet

Comme vous pouvez l'imaginer avec IFTTT si vous connaissez ce service, j'ai des triggers qui permettent de récupérer des données pour être publiées n'importe où. 

# Des mécaniques, il ne faut pas rouler

Pour que cela ne soit pas fait par des traitements en série **et** bloquant, j'exploite le cache de Django à coup de `cache.set()` et `cache.get()` avec 2 tâches récurrentes, une qui récupère les données et fait donc le `cache.set()` et une qui publie les données à partir des éléments récupérés par `cache.get()`


# Les "solutions" utilisées pour le traitement des tâches

Depuis quelques semaines pour Trigger Happy, j'ai migré de "Job Queue", passant de [`Celery`](http://docs.celeryproject.org/) à [`Python-rq`](http://python-rq.org).
Celery cessant de fonctionner sans raison apparente (aucune info dans les logs ni dans la console), de guerrelasse, je suis passé à `RQ`, plus léger et facile à manipuler.

Mais il y a 10jours j'en ai eu marre de voir RQ prendre des fins de non recevoir du serveur redis à coup de "connections timeout" pour des choses "futiles" (par exemple une pauvre tâche changeant version=2 à version=1 de 3 ou 4 données seulement).

Donc je suis parti creuser côté RQ ce qui pouvait poser problème, et, au hasard d'un ticket, je découvre qu'en fait... RQ ne gère qu'**un worker à la fois** et pas toute une batterie comme avec celery. Ce ticket datant de 2012 (ouais 4ans hein) d'autres se sont lancés dans des projets parallèles ([https://github.com/Koed00/django-q](https://github.com/Koed00/django-q) ,  [https://github.com/pricingassistant/mrq](https://github.com/pricingassistant/mrq)) pour remédier au problème. 

Je ne me suis pas amusé à tous les tester sinon j'y serai encore. Et surtout pour me faire installer mongodb en plus (le cas du projet mrq), j'ai trouvé ça trop lourd pour moi et ceux qui s'installeraient mon projet pour eux.

Je suis donc parti dans un (bad)road trip "broker / job queue" pour tenter de trouver mon bonheur.

# Road Trip Broker / Job Queue

Ce n'est pas la route 66 mais vous allez voir que ya matière...

## 1iere escale : [activeMQ](http://activemq.apache.org/)

Pourquoi celui là ?

Parce-que la lib python gérant ce dernier, nommée `stomp.py`, était limpide à mes yeux, (et si je parvenais à faire fonctionner la machinerie, ca permettrait que le code soit utilisable également pour [`RabbitMQ`](https://www.rabbitmq.com/) et [`Appolo`](http://activemq.apache.org/apollo/)), mais après avoir fini mon code et testé avec succès, comme pour `mongodb`, faire installer `activeMQ` et son giga de RAM à consommer, je ne me voyais pas mettre ce prérequis à installer pour le projet pour vous autres.


## 2ieme escale : beanstalk

Pourquoi celui là ? 

Parce-que rapide, m'a-t-on rapporté, et faisant exactement ce pour quoi il a été écrit.

Comme mon projet est en python 3, la batterie de libs existantes ne convenait pas. Je me suis orienté sur [https://github.com/jonasvp/django-beanstalkd](https://github.com/jonasvp/django-beanstalkd), que j'ai forké pour switcher de beanstalkc à pystalkd, histoire de faire ma sorcellerie dans mon coin sans gêner personne ;)

Manque de bol chez moi après avoir arrangé le code, même si la rapidité était au rendez-vous, au premier lancement : `JOB_TOO_BIG`

Alors peut-être que ça venait de la lib cliente `pystalkd` (en python 3 je rappelle), mais je n'ai plus eu l'envie de creuser celle-ci.

Du coup, après tout ça, il ne me restait plus rien comme solution existante, que je maîtrisais/connaissais ... Donc

## 3ieme escale : la stdlib !

Il y a quelques mois [j'évoquais sur s&m le multiprocessing](http://sametmax.com/python-ubiuite-multiprocessing/).

Donc c'est tout ce qu'il me restait, "quand faut y aller faut y aller" me dis-je.

Et au final ça n'a pas mal réussi puisque les temps de traitement sont passés de un peu moins d'une minute les 40 triggers à... 7sec (en moyenne haute ;)

Tout cela grâce à 9 lignes de code :)

```python
    trigger = TriggerService.objects.filter(status=True, user__is_active=True).select_related('consumer__name', 'provider__name')

    from multiprocessing import Pool, TimeoutError
    try:
        with Pool(processes=settings.DJANGO_TH['processes']) as pool:
            result = pool.map_async(publishing, trigger)
            result.get(timeout=360)
    except TimeoutError as e:
        logger.warn(e)
```
chez moi `settings.DJANGO_TH['processes']` vaut 5. Je vous fais grâce de la fonction `publishing` ;)


### Publication des données :

j'ai voulu charger la mule (toute proportion gardée:) en rajoutant 21 triggers de plus (entre autre traquer #django sur twitter), hé bien je suis passé à 12 secondes pour publier les données de 61 consumers (quand ceux ci ont des données à fournir évidemment) (donc ca fait un coup de 305triggers/min)

quand rien n'est à faire, la liste est passée au crible en 1/10° de seconde... c'est plutôt ... correct :D


### Récupération des données : 

10secondes pour les 61 triggers (ca fait un coup de 360triggers/min)


### Tentative d'amélioration des perfs

Pour éviter des accès à la base de données à tout prix, j'ai tenté de n'exploiter que le cache. 
Du coup j'ai dû m'orienter vers `apply_async` vs `map_async`, mais les temps de traitements étaient pire que si je n'avais pas utilisé `multiprocessing.Pool.apply_async()`. Ensuite j'ai rajouté plus d'info dans le cache pour arriver à ne passer que par `map_async()` mais encore une fois le résultat n'était pas terrible.

Du coup j'en suis resté à mes 9 lignes de code ci dessus.

## Nota

Ici je n'ai pas cherché à dézinguer un projet plus qu'un autre, chacun fonctionnant dans un univers, au final, très différent du mien, j'ai juste voulu souligner, qu'à aller chercher des solutions toutes faites, ce n'était pas forcément le plus bénéfique, si on prenait le temps de se pencher sur ce qu'offrait déjà le langage.

Par ailleurs, un truc qui ne transparait pas ici, c'est le temps que tout cela m'a pris pour tester et appréhender chaque solution de job queue / messages broker, de même que se pencher sur `apply_async` et `map_async`. 

Ceci explique pourquoi, à un moment donné, je n'approfondis plus mes investigations dans la recherche de bug dans pystakld par exemple sur le `JOB_TOO_BIG` pour continuer sur la voie `beanstalkd`.


## Last but not... toussa

En l'état, si on veut un rafraichissement des données assez correct (toutes les 15minutes) alors le serveur est capable de gérer un petit contingent de ~3600triggers repartis sur 60 utilisateurs chacun ayant 60 triggers, lesquels seront engloutis en 10min. 

### Ni trop 

De plus il ne faut pas non plus "publier" trop souvent, les accès aux API des services tiers comme Twitter, finiraient par vous envoyer aux pelotes avec un truc genre `User Limit Reached`. 

### Ni trop peu

A l'inverse il ne faut pas non plus publier trop "rarement" car là vous amassez une quantité de données importante dans le cache, que vous ne pourrez pas publier correctement, avec le même genre d'erreur que précédemment.

### Dernière analyse 

Sur les 60triggers que j'ai défini, il y en a entre 3 et 11 qui sont utilisés de façon recurrente, par exemple ceux qui suivent des hashtags sur twitter ou suivent simplement un @compte_twitter, ou les gros sites de news. 

Du coup ca fait pas bézef sur les 60, mais 1) ca me suffit 2) ca marche parfaitement pour mon besoin.

Voici tout de même quelques logs à se mettre sous la dent pour voir ce que donne les temps de réponses.

* toutes les 15min, la publication a lieu
* toutes les 13min, la récupération des données a lieu

ne sont pas affichées, les logs qui n'ont pas de données à traiter, mais qui évidement, consomme du temps. Ce qui explique que de 14:00:00 à 14:00:06 il ne s'affiche rien.

```shell
2016-04-13 13:26:02,928 INFO tasks 3902 foxmask - ServiceRss - ServicePocket - Frandroid - pocket - 1 new data
2016-04-13 13:26:06,156 INFO tasks 3903 foxmask - ServiceRss - ServiceEvernote - LinuxFr - 1 new data
2016-04-13 13:26:06,802 INFO tasks 3902 foxmask - ServiceTwitter - ServicePocket - Django - 2 new data
2016-04-13 13:26:07,137 INFO tasks 3906 foxmask - ServiceTwitter - ServiceTrello - Django - 2 new data
2016-04-13 13:26:08,504 INFO tasks 3903 foxmask - ServiceTwitter - ServiceReadability - Django - 2 new data
2016-04-13 13:30:03,616 INFO tasks 3946 foxmask - ServiceRss - ServicePocket - Frandroid - pocket - 1 new data
2016-04-13 13:30:04,152 INFO tasks 3949 foxmask - ServiceTwitter - ServicePocket - Django - 2 new data
2016-04-13 13:30:04,931 INFO tasks 3947 foxmask - ServiceTwitter - ServiceReadability - Django - 2 new data
2016-04-13 13:30:07,977 INFO tasks 3948 foxmask - ServiceRss - ServiceEvernote - LinuxFr - 1 new data
2016-04-13 13:30:09,572 INFO tasks 3950 foxmask - ServiceTwitter - ServiceTrello - Django - 2 new data
2016-04-13 13:39:05,783 INFO tasks 4348 foxmask - ServiceRss - ServicePocket - TheVerge - 1 new data
2016-04-13 13:42:02,482 INFO tasks 4383 recycle of cache done!
2016-04-13 13:52:03,933 INFO tasks 4462 foxmask - ServiceRss - ServicePocket - TheVerge - 1 new data
2016-04-13 13:52:06,910 INFO tasks 4462 foxmask - ServiceTwitter - ServiceTrello - Django - 2 new data
2016-04-13 13:52:07,632 INFO tasks 4461 foxmask - ServiceRss - ServiceReadability - Numerama - 1 new data
2016-04-13 13:52:07,993 INFO tasks 4463 foxmask - ServiceTwitter - ServicePocket - Django - 2 new data
2016-04-13 13:52:09,537 INFO tasks 4463 foxmask - ServiceTwitter - ServiceReadability - Django - 2 new data
2016-04-13 14:00:06,192 INFO tasks 4524 recycle of cache done!
2016-04-13 14:00:06,309 INFO tasks 4539 foxmask - ServiceRss - ServicePocket - TheVerge - 1 new data
2016-04-13 14:00:06,788 INFO tasks 4540 foxmask - ServiceTwitter - ServicePocket - Django - 2 new data
2016-04-13 14:00:07,321 INFO tasks 4536 foxmask - ServiceRss - ServicePocket - TheVerge - 1 new data
2016-04-13 14:00:07,497 INFO tasks 4538 foxmask - ServiceRss - ServiceReadability - Numerama - 1 new data
2016-04-13 14:00:07,751 INFO tasks 4535 foxmask - ServiceTwitter - ServiceReadability - Django - 2 new data
2016-04-13 14:00:10,278 INFO tasks 4536 foxmask - ServiceTwitter - ServiceTrello - Django - 5 new data
2016-04-13 14:00:10,875 INFO tasks 4542 foxmask - ServiceRss - ServiceEvernote - Korben - 1 new data
2016-04-13 14:00:11,279 INFO tasks 4536 foxmask - ServiceRss - ServiceEvernote - BeGeek - 1 new data
2016-04-13 14:00:11,461 INFO tasks 4536 foxmask - ServiceRss - ServiceEvernote - Google high-tech - 2 new data
2016-04-13 14:00:11,717 INFO tasks 4543 foxmask - ServiceTwitter - ServiceTrello - Django - 2 new data
2016-04-13 14:00:11,793 INFO tasks 4542 foxmask - ServiceTwitter - ServicePocket - Django - 5 new data
2016-04-13 14:00:12,634 INFO tasks 4536 foxmask - ServiceTwitter - ServiceReadability - Django - 5 new data
2016-04-13 14:00:14,414 INFO tasks 4537 foxmask - ServiceRss - ServiceReadability - Korden - 1 new data
2016-04-13 14:00:15,533 INFO tasks 4534 foxmask - ServiceRss - ServiceReadability - Numerama - 1 new data
2016-04-13 14:00:16,498 INFO tasks 4543 foxmask - ServiceRss - ServiceEvernote - BeGeek - 1 new data
2016-04-13 14:00:17,206 INFO tasks 4542 foxmask - ServiceRss - ServiceReadability - BeGeek - 1 new data
```

## Conclusion

Cette fois ci l'éternel insatisfait que je suis, se sent un peu mieux avec cette solution (... quoi que ya encore un truc à gratter pour que ca soit 'encore mieux';)
