Title: Django Shortener clap une première
Date: 2012-09-30 21:32
Author: foxmask
Category: Techno
Tags: Django
Slug: django-shortener-clap-une-premiere
Status: published

Ce soir, me suis fendu d'un mini module django permettant de gérer son
propre service de raccourcisseurs d'URL tel bitly et ses amis.

**Premier effet kisskool : un service "con comme la lune"**

On dépose une longue URL, le module vous en retourne une version courte.

2 petits paramètres sont nécessaire dans votre fichier settings.py: la
taille de l'URL courte, l'hôte hébergeant le service (si ce n'est pas le
domaine courant).

Quand c'est fait vous faites votre copier coller de l'URL courte dans
votre texte et "voilà" comme ils disent outre manche ;)

**Deuxième effet kisskool : intégration avec d'autres modules**

Comme le service ne pouvait s'en tenir là, j'ai aussi produit un
template processor permettant de parser une string pour en extraire
*toutes les* URLs et en ressortir une version courte pour chaque !

```python
{{ my_nice_text | shrt }}
```

on peut bien évidement ajouter une ribambelle de filtres à la suite

```python
{{ my_nice_text | shrt | safe |escape}}
```

**Où trouver le module ?**

Pour tester ce module vous avez la possibilité de le trouver sur
[PyPi](http://pypi.python.org/pypi/django_shortener/), ou de taper

```python
pip install django_shortener
```

ou de vous faire [un fork sur
github](https://github.com/foxmask/django_shortener).

Tout retour sur ce module sera apprécié comme c'est le premier, j'espère
d'une longue série ;)

