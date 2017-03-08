Title: Incontournables Pythonerie : le fichier requirements.txt
Date: 2013-07-01 11:00
Author: foxmask
Category: Techno
Tags: python, pythonerie
Slug: incontournables-pythonerie-le-fichier-requirements-txt
Status: published

pour faire écho au billet de [Sam et Max sur
requirements.txt](sametmax.com/votre-python-aime-les-pip), voici un tout
petit billet encore sur distutils :)

Mon application dépend de plein d'autres, c'est pour cette raison qu'on
a produit requirements.txt. Mais il n'est pas juste là pour faire joli,
ou dire "les mecs faites pip install -r de mon fichier"...

Il faut bien l'exploiter d'une manière ou d'une autre pour que le moment
venu, notamment lors de l'installation de son application via pip
install <appli>, que ces prérequis soient installés automatiquement tant
qu'à faire.

Pour cela on va retourcher le setup.py comme ceci (snipset recupéré d'un
des setup.py du sieur David Larlet:) :

```python
import os

def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

setup (
    ...
    install_requires=install_requires,
)
```

ce qui aura pour effet que lors de l'installation, le fichier
requirements.txt soit lu puis que chaque ligne de ce fichier soit
appelée pour être installée.

Ensuite quand vous testez (j'espere) que votre packaging fonctionne via
un pip install <appli>, si vous rencontrez ce problème :

```python
Downloading/unpacking django-th
  Running setup.py egg_info for package django-th
    Traceback (most recent call last):
      File "", line 14, in 
      File "/home/foxmask/Django-VirtualEnv/foobar/build/django-th/setup.py", line 12, in 
        install_requires = reqs('requirements.txt')
      File "/home/foxmask/Django-VirtualEnv/foobar/build/django-th/setup.py", line 10, in reqs
        os.path.join(os.getcwd(), *f)).readlines()]))
    IOError: [Errno 2] No such file or directory: '/home/foxmask/Django-VirtualEnv/foobar/build/django-th/requirements.txt'
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):

  File "", line 14, in 

  File "/home/foxmask/Django-VirtualEnv/foobar/build/django-th/setup.py", line 12, in 

    install_requires = reqs('requirements.txt')

  File "/home/foxmask/Django-VirtualEnv/foobar/build/django-th/setup.py", line 10, in reqs

    os.path.join(os.getcwd(), *f)).readlines()]))

IOError: [Errno 2] No such file or directory: '/home/foxmask/Django-VirtualEnv/foobar/build/django-th/requirements.txt'
```

c'est que votre package ne contient pas ledit requirements.txt

Si vous utilisez un MANIFEST.in il faut ajouter une ligne :

```python
include *.txt
```

qui permettra à la commande

```python
python setup.py sdist
```

d'ajouter tout fichier txt, et là ca ira tout de suite mieux

```shell
Downloading/unpacking django-th
  Downloading django_th-0.3.0.tar.gz
  Running setup.py egg_info for package django-th
    
    warning: no previously-included files found matching 'django_th/local_settings.py'
Downloading/unpacking Django==1.4.3 (from django-th)
  Downloading Django-1.4.3.tar.gz (7.7Mb): 7.7Mb downloaded
  Running setup.py egg_info for package Django
    
Downloading/unpacking batbelt==0.4 (from django-th)
  Downloading batbelt-0.4.tar.gz
  Running setup.py egg_info for package batbelt
    
Downloading/unpacking django-profiles==0.2 (from django-th)
  Downloading django-profiles-0.2.tar.gz
  Running setup.py egg_info for package django-profiles
    
Downloading/unpacking django-registration==0.8 (from django-th)
  Downloading django-registration-0.8.tar.gz (284Kb): 284Kb downloaded
  Running setup.py egg_info for package django-registration
    
Downloading/unpacking evernote==1.23.2 (from django-th)
  Downloading evernote-1.23.2.tar.gz (132Kb): 132Kb downloaded
  Running setup.py egg_info for package evernote
    
Downloading/unpacking feedparser==5.1.3 (from django-th)
  Downloading feedparser-5.1.3.tar.gz (283Kb): 283Kb downloaded
  Running setup.py egg_info for package feedparser
    
Downloading/unpacking httplib2==0.8 (from django-th)
  Downloading httplib2-0.8.tar.gz (110Kb): 110Kb downloaded
  Running setup.py egg_info for package httplib2
    
Downloading/unpacking oauth2==1.5.211 (from django-th)
  Downloading oauth2-1.5.211.tar.gz
  Running setup.py egg_info for package oauth2
    
Downloading/unpacking ordereddict==1.1 (from django-th)
  Downloading ordereddict-1.1.tar.gz
  Running setup.py egg_info for package ordereddict
    
Downloading/unpacking South==0.7.6 (from django-th)
  Downloading South-0.7.6.tar.gz (91Kb): 91Kb downloaded
  Running setup.py egg_info for package South
    
Downloading/unpacking pytidylib==0.2.1 (from django-th)
  Downloading pytidylib-0.2.1.tar.gz (157Kb): 157Kb downloaded
  Running setup.py egg_info for package pytidylib
    
Installing collected packages: django-th, Django, batbelt, django-profiles, django-registration, evernote, feedparser, httplib2, oauth2, ordereddict, South, pytidylib
  Running setup.py install for django-th
    
    warning: no previously-included files found matching 'django_th/local_settings.py'
  Running setup.py install for Django
    changing mode of build/scripts-2.7/django-admin.py from 644 to 755
    
    changing mode of /home/foxmask/Django-VirtualEnv/toto/bin/django-admin.py to 755
  Running setup.py install for batbelt
    
  Running setup.py install for django-profiles
    
  Running setup.py install for django-registration
    
  Running setup.py install for evernote
    
  Running setup.py install for feedparser
    
  Running setup.py install for httplib2
    
  Running setup.py install for oauth2
    
  Running setup.py install for ordereddict
    
  Running setup.py install for South
    
  Running setup.py install for pytidylib
    
Successfully installed django-th Django batbelt django-profiles django-registration evernote feedparser httplib2 oauth2 ordereddict South pytidylib
Cleaning up...
```
