Title: ActionForm Django à la rescousse !
Date: 2016-03-23 22:30
Author: foxmask
Tags: django, actionform
Category: Techno
Slug: actionform-django-a-la-rescousse
Status: published


Un besoin se fit ressentir today :

Pouvoir, depuis la page d'administration de django, réaffecter des données se trouvant dans un service et les mettre dans un autre.

Comme le montre la [doc](https://docs.djangoproject.com/fr/1.8/ref/contrib/admin/actions/#adding-actions-to-the-modeladmin), on peut effectuer des actions à sa sauce comme ceci :

```python
from django.contrib import admin
from myapp.models import Article

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Article, ArticleAdmin)
```


Arrive le moment où c'est sympa, mais ceci ne suffit plus.

![page de l'admin classique](/static/2016/03/admin_standard.png)

Si j'ai à ventiler des données à partir de données se trouvant dans un autre modèle, je vais pas créer 'n' make_published_x,y,z .

Et le DRY là dedans, hmmm? :P

Pour arriver à ses fins, un helper existe tout de même, il s'agit d'[ActionForm](https://github.com/django/django/blob/master/django/contrib/admin/helpers.py#L26).

Dans mon module `admin.py` j'y mettrai donc un truc du genre

```python
class ServicesActivatedActionForm(ActionForm):
    provider = forms.ChoiceField(choices=ServicesActivated.objects.values_list('id', 'name'))
    consumer = forms.ChoiceField(choices=ServicesActivated.objects.values_list('id', 'name'))
```

on notera en passant l'astuce pour fournir à `choices` un `tuple` qui provient du modèle, grâce à l'utilisation de `values_list()`

Puis dans le ModelAdmin je glisse :

```python
class TriggerServiceAdmin(admin.ModelAdmin):
    action_form = ServicesActivatedActionForm
```

Ce qui aura pour effet, d'afficher à coté de la liste déroulante des actions, une liste déroulante des mes provider/consumer.

En l'état ça ne suffit pas pour fonctionner complètement. Il faut évidement gérer la validation du choix du provider/consumer comme suit :

```python
    def change_service(self, request, queryset):
        provider = request.POST['provider']
        consumer = request.POST['consumer']
        queryset.update(provider=provider, consumer=consumer)

    change_service.short_description = 'Change of Service'
```

A présent, ma liste d'actions contient 2 actions, la suppression (action par defaut proposer par l'admin) et la mienne. Tout ça à gauche de ma liste déroulante des provider/consumer !

![page de l'admin avec les actions](/static/2016/03/admin_actionform.png)

Le code complet à présent donne :

```python
from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms

from django_th.models import TriggerService


class ServicesActivatedActionForm(ActionForm):
    provider = forms.ChoiceField(choices=ServicesActivated.objects.values_list('id', 'name'))
    consumer = forms.ChoiceField(choices=ServicesActivated.objects.values_list('id', 'name'))


class TriggerServiceAdmin(admin.ModelAdmin):

    list_display = ('user', 'provider', 'consumer', 'description',
                    'date_created', 'date_triggered', 'status')
    list_filter = ['user', 'provider', 'consumer', 'status']
    action_form = ServicesActivatedActionForm

    def change_service(self, request, queryset):
        provider = request.POST['provider']
        consumer = request.POST['consumer']
        queryset.update(provider=provider, consumer=consumer)

    change_service.short_description = 'Change of Service'
    actions = [change_service]


admin.site.register(TriggerService, TriggerServiceAdmin)
```


Voilou pour le tips du jour ;)
