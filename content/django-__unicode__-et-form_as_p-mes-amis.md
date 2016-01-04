Title: Django __unicode__ et form.as_p mes amis
Date: 2013-01-21 10:00
Author: foxmask
Category: Techno
Tags: Django
Slug: django-__unicode__-et-form_as_p-mes-amis
Status: published

Toujours dans mes périgrinations de débutant, voici un coup qui m'a pris
du temps à trouver seul, donc si ça peut servir à d'autres ;)

Donc voici,

**Chapitre Un \_\_unicode\_\_**

je veux produire une page pour afficher un formulaire composé de 2
listes déroulantes issues d'un autre modèle + un champ de texte

j'ai composé le modèle suivant :  
**models.py**

```python
class TriggerType(models.Model):
    """
        TriggerType
    """
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=140)


class TriggerService(models.Model):
    """
        TriggerService
    """
    provider = models.ForeignKey(TriggerType, related_name='+', blank=True)
    consummer = models.ForeignKey(TriggerType, related_name='+', blank=True)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date_created = models.DateField()
```

et voici mon formulaire  
**forms.py**

```python
class TriggerServiceForm(forms.ModelForm):
    """
        Trigger Form
    """
    class Meta:
        """
            meta to add/override anything we need
        """
        model = TriggerService
        widgets = {
            'description':  
           TextInput(attrs={'placeholder':  
                            _('A description for your new service')}),
        }

    provider = forms.ModelChoiceField(queryset=TriggerType.objects.all())
    consummer = forms.ModelChoiceField(queryset=TriggerType.objects.all())
```

Voilà !

A présent voici ce qui se passait quand j'affichais mon formulaire :

Dans mes 2 listes déroulantes j'obtenais "TriggerType object" en quise
de valeur dans ces 2 listes.  
Comme j'ai eu du mal à trouver la solution finale, dans un premier
temps je me suis résigné à faire un tuple dans mon form :

```python
TRIGGER_TYPE = [(data.code, data.name) for data in TriggerType.objects.all()]
provider = forms.ChoiceField(label=_('Provider'),
                         widget=forms.Select, choices=TRIGGER_TYPE,
                         help_text=_('Select the service from which you want to grad your datas'))
consummer = forms.ChoiceField(label=_('Consummer'),
                          widget=forms.Select, choices=TRIGGER_TYPE,
                          help_text=_('Select the service to which you want to put your datas'))
```

ca marchait très bien mais comme je suis borné et avait repéré
[ModelChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#modelchoicefield)
je me suis dit "nan mais ho ModelChoiceField prend bien en argument le
nom d'un modèle alors CA DOIT le faire!"

En retournant donc sur la doc j'entrevois la lumière :

> The \_\_unicode\_\_ method of the model will be called to generate
> string representations of the objects for use in the field's choices;
> to provide customized representations,

Non de ieuD ! c'est aussi con que ça ?  
je retourne à mon modèle :  
**models.py**

```python
class TriggerType(models.Model):
    """
        TriggerType
    """
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=140)

    def __unicode__(self):
        """
            required to build the drop down list
            otherwise will dislpay 
        """
        return "%s" % (self.name)
```

et là de retour dans ma page web, Alélouya tout est tout propre.

Content de moi, cette fois ci je pars pour saisir mes données et les
enregistrer.

**Chapitre Deux form.as\_p**  
Confiant je ponds un formulaire à la main avec la vue qui va bien et
avec le modèle ci dessus *TriggerService* et mon form
*TriggerServiceForm*

**add\_service.html**

```python
    
        {% trans 'Creation of a new service' %}
        
        {% csrf_token %}
        
            {% trans 'Provider' %}
            
            {{ form.provider }}
            
        
        
            {% trans 'Consummer' %}
            
            {{ form.consummer }}
            
        
        
            {% trans 'Description' %}
            
            {{ form.description }}
            
        
        
            
            {% trans "Create it" %}
        
        
     
```

et voici ma vue **views.py**

```python
@login_required
def save_service(request):
    """
        save a service
    """
    if request.method == 'POST':  # If the form has been submitted...
        service = TriggerService(user_id=request.user.id)
        form = TriggerServiceForm(request.POST, instance=service)

        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect('/trigger_added/')

    else:
        # unbound form (if any)
        form = TriggerServiceForm()
    # redirect to home of the existing enabled services
    return redirect('home')
```

Et là quand je soumets mon formulaire je repars d'où je viens, la page
d'accueil (ici "home") sans que rien n'ai été ajouté dans ma base.

Parti la fleur au fusil j'ai carrément été trop vite.  
Oui et le lecteur attentif dira "ben oui tu gères pas le cas où le
formulaire n'est pas valide du coup on n'a pas les raisons du pourquoi
ca passe pas"

Exact ! So Let's go :

```python
@login_required
def save_service(request):
    """
        save a service
    """
    if request.method == 'POST':  # If the form has been submitted...
        service = TriggerService(user_id=request.user.id)
        form = TriggerServiceForm(request.POST, instance=service)
        # 1) valid the form
        if form.is_valid():  # All validation rules pass
            form.save()
            # 2) redirect user
            return HttpResponseRedirect('/trigger_added/')
        # 3) if not valid
        else:
            template_name = 'add_service.html'
            # 4) keep the data put in the form
            context = {'form': form }
            context.update(csrf(request))
            # 5) go back to the form and display the values + errors
            return render_to_response(template_name,
                                      context,
                                      context_instance=RequestContext(request))
    # attempt to acces to save_service by another method than POST
    else:
        # unbound form (if any)
        form = TriggerServiceForm()
    # redirect to home of the existing enabled services
    return redirect('home')
```

Là, ma vue m'a l'air cool mais encore une fois je me retrouve sur le
formulaire de saisie à tourner en boucle sans avoir les erreurs ...  
Après un peu de creusage de neuronne (oui j'en ai qu'un, surtout à
cette heure là :P) je farfouille dans les sources de django-registration
:D et retombe sur la propriété errors de chacun des champs.  
Je modifie tout ca et fini par produire le template suivant :  
**add\_service.html**

```python
    
        {% trans 'Creation of a new service' %}
        
        {% csrf_token %}
        {{ form.non_field_errors }}
        
            {% trans 'Provider' %}
            
            {{ form.provider.errors }}
            {{ form.provider }}
            
        
        
            {% trans 'Consummer' %}
            
            {{ form.consummer.errors }}
            {{ form.consummer }}
            
        
        
            {% trans 'Description' %}
            
            {{ form.description.errors }}
            {{ form.description }}
            
        
        
            
            {% trans "Create it" %}
        
        
     
```

Là tranquillement j'enregistre mon formulaire confiant (oui toujours ;)
mais déchante aussitôt !  
Je boucle toujours !!!

\*Groumpf\*

[Je retourne à la doc et je retrouve une
balise](https://docs.djangoproject.com/en/dev/topics/forms/#displaying-a-form-using-a-template "displaying a form using a template")
**form.as\_p** qui permet d'afficher son formulaire sans rien faire
d'autre ;)  
je m'empresse de l'ajouter après **{% csrf\_token %}** et recharge ma
page et là Ô surprise, je m'aperçois que j'ai oublié tout bêtement 2
éléments de mon modèle qui sont à présent dans mon formulaire qui sont :
user et date\_create ce qui fait que mon form.is\_valid() ne passait pas
une seule fois.

Donc j'ajoute à ma classe **Meta** de ma classe **TriggerServiceForm**
:  
**forms.py**

```python
        exclude = ('user',
                   'date_created')
```

et une option à mon modèle pour ajouter une date automatiquement à
chaque enregistrement des données du modèle

**models.py**

```python
class TriggerService(models.Model):
    """
        TriggerService
    """
...
   date_created = models.DateField(auto_now_add=True)
```

et hop hop hop tout roule comme sur des roulettes.

C'est pas trop tôt !

