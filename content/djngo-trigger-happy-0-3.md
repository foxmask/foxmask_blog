Title: Django Trigger Happy 0.3
Date: 2013-06-21 23:15
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: djngo-trigger-happy-0-3
Status: published

Hey !  
Hé oui déjà une version 0.3.0 [après la
0.2.0](/post/2013/06/17/django-trigger-happy-0-2/ "Django Trigger Happy 0.2")

la méthode des petits pas ; ya rien de tel pour débuter :)

Alors rien de transcendant mais du confort pour suivre ce qui se trame
dans la récupération des informations de la toile. J'ai ajouté un
compteur de news ainsi que le nom du compte de l'utilisateur à qui
appartient le trigger qui tourne ce qui donne par exemple:

```shell
user: foxmask - provider: ServiceRss - consummer: ServiceEvernote - News de Sam et Max = 12 new data
```

j'ai mis un coup de bootstrap sur la liste des services activés et c'est
tout.

**installation**

pour l'installer je vous recommande de ne pas utiliser pip ... pypi m'a
pourri les urls du projet ; le md5 est faux l'url est fausse bref rien
de mieux que "[la
source](https://github.com/foxmask/django-th/archive/trigger-happy-0.3.0.zip)",
décompressez et faire python setup install et basta. J'espère que ça
s'arrangera pour les prochaines release; c'est la misère depuis que pypi
veut héberger les archives.

**no Future ?**  
A présent que cette version semble tenir la route, pour l'utiliser à
titre perso en prod avec près de 30 flux RSS suivis, je vais pouvoir
m'atteler à intégrer de nouveaux services.

-   [Pocket](https://github.com/foxmask/django-th/issues/17)
-   [Readability](https://github.com/foxmask/django-th/issues/18)

Ceux ci seront assez facilement mis en place puisque peu d'information
leur sont demandées de stocker et très similaires à gérer.

Mais au delà de ces derniers, si vous êtes utilisateurs de IFTTT.com,
quels services utilisez vous abondamment que vous voudriez bien me voir
ajouter à "DTH" (Django Trigger Happy) ?

Lâchez vous c'est openbar ;)

rappel : si vous n'avez pas suivi ce qu'est DTH ; [en revoici les
contours](/post/2013/05/27/django-trigger-happy/ "Django Trigger Happy – une première"),
[et en
images](/post/2013/06/04/django-trigger-happy-un-ifttt-like-en-images/ "Django Trigger Happy un IFTTT like , en images")

*edit concernant le process d'installation via pypi:*

aller, j'ai botté le train de pypi :) et tout est rentré dans l'ordre

```shell
(foobar)foxmask@:~/Django-VirtualEnv/foobar$ pip install django_th
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
    
    changing mode of /home/foxmask/Django-VirtualEnv/foobar/bin/django-admin.py to 755
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

Les dépendances sont enfin respectées.

