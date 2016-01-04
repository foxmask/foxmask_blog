Title: Django, la doc, en PDF c'est mieux
Date: 2010-08-24 23:23
Author: foxmask
Category: Techno
Tags: Django
Slug: django-doc-en-pdf-cest-mieux
Status: published

Afin de rentabiliser le temps que je perds dans les transports
parisiens, et ayant envi de découvrir
[Django](http://www.djangoproject.com/), me suis dit qu'il me faudrait
bien la documentation de [Django](http://www.djangoproject.com/) sur mon
p'tit iPodTouch.

Donc je me suis farci le site <http://www.djangoproject.com/> en long en
large et en travers à la recherche d'un PDF, mais en vain.

En faisant [une petite recherche sur
google](http://www.google.fr/search?q=django+pdf), je me jette sur [un
vieux billet de
2008](http://www.biologeek.com/2008/12/la-documentation-django-en-local-html-et-pdf/),
qui indique la marche à suivre pour ... se générer la documentation
soi-même.

Ok, je vais pas m'arrêter là, suis motivé :-)

hop installation des outils **easy\_install** et du support **latex**

```shell
apt-get install python-setuptools
apt-get install python-plastex
apt-get install python-sphinx
apt-get install texlive-full (necessaire sinon erreur à la compilation latex=>pdf)
```

Mais au moment de la compilation sur ma debian (5.0) via :

```shell
sphinx-build -b latex . build_latex
```

l'avion crash en plein vol ...

```shell
The process fails when it tries to do an import:
from sphinx.directives.desc import option_desc_re
```

Bon, pour ne pas passer pour un enquiquineur de première sur la ML
django-fr, [je m'en retourne voir
google](http://www.google.fr/search?q=sphinx+impot+option_desc_re+no+module+named+desc),
et [nouvelle
trouvaille](http://osdir.com/ml/DjangoUsers/2010-08/msg00907.html)

J'apprends là bas qu'il faut une mise à jour issue tout droit du trunk
django, et qui consiste donc à copier [le fichier
djangodocs.py](http://code.djangoproject.com/svn/django/branches/releases/1.2.X/docs/_ext/djangodocs.py)
en lieu et place de celle de la 1.2.1.... et rebuilder

Reste donc **enfin** à produire le pdf :)

```shell
latex build_latex/django.tex django.pdf
```

Et là miracle, ca repète :)

```shell
tex capacity exceeded, sorry [save=5000]
```

rebelote google tout çaaaaaaaaaaaa, on doit donc éditer

```shell
/usr/share/texmf/web2c/texmf.cnf
```

et changer la valeur de `save_size`

retestage :

```shell
latex build_latex/django.tex django.pdf
Output written on django.pdf (1032 pages, 5261614 bytes)
```

Aaaaaaaaaaaaah enfin je peux le transférer dans iBooks sur l'iPodTouch

Quel périple juste pour un PDF, gageons que la suite sera moins
"rigolote" .

Ben en fait c'est pas génial :/ dans le PDF, le code écrit en noir sur
fond noir ça le fait pas du tout.

**EDIT** : après un retour à la [doc du projet lui
même](http://docs.djangoproject.com/en/dev/internals/documentation/)
j'ai fini par faire plus simple et ça marche :

Donc on se rend dans le dossier "doc" et on tape juste :

```shell
make latex
```

puis

```shell
cd _build/latex
make all-pdf
```

pour obtenir

```shell
Output written on django.pdf (1057 pages ...)
```

et cette fois ci on a le code illustrant la doc tout à fait lisible :)

[La Doc Django 1.2.1 en PDF est doc
là](/post/2010/08/24/django-doc-en-pdf-cest-mieux/django-1-2-1/)
:)

**EDIT2** : c'est bien lisible dans iBooks :D à moi le mille feuilles
dans le RER :-)

