Title: Django Trigger Happy un IFTTT like , en images
Date: 2013-06-04 12:43
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-un-ifttt-like-en-images
Status: published

BonjEllo !

Je ne vous referai par "l'article" [j'ai déjà longuement détaillé ce
petit projet
ici](/post/2013/05/27/django-trigger-happy/ "Django Trigger Happy – une première"),
je vous montre juste ce à quoi il ressemble pour le moment, dans une
version très "toute neuve" ;)

**Les services activés par l'utilisateur :**

[![Liste des services activés par l'utilisateur](/static/2013/06/dth_services-1024x289.png)](/static/2013/06/dth_services.png)

**Wizard de création d'un trigger en 3 petites pages :**

[![Wizard page 1 ; quel flux RSS veux je utiliser
?](/static/2013/06/dth_wizard1-1024x368.png)](/static/2013/06/dth_wizard1.png)


[![dans quel notebook et avec quel tag je veux créer mes notes ?](/static/2013/06/dth_wizard2-1024x365.png)](/static/2013/06/dth_wizard2.png)

[![Une description à mon "trigger"](/static/2013/06/dth_wizard3-1024x363.png)](/static/2013/06/dth_wizard3.png)

**Les des triggers prêts à l'emploi**  
Une fois le wizard utilisé pour définir ce qu'on veut "grabber", on a
notre jolie page d'accueil qui ressemble à ceci :

[![Liste des triggers définis ; actifs ou non](/static/2013/07/dth_triggers-1024x434.png)](/static/2013/07/dth_triggers.png)


**fire !**  
à présent que tout est prêt il nous reste un petit script python qui va
nous faire notre tambouille et qui au lancement vous donne le cours des
opérations :

```shell
./fire.py
INFO PROVIDER ServiceRss CONSUMMER ServiceEvernote : News Sam et Max
INFO PROVIDER ServiceRss CONSUMMER ServiceEvernote : News de Numerama
INFO PROVIDER ServiceRss CONSUMMER ServiceEvernote : Python Package Index
INFO PROVIDER ServiceRss CONSUMMER ServiceEvernote : mes news pourries :)
```

ce script est collé dans une crontab toutes les 10minutes

**Résultat dans Evernote**  
ah oui tout de même last but not least, il est bien beau avec son
script mais zoukilé le résultat de toutes ces pages remplies ? c'est là
ça vient ;)

[![Résultat de l'exécution de django- trigger happy dans son compte evernote](/static/2013/06/dth_evernote-1024x450.png)](/static/2013/06/dth_evernote.png)


Comme on le voit, comme dans le wizard ci dessus, sur la partie droite
de l'écran sous le titre "Nexus 10", on lit bien les noms des notebook
et tags, correctement repris et bien créés à la volée.

Si ce petit bidule vous plait, libre à vous de l'essayer, contribuer,
critiquer. C'est open bar !

Le projet ne risque pas de pourrir dans un coin, j'en suis le premier
client et est moult idées ;)

*ps: si vous l'essayer, utiliser plutot le dépôt github que pypi qui
n'est pas uptodate avec les dernières corrections*

**Edit**: je vous rajoute 2 captures pour illustrer le rendu ...

1\) reçu directement par mail en s'abonnant à la ml de **sam&max**

[![Sam et Max : les news via Email](/static/2013/06/sam_et_max_batbelt_via_email.png)](/static/2013/06/sam_et_max_batbelt_via_email.png)


2\) reçu via DTH

[![Sam et Max : les news via DTH "Django Trigger Happy"](/static/2013/06/sam_et_max_batbelt_via_dth.png)](/static/2013/06/sam_et_max_batbelt_via_dth.png)


