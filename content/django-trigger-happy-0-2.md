Title: Django Trigger Happy 0.2
Date: 2013-06-17 10:53
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-2
Status: published

Hop une nouvelle version !

[![Django Trigger Happy : La page d'accueil](/static/2013/06/django_th_home.png)](/static/2013/06/django_th_home.png)

Celle ci se voit agrémenter de :

-   Nouveautés :
    1.  Dans une note Evernote, ajout dans l'url de la note, du lien du
        flux, ceci permet d'utiliser la fonction "aller à la source"
    2.  Ajout d'un "statut" à son trigger permettant de l'activer ou non
        sans pour autant avoir à le supprimer si on n'en veut plus,
        temporairement
    3.  Ajout d'une pagination sur la liste des triggers


    [![Django Trigger Happy : ajout d'une pagination et gestion de l'activation/désactivation des triggers](/static/2013/06/django_th_020_triggers_list-1024x567.png)](/static/2013/06/django_th_020_triggers_list.png)

-   Améliorations:
    1.  Dans le pied de page de la note, remplacement du lien par
        l'affichage de l'origine de la source des données + le lien vers
        celle-ci

    [![Django Trigger Happy : 2 améliorations dans la note
    evernote](/static/2013/06/django_th_020_evernote.png)](/static/2013/06/django_th_020_evernote.png)

-   Corrections de bugs:
    1.  L'imposition d'un tag, pour la création des notes, n'est plus :)
    2.  Le traitement des flux Atom faisait planter le traitement batch
    3.  Edition d'un trigger rendu possible à présent

    [![Django Trigger Happy : modification d'un
    trigger](/static/2013/06/django_th_020_edit_trigger.png)](/static/2013/06/django_th_020_edit_trigger.png)


**Edit**  
si vous vouliez l'installer via

```python
pip install django_th
```

oubliez !  
pour cette version ca ne fonctionne pas ; balot que je suis je n'ai pas
mis le setup.py là où pypi l'attendait.  
Donc en attendant 2 solutions, l'archive est dispo

-   [depuis Pypi](https://pypi.python.org/pypi/django_th/0.2.0)
-   [depuis GitHub (le lien zip
    :)](https://github.com/foxmask/django-th/tree/trigger-happy-0.2.0)

