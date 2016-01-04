Title: Django Trigger Happy 0.10.x et ses amis
Date: 2015-04-21 10:30
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-10-x-et-ses-amis
Status: published

Le projet Triger Happy sort en version 0.10.1 avec au programme :

**Nouveautés :**

-   Moteur de recherche basé sur haystack (quand on a plus de 30
    triggers ca commence à en faire ;)
-   Un mode *vacances*, permettant de mettre en pause tous les triggers
    jusqu'à votre retour de congés, histoire de vivre vraiment
    *déconnecté* ses vacances ;)

**Améliorations :**

-   support de Django 1.8
-   support python 3
-   support des caractères accentués mal affichés avec un
    *html\_entities php like*
-   contribution de [Adrihein](https://github.com/Adrihein) sur le
    layout de l'application

**Ses amis à jour aussi :**

-   module Twitter : /!\\ ici une colonne change de type : bigint vs int
-   module Evernote : ras
-   module Pocket : ras
-   module RSS : ras
-   module Readability : ras
-   module Dummy : ras

**La suite :**  
je n'ai pas été hyper productif sur cette version parce que dans le
même temps, je me suis longuement attardé sur
[Crossbar.io](http://crossbar.io/) / [WAMP.WS](http://wamp.ws) /
[Autobahn](http://autobahn.ws/python/) pour faire un bac à sable
[wamp-th](https://github.com/foxmask/wamp-th).

Ce dernier marche parfaitement ! Encore des détails mais apres ca
devrait etre au point.  
In fine ca devrait remplacer les "managment commands" qui sont
actuellement mises dans une crontab.

Ca devrait permettre d'encore booster Trigger Happy et rendre toutes les
interactions fun ;)

Amusez vous bien !

[Où trouver le projet](http://trigger-happy.eu/)  
[Où trouver les sources](https://github.com/foxmask/django-th/)  
[Où trouver la doc](https://trigger-happy.readthedocs.org/)

