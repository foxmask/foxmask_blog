Title: Trigger-Happy.eu s'ouvr.eu
Date: 2013-08-13 11:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: trigger-happy-eu-souvr-eu
Status: published

Hello,  
A ceux qui suivent mes dernières expériences pythono-djanguesques vous
ne serez pas étonnés d'apprendre ce qui suit, aux nouveaux venus,
welcome et bonne lecture ;).

Présentation
------------

Ainsi je me suis lancé dans un projet nommé [Django Trigger
Happy](http://trigger-happy.eu "Service de gestion de déclencheurs / propagateurs d'informations")
permettant depuis une source de données depuis l'autre coté de la toile,
d'alimenter un autre service tel Evernote, Facebook, Twitter,
Readability, Pocket, Feedly et j'en passe et des meilleurs.

Pour le moment le projet ne sait faire que 2 choses :

-   lire des flux RSS/ATOM
-   depuis ces derniers, écrire des notes dans Evernote, et en fonction
    de chacun des flux on peut décider de dispatcher dans un carnet
    plutôt qu'un autre.

Pourquoi Comment ?
------------------

Tout comme il existe des logiciels pour héberger son blog, ou d'autres
pour produire son site web avec Drupal, Magento, ou encore d'autre pour
des forums, ... Django Trigger Happy se veut être une solution
personnelle de gestion de services depuis des sources éparses comme
citées plus haut.

je ne détaillerai pas plus pour en avoir longuement parlé [en
long](/post/2013/06/04/django-trigger-happy-un-ifttt-like-en-images/ "Django Trigger Happy un IFTTT like , en images")
[en
large](/post/2013/06/21/djngo-trigger-happy-0-3/ "Django Trigger Happy 0.3")
[et en travers dans ces
billets](/post/2013/05/27/django-trigger-happy/ "Django Trigger Happy – une première")
;)

Le but principal de ce billet est juste de vous annoncer que j'ai ouvert
[Trigger-Happy.eu](http://trigger-happy.eu/) afin que vous puissiez
l'essayer si vous disposez d'un jeu de flux RSS et bien sûr surtout,
d'un compte Evernote.

Ainsi si c'est le cas, après vous êtes enregistré sur
[Trigger-Happy.eu](http://trigger-happy.eu/), activez les 2 services ...

Création d'un trigger
---------------------

[![Liste des services activés par l'utilisateur](/static/2013/06/dth_services-1024x289.png)](/static/2013/06/dth_services.png)


... pour les utiliser avec le wizard que vous trouverez à cet effet,
vous demandant le nom et l'url du flux RSS/ATOM "source" et le carnet
evernote "cible" où stocker les infos comme suit :

[![Wizard page 1 ; quel flux RSS veux je utiliser ?](/static/2013/06/dth_wizard1-1024x368.png)](/static/2013/06/dth_wizard1.png)

[![dans quel notebook et avec quel tag veux je créer mes notes ?](/static/2013/06/dth_wizard2-1024x365.png)](/static/2013/06/dth_wizard2.png)


ce qui vous donnera quelque chose comme ceci :

[![Liste des triggers définis ; actifs ou non](/static/2013/07/dth_triggers-1024x434.png)](/static/2013/07/dth_triggers.png)


Une fois tout ceci effectué, toutes les 10 minutes, tous les flux
RSS/ATOM seront passés en revu et une note sera créée dans les carnets
que vous aurez décidé le cas échéant.

Le mot de la fin
----------------

Pour finir, **la roadmap** concernant les prochains services qui seront
intégrés [seront
ceux-ci](/post/2013/07/13/sondage-quels-services-utilisez-vous-le-plus/ "Sondage : quels services utilisez vous le plus ?")
après que la vox populi se soit exprimée (et je l'en remercie ;)

Si vos tests sont concluant, n'hésitez pas à vous installer votre propre
"Trigger Happy" sur votre serveur/hébergement [en suivant cette
procédure](https://github.com/foxmask/django-th/blob/master/README.rst "Installation de Django Trigger Happy").  
Si vous ne pouvez pas installer "Trigger Happy" sur un serveur
personnel, libre à vous d'utiliser le site
[Trigger-Happy.eu](http://trigger-happy.eu/) pour vos propres besoins,
mais sachez qu'aucune (vile) exploitation de vos données personnelles
avec ce projet ne sera faite, tant mercantile que statistiques :P

English version
---------------

**here is a short version of the announcement**  
Today we can host our own blog website with dedicated software like
Wordpress, or build our own website with soft like Magento, Drupal. Now
Django Trigger Happy, an opensource project, offers the possibility to
host your own service to manage all datas from all around the web.  
Today, Django Trigger Happy can do only 2 things :

-   read RSS/ATOM Feeds
-   and from this data, create notes in Evernote

So i opened [Trigger-Happy.eu](http://trigger-happy.eu/), to let you try
to play with your sets of RSS/ATOM. You just need to register and then
once it's done, go to the services pages and activate each of them. Once
it's done you are able to create a trigger and fill the expected
informations. Then once everything is ready, each 10 minutes, the
RSS/ATOM Feeds will be read and notes Evernote will be create at the
right moment at the right place.

notice : none of the data you will provide will be used for mercantile
purpose nor statistics.

