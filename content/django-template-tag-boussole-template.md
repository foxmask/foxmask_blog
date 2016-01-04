Title: Django, un template tag, une boussole dans le template
Date: 2012-10-13 16:30
Author: foxmask
Category: Techno
Tags: Django
Slug: django-template-tag-boussole-template
Status: published

Dans un template utilisé tout au long de son site, tel un menu, je
voulais trouver un moyen de savoir quelle vue l'avait appelé afin de
positionner une classe CSS 'active' au bon endroit.

Dans mes recherches j'ai trouvé [A Django template tag for the current
active
page](http://gnuvince.wordpress.com/2007/09/14/a-django-template-tag-for-the-current-active-page/),
où au début j'avais le me cheminement consistant à parser request.path,
ensuite j'ai mis la main sur une amélioration de la proposition
précédente [sur ce
blog](http://110j.wordpress.com/2009/01/25/django-template-tag-for-active-class/)...
que j'ai à mon tour modifié ;)

Voici ce que ça donne dans un template :

```python
{% url 'base' as home %}
{% url 'profiles_profile_detail' request.user.username as profiles_profile_detail %}
{% url 'relationship_list' request.user.username 'friends' as relationship_list_friends %}              


     {% trans "Home" %}
     {{ request.user.username }}
     {% trans "My network" %}
     {% trans "log out" %}                        
```

Mon grin de sel se situe coté HTML où je ne veux pas laisser dans la
page HTML des propriétés vides [comme on le voit
ici](http://110j.wordpress.com/2009/01/25/django-template-tag-for-active-class/)

Du coup je retourne bêtement **class="active"** plutôt que **active**

```python
@register.simple_tag
def active(request, pattern):
    import re
    pattern = "^%s$" % pattern
    if re.search(pattern, request.path):
        return ' class="active" '
    return ''
```
