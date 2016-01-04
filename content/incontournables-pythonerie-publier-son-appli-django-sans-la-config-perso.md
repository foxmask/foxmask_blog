Title: Incontournables Pythonerie : publier son appli Django sans la config perso
Date: 2013-06-24 14:15
Author: foxmask
Category: Techno
Tags: python
Slug: incontournables-pythonerie-publier-son-appli-django-sans-la-config-perso
Status: published

Voici donc une nouvel épisode des Incontournable Pythonerie que vous
auriez pu oublier ;)

Imaginons que vous ayez pondu la plus belle lib python jamais vu et que
vous ayez besoin de la publier sur le dépôt
[Pypi](https://pypi.python.org/pypi).

Vous me direz c'est "QQ la praline (coucou christian;) ton histoire on
fait juste python setup.py sdist et byebye"

Alors oui vous avez raison !

A présent imaginons un truc plus élaboré par exemple une application
django.  
Avec django on dispose d'un fichier de configuration nommé comme chacun
sait, settings.py

Souvent, on y colle des trucs propres à notre environnement et au moment
de commiter ce fichier sur github ou autre, on est fort bien
emmerdouiller à retirer de ce fichier, notre config perso.

Du coup, on en vient à une bidouille toute bête permettant de conserver
le settings.py d'origine et d'y importer sa config perso comme ceci :

```python
# local settings management
try:
    from .local_settings import *
except ImportError:
    pass
```

c'est 5 lignes vont en fin de votre settings.py et vous pouvez mettre
tout ce que vous voulez dedans il aura la même fonction que l'original  
Ne vous reste plus ensuite qu'à mettre dans votre fichier .gitignore
local\_settings.py pour ne pas l'expédier dans les sources de votre
projet

Maintenant je suis tout joie, mon appli marche parfaitement et je vais
de ce pas la publier sur pypi pour faire partager ma liesse :

je tape

```python
python setup.py register
```

réponds aux questions demandées et enchaine avec

```python
python setup.py sdist
```

pour créer une archive  
suivi de

```python
python setup.py sdist upload
```

pour envoyer ladite archive sur pypi.

le résultat de sdist donne ceci :

```shell
$ python setup.py sdist 

running sdist
running egg_info
creating django_th.egg-info
writing requirements to django_th.egg-info/requires.txt
writing django_th.egg-info/PKG-INFO
writing top-level names to django_th.egg-info/top_level.txt
writing dependency_links to django_th.egg-info/dependency_links.txt
writing manifest file 'django_th.egg-info/SOURCES.txt'
reading manifest file 'django_th.egg-info/SOURCES.txt'
writing manifest file 'django_th.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.txt

...

creating django_th-0.3.0
creating django_th-0.3.0/django_th
creating django_th-0.3.0/django_th.egg-info
...
creating django_th-0.3.0/django_th/models
creating django_th-0.3.0/django_th/services
creating django_th-0.3.0/django_th/templatetags
making hard links in django_th-0.3.0...
hard linking setup.py -> django_th-0.3.0
hard linking django_th/__init__.py -> django_th-0.3.0/django_th
hard linking django_th/admin.py -> django_th-0.3.0/django_th
hard linking django_th/context_processors.py -> django_th-0.3.0/django_th
hard linking django_th/service_provider.py -> django_th-0.3.0/django_th
hard linking django_th/local_settings.py -> django_th-0.3.0/django_th
hard linking django_th/settings.py -> django_th-0.3.0/django_th
hard linking django_th/urls.py -> django_th-0.3.0/django_th
hard linking django_th/views.py -> django_th-0.3.0/django_th
hard linking django_th/wsgi.py -> django_th-0.3.0/django_th
```

si vous avez prêté attention aux logs vous voyez un truc que je ne
voulais pas mettre dans mon archive

```shell
hard linking django_th/local_settings.py -> django_th-0.3.0/django_th
```

là c'est la cata ... ma config part sur pypi avec potentiellement des
clés de services tiers... vous voyez le basard :P

Donc en retournant à la doc [de
distutils](http://docs.python.org/3/distutils/sourcedist.html), on voit
qu'on dispose d'une option permettant d'exclure du packaging une partie
de son projet.

On créé un fichier MANIFEST.in contenant :

```python
include *.txt
recursive-include examples *.txt *.py
prune examples/sample?/build
```

ici on n'a aucun cas d'exclusion explicite, elles sont plutôt
implicites, puisqu'on dit ce qu'on veut mais pas ce qu'on ne veut pas.

Dans mon cas je ne souhaite pas mettre local\_settings.py c'est tout.
Donc dans le MANIFEST.in on mettra

```python
exclude django_th/local_settings.py
```

Je supprime le dossier "dist" créé via la commande python setup.py sdist
précédente et relance pour obtenir :

```shell
$ python setup.py sdist 

running sdist
running egg_info
creating django_th.egg-info
writing requirements to django_th.egg-info/requires.txt
writing django_th.egg-info/PKG-INFO
writing top-level names to django_th.egg-info/top_level.txt
writing dependency_links to django_th.egg-info/dependency_links.txt
writing manifest file 'django_th.egg-info/SOURCES.txt'
reading manifest file 'django_th.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'django_th.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.txt

...

creating django_th-0.3.0
creating django_th-0.3.0/django_th
creating django_th-0.3.0/django_th.egg-info
creating django_th-0.3.0/django_th/forms
creating django_th-0.3.0/django_th/lib
creating django_th-0.3.0/django_th/lib/conditionchecker
creating django_th-0.3.0/django_th/lib/feedsservice
creating django_th-0.3.0/django_th/migrations
creating django_th-0.3.0/django_th/models
creating django_th-0.3.0/django_th/services
creating django_th-0.3.0/django_th/templatetags
making hard links in django_th-0.3.0...
hard linking MANIFEST.in -> django_th-0.3.0
hard linking setup.py -> django_th-0.3.0
hard linking django_th/__init__.py -> django_th-0.3.0/django_th
hard linking django_th/admin.py -> django_th-0.3.0/django_th
hard linking django_th/context_processors.py -> django_th-0.3.0/django_th
hard linking django_th/service_provider.py -> django_th-0.3.0/django_th
hard linking django_th/settings.py -> django_th-0.3.0/django_th
hard linking django_th/urls.py -> django_th-0.3.0/django_th
hard linking django_th/views.py -> django_th-0.3.0/django_th
hard linking django_th/wsgi.py -> django_th-0.3.0/django_th
```

cette fois ci le fichier MANIFEST.in est pris en compte et on ne trouve
plus le fichier de config perso.

on pourra s'envoyer de nouveau un coup de

```python
python setup.py sdist upload
```

pour envoyer les sources sur pypi.

Si vous êtes arrivé au bout de ce billet bravo ;) pour la peine un
cadeau "bonusque" (comme disait Coluche) :

Je me suis pris la tête une bonne heure avec

```python
python setup.py build
```

qui n'excluait pas le local\_settings.py avec le fichier MANIFEST.in

alors qu'en fait c'est sdist qui le gérait ...

