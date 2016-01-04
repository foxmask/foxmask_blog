Title: Quand Django reste muet à vous rendre dingue
Date: 2012-12-19 22:59
Author: foxmask
Category: Techno
Tags: Django
Slug: quand-django-reste-muet-a-vous-rendre-dingue
Status: published

Voici un truc qui m'a usé les nerfs (de noob mais pas que :P) avec
[Django](https://docs.djangoproject.com/ "Django Project - the web framework for perfectionnists with deadline").

je me fais un template principale, con à souhait, dans lequel je fais un
include, "QQ la praline", comme suit :

**base.html**

```python


{% load static %}
{% load staticfiles %}
{% load i18n %}
{% load url from future %}
[...]
{% include "mark_forum.inc.html" %}
```

dans **mark\_forum.inc.html**

```python
    
    {% trans "Mark all forum as read" %}
    {% if current_id_forum > 0 %}
    {% trans 'Mark this forum as read' %}
    {% endif %}
    {% trans 'Show new posts' %}
    {% if current_id_forum > 0 %}
        {% if subscribed_to_this_forum %}
    {% trans 'Unsubscribe to this forum' %}
        {% else %}
    {% trans 'Subscribe to this forum' %}
        {% endif %}
    {% endif %}
```

je lance mon appli et dans la console, me saute aux yeux

```shell
lib/python2.6/site-packages/django/template/defaulttags.py:1235: DeprecationWarning: The syntax for the url template tag is changing. Load the `url` tag from the `future` tag library to start using the new behavior.
```

donc j'ajoute à **mark\_forum.inc.html** (malgré l'ajout existant dans
l'index.html)

```python
{% load url from future %}
```

et je relance ... et là plus d'erreur dans la console ! Yeah !

je me dis nickel ca marche, avancons ! ... ben non.  
**Aucun** message d'erreur et le template que je tente d'inclure
affiche ... rien !

Donc je sors le scalpele et pars décortiquer tout le code du template.  
Je retire tout et colle un beau coucou à la place de tout le reste ;
qui s'affiche.  
Bon déjà je me dis ok je suis pas débile c'est bien comme ça que
l'inclusion marche (vin diou).  
Je rajoute mon premier noeud li et là re patatra plus rien ne
s'affiche...  
Comme le problème de syntaxe sur *url* n'est plus en cause je me dis
voyons *trans* et mettons une string pipo ~~alakon~~.

Et là Bingo ! Il me manque donc

```python
{% load "i18n" %}
```

J'avais imaginé que le template inclus récupérait le contexte parent et
donc le load que j'avais fait dans le index.html.... que néni... comme
pour le load url en fait.

Mais là où j'ai mis le temps c'est, comme je l'ai dit plus tôt AUCUN
message d'erreur me dit que je tente d'utiliser un "template tag" que je
n'ai pas chargé avant ... Une bosse grosse engueulade comme pour le
*load url from future* m'aurait largement aidé ;)

Là franchement c'est très bas de la part de Django :P

Si quelqu'un a une explication sur le mutisme de Django là dessus, je
lui en serai gré ;)

