Title: Django filtrer les données d'une ListView avec Q()
Date: 2014-05-06 11:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-filtrer-listview
Status: published

J'étais parti pour vous faire un article funny avec James Bond,
Monneypenny, et Q, mais restons soft ;)

Donc dans cet article je vais aborder une fonction toute "simple" et
ultra pratique : [Lookup with Q
Objects](https://docs.djangoproject.com/en/1.6/topics/db/queries/#complex-lookups-with-q-objects).

Le but de cette fonction est de gérer des requêtes SQL pour produire
quelque chose du genre :

```sql
SELECT col1, col2 FROM table1 WHERE user = 'foobar' AND (col1='2' OR col2='2');
```

C'est la partie après le AND qui est gérée par **Q()**

Ca serait simple si on se contentait d'utiliser cela dans une FBV en
récupérant le paramètre nommé dans urls.py, mais là, chez bibi, c'est
dans une CBV ListView que ça va servir, donc un poil plus subtile que
ça.

Dans la version précédente ma
[ListView](https://docs.djangoproject.com/en/1.6/ref/class-based-views/generic-display/#listview "ListView")
avait cette tête :

```python
class TriggerListView(ListView):
    context_object_name = "triggers_list"
    queryset = TriggerService.objects.all()
    template_name = "home.html"
    paginate_by = 7

    def get_queryset(self):
        # get the Trigger of the connected user
        if self.request.user.is_authenticated():
            return self.queryset.filter(user=self.request.user).  
               order_by('-date_created')
        # otherwise return nothing
        return TriggerService.objects.none()
```

Là, aucun filtrage des données depuis le template, affichage pour et
simple de toutes les données de l'utilisateur connecté.

L'ajout du filtrage va donc toucher les éléments suivants :

1.  views.py pour l'ajout des données peuplant la liste depuis
    **get\_context\_data** de la ListView
2.  le template pour afficher la liste des valeurs permettant le
    filtrage
3.  urls.py pour ajouter le mapping url/views
4.  views.py pour ajouter la logique de traitement de filtrage dans la
    methode **get\_queryset** de la ListView

**1 - Ajout des données peuplant la liste du point 1**

```python
class TriggerListView(ListView):

    """
    list of Triggers
    the list can be filtered by service
    """
    context_object_name = "triggers_list"
    queryset = TriggerService.objects.all()
    template_name = "home.html"
    paginate_by = 7

    def get_context_data(self, **kw):
        """
        List of triggers activated by the user
        """
        if self.request.user.is_authenticated():
            context['trigger_filter_by'] = UserService.objects.filter(
                user=self.request.user)

        return context
```

**2 - Template, affichage de la liste pour filtrage**

```python
            
                 
                
                {% for trigger_filter in trigger_filter_by %}
                    {{ trigger_filter.name|service_readable }}
                {% endfor %}
                
            
```

**3 - urls.py**

```python
    url(r'^th/$', TriggerListView.as_view(), name='base'), 
    #ajouté pour gerer le filtrage
    url(r'^th/trigger/by/(?P[a-zA-Z]+)$', TriggerListView.as_view(), name='trigger_filter_by'),
```

**4 - Logique de traitement du filtrage**

```python
class TriggerListView(ListView):

    """
    list of Triggers
    the list can be filtered by service
    """
    context_object_name = "triggers_list"
    queryset = TriggerService.objects.all()
    template_name = "home.html"
    paginate_by = 7

    def get_queryset(self):
        trigger_filter_by = None
        # get the Trigger of the connected user
        if self.request.user.is_authenticated():
            # if the user selected a filter, get its ID
            if 'trigger_filter_by' in self.kwargs:
                user_service = UserService.objects.filter(
                    user=self.request.user, name=self.kwargs['trigger_filter_by'])
                trigger_filter_by = user_service[0].id

            # no filter selected : display all
            if trigger_filter_by is None:
                return self.queryset.filter(user=self.request.user).order_by('-date_created')
            # filter selected : display all related trigger
            else:
                # here the queryset will do :
                # 1) get trigger of the connected user AND
                # 2) get the triggers where the provider OR the consumer match
                # the selected service
                return self.queryset.filter(user=self.request.user).filter(Q(provider=trigger_filter_by) | Q(consumer=trigger_filter_by)).order_by('-date_created')
        # otherwise return nothing when user is not connected
        return TriggerService.objects.none()
```

Ainsi donc ici on voit où entre en compte le Q objects :

```python
.filter(Q(provider=trigger_filter_by) | Q(consumer=trigger_filter_by)
```

ceci produit le "OR" attendu puisque je souhaite bel et bien TOUS les
triggers de l'utilisateur connecté ET soit les *provider* soit les
*consumer* contenant la valeur recherchée dans la liste déroulante.

Avant d'arriver à cette solution, je cherchais à ajouter un Form à
ListView pour produire une dropdown (un select html)... mais vu la
complexité du code pour gérer l'ajout du form au context ou pas, je me
suis rabattu sur une simple liste html, et hop Q() à la rescousse ;)

Tout est dans la "Simplicity, Efficiency, Beauty" ;)

si besoin, pour les curieux, [Le code source original de cette Views.py
sur
Github](https://github.com/foxmask/django-th/blob/trigger-happy-0.9.0/django_th/views.py)

