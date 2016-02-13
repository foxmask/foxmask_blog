Title: History not to lose the thread : TrackingFields 
Date: 2016-02-13 17:00
Author: foxmask
Category: Techno
Tags: django, python
Slug: history-not-to-lose-the-thread-trackingFields 
Status: published

## Introduction

this post is an english version [of this post made on [sam et max](http://sametmax.com/histoire-de-ne-pas-perdre-le-fil-trackingfields/) made last week.

The goal of that post will be to show how, without changing anything in a form, we can track the modifications of the data made in the application

the first part will set the scene by starting to show you how articulates an application with a form, additionally, composed by a sub form. I will explain when later. 

To do so, I takes you into the world of the 7th art, come, we will redo StarWars!

One model, one form, a view, a template and that will be finished 

## the models.py

```python
    from django.db import models
    
    
    class Movie(models.Model):
        """
            Movie
        """
        name = models.CharField(max_length=200, unique=True)
        description = models.CharField(max_length=200)
    
        def __str__(self):
            return "%s" % self.name
    
    
    class Episode(models.Model):
        """
           Episode - for Trilogy and So on ;)
        """
        name = models.CharField(max_length=200)
        scenario = models.TextField()
        movie = models.ForeignKey(Movie)
    
        def __str__(self):
            return "%s" % self.name
```

## the forms.py, very mini mini
```python
    from django import forms
    from django.forms.models import inlineformset_factory
    
    from starwars.models import Movie, Episode
    
    
    class MovieForm(forms.ModelForm):
    
        class Meta:
            """
                As I have to use : "exclude" or "fields"
                As I'm very lazy, I dont want to fill the list in the "fields"
                so I say that I just want to exclude ... nothing :P
            """
            model = Movie
            exclude = []
    
    # a formeset based on the model of the Mother "Movie" and Child "Episode" + 1 new empty lines
    EpisodeFormSet = inlineformset_factory(Movie, Episode, fields=('name', 'scenario'), extra=1)

```

## the views.py very very very DRY :)

```python
    from django.http import HttpResponseRedirect
    from django.core.urlresolvers import reverse
    from django.views.generic import CreateView, UpdateView, ListView
    
    from starwars.models import Movie
    from starwars.forms import MovieForm, EpisodeFormSet
    
    
    class MovieMixin(object):
        model = Movie
        form_class = MovieForm
    
        def get_context_data(self, **kw):
            context = super(MovieMixin, self).get_context_data(**kw)
            if self.request.POST:
                context['episode_form'] = EpisodeFormSet(self.request.POST)
            else:
                context['episode_form'] = EpisodeFormSet(instance=self.object)
            return context
    
        def get_success_url(self):
            return reverse("home")
    
        def form_valid(self, form):
            formset = EpisodeFormSet((self.request.POST or None), instance=self.object)
            if formset.is_valid():
                self.object = form.save()
                formset.instance = self.object
                formset.save()
    
            return HttpResponseRedirect(reverse('home'))
    
    
    class Movies(ListView):
        model = Movie
        context_object_name = "movies"
        template_name = "base.html"
    
    
    class MovieCreate(MovieMixin, CreateView):
        """
            MovieMixin manage everything for me ...
        """
        pass
    
    
    class MovieUpdate(MovieMixin, UpdateView):
        """
            ... and I'm DRY :D
        """
        pass
```

## To finish to set the scene and the costumes : the templates

### base.html
```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <title>Manage stories for StarWars</title>
    </head>
    <body>
    <h1>Stories Manager for Starwars</h1>
    {% block content %}
    <a href="{% url 'movie_create' %}">Add a movie</a><br/>
    <h2>Movie list</h2>
    <ul>
    {% for movie in movies %}
    <li><a href="{% url 'movie_edit' movie.id %}">{{ movie.name }}</a></li>
    {% endfor %}
    </ul>
    {% endblock %}
    </body>
    </html>
```

### movie_form.htlm (the template used by UpdateView & CreateView)

```html
    {% extends "base.html" %}
    {% block content %}
    <form method="post" action="">
        {% csrf_token %}
        {{ formset.management_form }}
        <table>
        {{ form.as_table }}
        </table>
        <table>
        {{ episode_form.as_table }}
        </table>
        <button>Save</button>
    </form>
    {% endblock %}
```

## Update of the database 

this is necessary  :

```bash
(starwars) foxmask@foxmask:~/DjangoVirtualEnv/starwars/starwars $  ./manage.py migrate

Operations to perform:
  Synchronize unmigrated apps: messages, starwars, staticfiles
  Apply all migrations: contenttypes, admin, sessions, auth
Synchronizing apps without migrations:
  Creating tables...
    Creating table starwars_movie
    Creating table starwars_episode
    Running deferred SQL...
  Installing custom SQL...
```

Here we are, ready, I can now create my double Trilogy like Georges Lucas

## Tracking the ungodly

But a day comes when me, George Lucas, I sell StarWars to Walt Disney, but I want to miss
what they will do my "baby", I add a "tracker changes" in my application, not to lose the "field" of history.

### Installation of Tracking Fields

as a prerequisites, if you want to also track who change thing, and not what data have been whanged, you will need  
django-current-user, so the pip command to use will be this one 

```python
    (starwars) foxmask@foxmask:~/DjangoVirtualEnv/starwars/starwars $ pip install django-tracking-fields django-cuser
    Collecting django-tracking-fields
      Downloading django-tracking-fields-1.0.6.tar.gz (58kB)
        100% |████████████████████████████████| 61kB 104kB/s 
    Collecting django-cuser
      Downloading django-cuser-2014.9.28.tar.gz
    Requirement already satisfied (use --upgrade to upgrade): Django>=1.5 in /home/foxmask/DjangoVirtualEnv/starwars/lib/python3.5/site-packages (from django-cuser)
    Installing collected packages: django-tracking-fields, django-cuser
      Running setup.py install for django-tracking-fields ... done
      Running setup.py install for django-cuser ... done
    Successfully installed django-cuser-2014.9.28 django-tracking-fields-1.0.6
```

the necessary changes in  **settings.py** :

```python
    INSTALLED_APPS = (
        ...
        'cuser',
        'tracking_fields',
        ...
    )
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'cuser.middleware.CuserMiddleware',  ## <=== do not forget to catch the badass who make change on my movies;)
    )
```

the little migrate that fit our needs, to add the tables for our modeles of django-tracking-fields

```python
    (starwars) foxmask@foxmask:~/DjangoVirtualEnv/starwars/starwars $  ./manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: staticfiles, messages, cuser, starwars
      Apply all migrations: auth, sessions, contenttypes, tracking_fields, admin
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
      Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying tracking_fields.0001_initial... OK
      Applying tracking_fields.0002_auto_20160203_1048... OK
```
and here we are ready to play with the trackers


### Usage

We cant dream a more simpler way to do, this can be summarize to a decorator on the model which identifies which data are changed, 
and on field ̀`histo` which will link the model TrackingEvent of the application TrackingFields, to my tacle to watch.
And here, even if my model has been changed with this new field, it's unecessary to do a new "python manage.py migrate", nothing will happen, 
because histo will be a [GenericRelation()](https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#generic-relations).   
Effectivly, TrackingEvent is based of [ContenType](https://docs.djangoproject.com/e,/1.9/ref/contrib/contenttypes/) aka
En effet, TrackingEvent repose sur [ContenType](https://docs.djangoproject.com/fr/1.9/ref/contrib/contenttypes/) aka "The contenttypes framework". 
If you already played with the permission management, you should have already  meet it before;)


To make it short, this will give :

#### models.py

```python
    from django.db import models
    from django.contrib.contenttypes.fields import GenericRelation
    
    from tracking_fields.decorators import track
    from tracking_fields.models import TrackingEvent
    
    
    @track('name', 'description')
    class Movie(models.Model):
        """
            Movie
        """
        name = models.CharField(max_length=200, unique=True)
        description = models.CharField(max_length=200)
        histo = GenericRelation(TrackingEvent, content_type_field='object_content_type')
    
        def episodes(self):
            return Episode.objects.filter(movie=self)
    
        def __str__(self):
            return "%s" % self.name
    
    @track('name', 'scenario')
    class Episode(models.Model):
        """
           Episode - for Trilogy and So on ;)
        """
        name = models.CharField(max_length=200)
        scenario = models.TextField()
        movie = models.ForeignKey(Movie)
        histo = GenericRelation(TrackingEvent, content_type_field='object_content_type')
    
        def __str__(self):
            return "%s" % self.name
```

so, here, it is very simple like a pancake recipe: 3 imports, the decorator, the  GenericRelation, we mix all of them and that give what follow.
I have, in the meantime, added a function `episodes` to my Movie class, I will explain it too later ;)
 
### the template of the expected DetailView 

```html
    <table>
       <caption>History of the modification of {{ object }} </caption>
       <thead>
       <tr><th>Old Value</th><th>New Value</th><th>By</th><th>at</th></tr>
       </thead>
       <tbody>
    {% for h in object.histo.all %}
       {% for f in h.fields.all %}
           <tr><td>{{ f.old_value }}</td><td>{{ f.new_value }}</td><td>{{ h.user }}</td><td>{{ h.date }}</td></tr>
       {% endfor %}
    {% endfor %}
       </tbody>
    </table>
```
Now if I go the my page to modify the story of one episode, my template below, wont display thoses modifications !
But Why god ? Because until here, I just display the "histo" of Movie and not of the Episode. We now understand here my interest for the sub form.
The issue 


### Let's fix it

this is here, that enter if the game, the function `episodes` of my Movie class to permit to loop on it and display of the needed stuff 

### the template of the expected DetailView (again :)

```html
    <table>
        <caption>History of the modifications of {{ object }} </caption>
        <thead>
            <tr><th>Old Value</th><th>New Value</th><th>By</th><th>at</th></tr>
        </thead>
        <tbody>
    {% for h in object.histo.all %}
       {% for f in h.fields.all %}
           <tr><td>{{ f.old_value }}</td><td>{{ f.new_value }}</td><td>{{ h.user }}</td><td>{{ h.date }}</td></tr>
       {% endfor %}
    {% endfor %}
        </tbody>
    </table>
    {% for ep in object.episodes %}
        {% if ep.histo.all %}
    <table>
        <caption>history of the modifications of Episode</caption>
        <thead>
            <tr><th>Old Value</th><th>New Value</th><th>By</th><th>at</th></tr>
        </thead>
        <tbody>
            {% for h in ep.histo.all %}
                {% for f in h.fields.all %}
                {% if f.old_value == f.new_value %} {# they are the same when the new value is created to avoid to display "null" #}
                {% else %}
                <tr><td>{{ f.old_value }}</td><td>{{ f.new_value }}</td><td>{{ h.user }}</td><td>{{ h.date }}</td></tr>
                {% endif %}
                {%  endfor %}
            {% endfor %}
        </tbody>
     </table>
        {% endif %}
    {% endfor %}
```

And voilà !
Voili voilou ! As a bonus, if you're curious, of the admin side, you also have a list of all the changes if needed;)

For the advanced users who would say:

> why have recoded the front side since this is already managed on the admin side without lifting a finger?

Because George Lucas wants to show changes to his baby StarWars by Walt Disney, to the world of course 

Ho, and a last detail : in the admin, the view which displays the list of changes gives : "Episode Object" or "Movie Object".
To avoid that, you shoud have notice that I have added the function  **__str__**  in my model which will return a more
readable value of what have been changed


## Conclusion : 

IRL, I didnt see myself, create a History model linked physically by a FK on each model, I decide to search, arround the web, some ressources 

It's finally on [#django-fr@freenode](irc://irc.freenode.net/django-fr) that I asked my question and got from [Gagaro](https://github.com/gagaro) the grââl : 
one application named [tracking-fields](https://github.com/makinacorpus/django-tracking-fields), his author.


For once I do my lazy by not coding all by myself, [it's nice to come across such an app](https://github.com/makinacorpus/django-tracking-fields) ! 

If you want to play with the code of this Movie manager [here is the tasty soup](https://github.com/foxmask/tracking-starwars)
