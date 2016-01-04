Title: Django - think twice - another day for you and me in paradise
Date: 2013-04-11 15:00
Author: foxmask
Category: Techno
Tags: Django
Slug: django-think-twice-another-day-for-you-and-me-in-paradise
Status: published

**thought one**

**Intro** :

Parfois ça crêve les yeux mais quand on n'est pas réveillé ; on a
justement les yeux crevés :)

**Voilà ce qui m'aveuglait** :

En tapant un

```shell
python manage.py syncdb
```

J'obtenais :

```python
django.core.exceptions.ImproperlyConfigured: '/home/foxmask/Django-Virtualenv/django-trigger-happy/django_th/django_th/sqlite3' isn't an available database backend.
Try using django.db.backends.XXX, where XXX is one of:
    'dummy', 'mysql', 'oracle', 'postgresql_psycopg2', 'sqlite3'
Error was: Import by filename is not supported.
```

Evident non ?

bon, mon settings.py contenait :

```python
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': '',
        'NAME': '',
        # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}
```

j'ai juste rajouté 'ENGINE':'sqlite3' et patatra alors que le message
complet et explicite me dit "using django.db.backends.XXX where XXX is
one of ..." c'etait tellement evident ;)

**Pourquoi comment ?**

dans mon process de dev j'utilise un settings.py que je ne modifie pas
du tout pour la config DATABASES qui est elle dans un local\_settings.py
chargée à la fin de settings.py. Du coup en committant mon settings.py
j'ai viré tout simplement **"django.db.backend."** de **'ENGINE':** de
ce dernier puisque présent dans local\_settings.

**Comment se faire des noeuds au cerveau ?**

Aahhhhhhhhhhhh je vous jure ;)

**thought two**  
A coté de ce sujet qui a bien fait marrer \#django-fr @ freenode ;)),
un moins "QQ La praline" : splitter models.py en petit bout en fonction
d'un périmètre fonctionnel

Pour arriver à séparer les classes de son models.py on doit créer un
dossier models contenant :

```python
myapp/
    models/
        __init__.py
        truc.py
        muche.py
```

et dans \_\_init\_\_.py mettre simplement :

```python
from truc import Machin
from muche import Chose
```

où Machin et Chose sont des classes dans truc.py et muche.py

Seulement tout ceci ne suffit pas... quand on va lancer python manage.py
syncdb, aucune des 2 tables ne sera créée.

La solution, subtilité est cachée par là :

```python
class Machin(models.Model):
    class Meta:
        app_label = 'myapp'
```

si app\_label n'est pas défini django ne saura pas que la classe splitée
appartient à cette application ([si j'ai tout bien suivi les
explications
ici](http://www.nomadjourney.com/2009/11/splitting-up-django-models/))

