Title: Des news ? Mais Allo !
Date: 2022-01-02 18:00:00
Author: foxmask
Category: Techno
Tags: python
Slug: des-news-mais-alloo
Status: published


# Des news ? Mais Alloo ! 



Quelques nouvelles de 2 applications maison 



## Nyuseu

l'une pour lire des news de ses sites préférés, soit comme une app classique telles que innoreader, feedly et compagnie ou comme le regrêté feû "multiboard" de sam&max.



C'est realisé avec [Django](https://www.djangoproject.com/) (3 puis) 4 et supporte python 3.8 à 3.10



L'application est simple comme bonjour, on ajoute ses flux coté admin et coté publique on accède aux news au fur et à mesure que le moteur, lancé via une crontab, récupère les données des flux RSS.



La dernière nouveauté qui m'a plu de developper dans ce projet c'est la possibilité de s'affranchir de flux "tronqué". Kézako un flux tronqué ?



Exemple : je recupere les flux de numerama mais, comme avec beaucoup de sites avec enormement de contenu lié à de la pub, on ne recoit dans son flux que 2 à 3 phrases suivi du fameux "lire la suite" vous conviant à venir sur le site... pour manger la pub... 

Mais il y a peu, j'ai découvert dans une appli android, [Feeder](https://gitlab.com/spacecowboy/Feeder), pour la nommer, la possibilité de récupérer l'intégralité de son article (tronqué à la base) à la demande.

Or pour pallier à ma frustration, j'ai fouillé la python sphere et suis tombé sur un lib python excellentissime, capable de lire des articles à partir de l'url que vous lui fournissez, celle-ci se nomme [Newspaper](https://github.com/codelucas/newspaper).

A présent, un petit click sur le picto "reload" et voila l'article entier qui s'affichera pour le lire tranquillement ;)



![Nyuseu main page](https://framagit.org/annyong/nyuseu/-/raw/master/nyuseu/doc/screenshot.png)

[Projet Nyuseu](https://framagit.org/annyong/nyuseu/)

## Yeoboseyo 

l'autre application, toujours dans la "mouvance" des applications invisibles, s'exécutant en arrière plan et travaillant pour vous (comme ce que j'avais realisé avec "[TriggerHappy](https://github.com/foxmask/django-th/)"), vous permet donc d'automatiser la propagation de données vers tous les services suivant en même temps :

* Mastodon

* Mattermost

* Slack

* Discord

* Telegram

* Wallabag

* Fichiers locaux en markdown

* ou tout autre service pouvant etre contacté avec un webhook



Ce appli, minuscule est faite avec VueJS pour le front et [Starlette](https://starlette.io) pour le back et supporte python de 3.8 à 3.10.

![Yeoboseyo main page](https://framagit.org/annyong/yeoboseyo/-/raw/master/doc/Yeoboseyo_list.png)

[Projet Yeoboseyo](https://framagit.org/annyong/yeoboseyo/)

## Et Aussi

Bien évidemment, s'il vous prennait l'envi d'ajouter des fonctionnalités pour couvrir un besoin, let me know avec une demande sur les pages des projets respectifs;)


Bonne année 2022 !
