Title: Django Aptana gestion du PYTHONPATH avec un VirtualEnv
Date: 2013-09-26 22:33
Author: foxmask
Category: Techno
Tags: Aptana, Django, python
Slug: django-aptana-pythonpath-virtualenv
Status: published

Avec l'éditeur Aptana, [comme dit dans un précédant
billet](/post/2012/08/25/django-runserver-depuis-aptana/),
on peut faire joujou avec le manager.py de django.

Ici, je vais montrer comment gérer le PYTHONPATH d'un projet Django
qu'on a mis dans un virtualenv de surcroit.

Le but de ce PYTHONPATH avec Aptana va être de nous affranchir d'avoir
en rouge tous les imports django comme par exemple :

```python
from django import forms
```

et dans le même temps cela permettra d'avoir une *completion* du code
des classes les doigts dans le nez.

Pour arriver au but on fera un click droit sur le nom du projet dans la
*perspective* PyDev puis "Propriétés" ce qui nous donnera cette image :  
[![Django Aptana gestion du PYTHONPATH avec
VirtualEnv](/static/2013/09/aptana_django_pythonpath_virtualenv.png)](/static/2013/09/aptana_django_pythonpath_virtualenv.png)

on va procéder ici en 2 étapes :

-   "Pydev - interpreter/grammar"
-   "PyDev - PYTHONPATH"

Etape 1 :

On sélectionne la ligne de gauche "Pydev - interpreter/grammar"  
Puis on sélectionne le lien "click to configure an interpreter not
listed"  
Ici vous allez aller chercher "python" dans le dossier "bin" de votre
virtualenv en cliquant sur "new"  
Une fois fait on clique sur "apply" (en bas à droite de la popup) et
Aptana nous charge tout le contenu de "lib". Avec cette étape les
"import django.xxx" ne seront plus rouge ;)

Etape 2 :

On sélectionne la ligne de gauche "PyDev - PYTHONPATH"  
Sur l'onglet "Sources folder" on doit déjà trouver le path vers django
dans la liste, suite à la manipulation précédante  
On va à présent ajouter ici le path vers le dossier de son application
Django. Pour le localiser, ce dernier est au même niveau que le folder
"bin" de votre virtualenv.

Voilà :)  
Pour en voir les effets, un petit click droit sur projet puis "PyDev"
\> "Code analasis"

