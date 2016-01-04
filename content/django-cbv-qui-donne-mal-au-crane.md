Title: Django CBV qui donne mal au crane
Date: 2013-06-30 12:23
Author: foxmask
Category: Techno
Tags: Django, python
Slug: django-cbv-qui-donne-mal-au-crane
Status: published

Toujours dans la veine des bouts de code qu'un n00b produit et se tend
en piège, voici une erreur à laquelle j'ai eu droit et qui pour autant,
sans attirer mon attention, en prod fini en erreur 500 ... et là arrive
le mal de crane... parce que debugger sans le DEBUG à True en prod ...
walou ...

```python
TypeError at /
int() argument must be a string or a number, not 'SimpleLazyObject'
```

le code incriminé est celui ci :

```python
class TriggerListView(ListView):
    def get_context_data(self, **kw):
        context = super(TriggerListView, self).get_context_data(**kw)
        enabled = TriggerService.objects.filter(user=self.request.user, status=1)
        disabled = TriggerService.objects.filter(user=self.request.user, status=0)
        context['nb_triggers'] = {'enabled': len(enabled), 'disabled': len(disabled)}
        return context
```

la ligne enable = ... ne convient pas quand on n'est pas connecté.  
j'imaginais que user= prendrait rien puisque la session n'existait pas.
erreuuuuuuuuuuuuuuuuuur !

pour résoudre le problème de cette ListView il faut donc la faire
proprement :

```python
    def get_context_data(self, **kw):
        enabled = disabled = ()
        if self.request.user.is_authenticated():
            enabled = TriggerService.objects.filter(user=self.request.user, status=1)
            disabled = TriggerService.objects.filter(user=self.request.user, status=0)
        context = super(TriggerListView, self).get_context_data(**kw)
        context['nb_triggers'] = {'enabled': len(enabled), 'disabled': len(disabled)}
        return context
```

et là enfin quand on accède à la ListView sans être connecté tout sera
en ordre

