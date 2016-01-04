Title: Django reverse for xxx with arguments ... not found
Date: 2012-08-31 10:30
Author: foxmask
Category: Techno
Tags: Django
Slug: django-reverse-for-xxx-with-arguments-not-found
Status: published

Nombreux sont ceux qui tombent dans le piège de cette erreur qui semble
être une erreur de noobs ...  
Cette erreur la voici :

```python
Erreur :
NoReverseMatch at /histo/
Reverse for ''histo_save'' with arguments '()' and keyword 
arguments '{}' not found.
```

Pour autant tout semble être correct, le fichier **urls.py** contient

```python
url(r'^histo/$','tglr.views.histo',name='histo'),
```

Tantdis que le **template** lui contient

``` {language="python"}

{% csrf_token %}
```

Donc tout semble parfaitement tourner rond sauf que ... dans la console
saute aux yeux :

```shell
/usr/local/lib/python2.6/dist-packages/django/template/defaulttags.py:1235: 
DeprecationWarning: The syntax for the url template tag is changing.
Load the `url` tag from the `future` tag library to start using the new behavior.
category=DeprecationWarning)
```

Okkkayyyyy donc dans le template on rajoutera :

```python
{% load url from future %}
```

et tout rentrera dans l'ordre

Pour info j'aurai pu faire sauter les simples quotes autour de
*histo\_save* mais comme le dit le *DeprecationWarning*, utiliser {% url
toto %} est déprécié

