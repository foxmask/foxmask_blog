Title: Django Trigger Happy - déclenche une heureuse rafale de mises à jour
Date: 2014-10-22 10:30
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-declenche-heureuse-rafale-maj
Status: published

Après quelques mois de tests et tergiversations, j'ai fini par me fendre
d'une nouvelle version du projet "Trigger Happy" et de tous ses modules.

Si vous découvrez tout juste le projet, follow ici [de quoi obtenir un
aperçu](h/post/2013/05/27/django-trigger-happy/)
([et en
images](/post/2013/06/04/django-trigger-happy-un-ifttt-like-en-images/))

Voici la listes des nouveautés & améliorations produites.

### A- Mises à jour

A tout seigneur tout honneur donc, on commence par le coeur du projet :

#### django-th : le Core

-   Partie Backend
    1.  suppression des doctest pour des tests unitaires
    2.  mise à jour Django 1.7
    3.  migration des 2 batches `fire.py` et `fire_as.py` en *management
        command* ce qui permet, comme chacun doit savoir, de lancer les
        commandes aisément depuis `manage.py`. La 2nde commande exploite
        `asyncio` et donc peut-être lancée depuis `python 3.4`
    4.  Doc au format `Sphinx` en cas de besoin ;)
    5.  amélioration des perfs en réduisant les requêtes SQL via
        `Queryset.select_related()`
-   Partie Front :
    1.  intégration de `BootStrap` 3 (vs version 2)
    2.  amélioration de l'interface à laquelle est ajoutée de l'Ajax
        (pour les urls est utilisent `django-js-reverse`) permettant
        d'activer ou non un trigger (sans recharger la page évidemment)
-   Packaging :
    1.  ajout d'un fichier `MODULES.rst` permettant de recenser les
        modules existants et dispo sur `pypi`

#### Modules "Trigger Happy"

Ensuite tous les modules "Trigger Happy" ont subit (quasiment) les mêmes
mises à jour :

-   Partie Backend :
    1.  mise à jour Django 1.7
    2.  Doc au format Sphinx en cas de besoin ;)
    3.  suppression des doctest pour des tests unitaires
-   Partie Front :
    1.  intégration de BootStrap 3 (vs version 2)

Celles-ci concernent :

-   **django-th-dummy** : module pour se bootstrap son propre module
    Trigger Happy,
-   **django-th-evernote** : module pour gérer les données de son compte
    Evernote,
-   **django-th-pocket** : module pour gérer les données de son compte
    Pocket,
-   **django-th-rss** : module pour gérer les données de flux RSS,
-   **django-th-readability** : module pour gérer les données de son
    compte Readability

### B - Nouveauté

*nouveau module flambant neuf* pour encore plus de liberté,
**django-th-twitter** :

Avec ce dernier vous pouvez envoyer des données d'un des services ci
dessus sur votre compte Twitter, ou récupérer des infos depuis Twitter
(via un Tag ou le compte d'un Twittos) pour les expédier vers l'un des
services ci dessus.  
Genre une news tombe chez nos amis de [Sam&Max](http://sametmax.com) et
vous voulez la publier cache sur Twitter, ou à l'inverse vous suivez
leur compte Twitter et voulez ne rien rater de leur Tweets pour les
balancer sur votre compte Pocket, ce module est là pour ça.

### C- Ze Stuff

Où trouver toute la clic ?

-   sur le classique Pypi :
    -   [Django Trigger Happy](https://pypi.python.org/pypi/django_th/)
    -   [Evernote](https://pypi.python.org/pypi/django_th_evernote/)
    -   [Pocket](https://pypi.python.org/pypi/django_th_pocket/)
    -   [Readability](https://pypi.python.org/pypi/django_th_readability/)
    -   [RSS](https://pypi.python.org/pypi/django_th_rss/)
    -   [Twitter](https://pypi.python.org/pypi/django_th_twitter/)
-   ou sur les dépôts GitHub :
    -   [Django Trigger Happy](https://github.com/foxmask/django-th)
    -   [Evernote](https://github.com/foxmask/django-th-evernote)
    -   [Pocket](https://github.com/foxmask/django-th-pocket)
    -   [Readability](https://github.com/foxmask/django-th-readability)
    -   [RSS](https://github.com/foxmask/django-th-rss)
    -   [Twitter](https://github.com/foxmask/django-th-twitter)

### A venir

Qu'est-il prévu pour la suite ?  
Un petit tour sur [la liste des
tickets](https://github.com/foxmask/django-th/issues) & milestones vous
en dira plus

### What's about you ?

Si une question vous taraude sur le projet, ou envie de laisser un petit
mot, n'hésitez pas.

