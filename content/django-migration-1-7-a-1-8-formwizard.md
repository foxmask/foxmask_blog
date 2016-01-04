Title: Django Migration 1.7 à 1.8, FormWizard, InlineFormSet, Url from Future
Date: 2015-04-03 11:41
Author: foxmask
Category: Techno
Tags: Django, TriggerHappy
Slug: django-migration-1-7-a-1-8-formwizard
Status: published

Même si la la doc est superbement complète, je m'en vais vous narrer ci
et là les surprises qui ont jonché le chemin de ma migration

Comme tout à chacun j'ai donc fait :

```python
pip install -U django 
...
./manage.py test
```

Je suis tombé sur des erreurs sur django-debug-toolbar parce que resté
en 0.9.5, donc estompées dès la 1.3.0 mise à jour.

Puis vint des suées :

```python
Traceback (most recent call last):
  File "./manage.py", line 10, in 
    execute_from_command_line(sys.argv)
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 338, in execute_from_command_line
    utility.execute()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 312, in execute
    django.setup()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/__init__.py", line 18, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/apps/registry.py", line 115, in populate
    app_config.ready()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/debug_toolbar/apps.py", line 15, in ready
    dt_settings.patch_all()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/debug_toolbar/settings.py", line 232, in patch_all
    patch_root_urlconf()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/debug_toolbar/settings.py", line 220, in patch_root_urlconf
    reverse('djdt:render_panel')
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 550, in reverse
    app_list = resolver.app_dict[ns]
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 352, in app_dict
    self._populate()
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 285, in _populate
    for pattern in reversed(self.url_patterns):
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 402, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/core/urlresolvers.py", line 396, in urlconf_module
    self._urlconf_module = import_module(self.urlconf_name)
  File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/django_th/django_th/urls.py", line 9, in 
    from django_th.views import TriggerListView, TriggerDeleteView,   
 File "/home/foxmask/Django-VirtualEnv/django-trigger-happy/django_th/django_th/views.py", line 13, in 
    from django.contrib.formtools.wizard.views import SessionWizardView
ImportError: No module named formtools.wizard.views
```

Alors là, le désagrément majeure pour bibi et "[Trigger
Happy](http://trigger-happy.eu)", c'est que toutes mes pages permettant
de créer des services, reposent entierement sur le Wizard...

[En creusant la
doc](https://docs.djangoproject.com/en/1.8/ref/contrib/formtools/) on
apprend que les wizard sont sortis des contrib pour devenir une app à
part : [Formtools](http://django-formtools.readthedocs.org/en/latest/)

Il faut donc ajouter `"formtools"` au `INSTALLED_APPS` après avoir fait
un

```python
pip install django-formtools
```

Puis on relance les tests :

```python
 ./manage.py test
Creating test database for alias 'default'...
........................................
----------------------------------------------------------------------
Ran 40 tests in 1.998s

OK
Destroying test database for alias 'default'...
```

ou avec un petit coup de

```python
Creating test database for alias 'default' (':memory:')...
Operations to perform:
  Synchronize unmigrated apps: staticfiles, django_th, messages, pocket, th_rss, django_js_reverse, th_pocket, debug_toolbar, formtools
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Creating table django_th_servicesactivated
    Creating table django_th_userprofile
    Creating table django_th_userservice
    Creating table django_th_triggerservice
    Creating table django_th_rss
    Creating table django_th_pocket
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
test_servicesactivated (django_th.tests.test_models_and_services.ServicesActivatedTest) ... ok
test_invalid_form (django_th.tests.test_models_and_services.TriggerServiceTest) ... ok
test_triggerservice (django_th.tests.test_models_and_services.TriggerServiceTest) ... ok
test_valid_form (django_th.tests.test_models_and_services.TriggerServiceTest) ... ok
test_userprofile (django_th.tests.test_models_and_services.UserProfileTest) ... ok
test_invalid_form (django_th.tests.test_models_and_services.UserServiceTest) ... ok
test_userservice (django_th.tests.test_models_and_services.UserServiceTest) ... ok
test_valid_form (django_th.tests.test_models_and_services.UserServiceTest) ... ok
test_get (django_th.tests.test_views.TriggerDeletedTemplateViewTestCase) ... ok
test_get (django_th.tests.test_views.TriggerEditedTemplateViewTestCase) ... ok
test_context_data (django_th.tests.test_views.TriggerListViewTestCase) ... ok
test_get (django_th.tests.test_views.UserServiceAddedTemplateViewTestCase) ... ok
test_get (django_th.tests.test_views.UserServiceDeletedTemplateViewTestCase) ... ok
test_context_data (django_th.tests.test_views.UserServiceListViewTestCase) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.889s

OK
Destroying test database for alias 'default' (':memory:')...
```

[si vous voulez voir la politique de dépréciation de
Django](https://docs.djangoproject.com/en/dev/internals/release-process/#internal-release-deprecation-policy).
Bon je n'y ai pas trouvé le "pourquoi" cette "contrib", à l'origine,
avait été retirée à présent.

Le billet évoluera probablement plus tard selon mes aventures sur le
sujet ;)

**Edit du 10/04 (minuit:)**  
les `inlineformset_factory` ayant évolués, il n'est à présent plus
possible de spécifier ET `form_class` ET `fields` dans la vue, c'est
l'un ou l'autre voire même que dalle si dans le `inlineformset_factory`
on colle le nom des fields qui nous interessent. [tout dans la
doc](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#inline-formsets)
;)

[De même en 1.7 on pouvait se contenter
d'écrire](https://docs.djangoproject.com/en/1.7/topics/forms/modelforms/#inline-formsets)
:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)

>>> from django.forms.models import inlineformset_factory
>>> BookFormSet = inlineformset_factory(Author, Book)
```

mais ceci ne va plus du tout, il faut bien spécifier une liste de fields
pleine ou vide (si ca vous chante:)

```python
>>> from django.forms.models import inlineformset_factory
>>> BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
```

**edit du 12/04**  
une nouvelle erreur qui saute aux yeux :

```python
/home/foxmask/Django-VirtualEnv/django-trigger-happy/local/lib/python2.7/site-packages/django/templatetags/future.py:25: RemovedInDjango19Warning: Loading the `url` tag from the `future` library is deprecated and will be removed in Django 1.9. Use the default `url` tag instead.
  RemovedInDjango19Warning)
```

celle ci est dûe à un

```python
{% load url from future %}
```

dans les templates

