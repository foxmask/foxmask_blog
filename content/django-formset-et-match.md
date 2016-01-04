Title: Django Jeu, FormSet et match
Date: 2014-07-01 11:00
Author: foxmask
Category: Techno
Tags: dj-diabetes, Django, python
Slug: django-formset-et-match
Status: published

Le
[FormSets](https://docs.djangoproject.com/en/1.5/topics/forms/formsets/)
kézako ? Une extension d'un formulaire standard, d'un
[Forms](https://docs.djangoproject.com/en/1.6/topics/forms/) quoi

Il a plusieurs buts :

1.  il permet d'afficher dans un formulaire "parent", les données dans
    un (ou plusieurs) formulaire(s) enfant
2.  il permet d'enregistrer les données enfants ajoutées, en même temps
    que les données parentes

Exemple concret : Des entêtes de facture et des lignes de facture,
peuvent être manipulées conjointement

Je vais illustrer le présent sujet avec un bout de code tiré tout droit
d'un [projet tout neuf dont j'ai parlé par
ici](/post/2014/06/29/gerer-son-diabete-il-y-a-une-appli-web-pour-ca/ "Gérer son Diabète, il y a une appli web pour ça").

L'exemple consistera à afficher un "Examen" et les "détails" qui l'ont
composé.

Dans un premier temps les *models* & formulaire *parent*
**Examinations** & **ExamensForm** seuls se composent :

du **models.py**

```python

class Examinations(models.Model):

    """
        Examinations
    """
    user = models.ForeignKey(User)
    examination_types = models.ForeignKey(ExaminationTypes)
    comments = models.TextField()
    date_examination = models.DateField()
    hour_examination = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
```

et du **forms.py** :

```python
class ExamsForm(forms.ModelForm):
    """
        Exams Form
    """
    # to " suit " the HTML textearea
    comments = forms.CharField(widget=forms.Textarea(
        {'class': 'form-control', 'rows': '3'}))
    date_examination = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    hour_examination = forms.TimeField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    def save(self, user=None):
        self.myobject = super(ExamsForm, self).save(commit=False)
        self.myobject.user = user
        self.myobject.save()

    class Meta:
        model = Examinations
        fields = ['examination_types', 'comments',
                  'date_examination', 'hour_examination']
        exclude = ('user',)
```

C'est un formulaire tout ce qu'il y a de plus classique qui sera
affiché, je vous dispense donc de la CBV pour le gérer.

S'ajoute alors les *models* & *formulaire* "enfant"
**ExaminationDetails** & **ExamDetailsForm** suivants :

**models.py** :

```python
class ExaminationDetails(models.Model):

    """
        ExaminationDetails
    """
    examination = models.ForeignKey(Examinations)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Examination Details'
        verbose_name_plural = 'Examination Details'

    def show(self):
        return "Examination Details %s %s %s %s %s" % (self.examination_id,
                                                       self.title,
                                                       self.value,
                                                       self.created,
                                                       self.modified)

    def __unicode__(self):
        return "%s" % (self.title)
```

Et son petit **forms.py** :

```python
class ExamDetailsForm(forms.ModelForm):
    """
     Details of Exams Form
    """
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    value = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = ExaminationDetails
        fields = ['title', 'value']
```

Encore une fois, rien de transcendant là dedans, c'est bateau.

[Coté doc, sur
formset](https://docs.djangoproject.com/en/1.6/topics/forms/formsets/),
django nous montre comment on produit des *formsets* d'un *form*
unique.  
Me voilà frais avec mes 2 *forms* distincts :P  
D'autant que pour corser le tout, j'utilise des ModelForms, pas de
simple Forms.

En creusant d'avantage, on trouve le sésame via
[django.forms.models.inlineformset\_factory](https://docs.djangoproject.com/en/1.6/ref/forms/models/#django.forms.models.inlineformset_factory)
qui traite de ModelForms.

Ce qui ceci donne dans mon **forms.py** :

```python
# a formset based on the model of the Parent and Child + 2 new empty extra lines
ExamDetailsFormSet = inlineformset_factory(Examinations, ExaminationDetails, extra=2)
```

Et oui mon bon monsieur, ma bonne dame, ca tient bien en UNE ligne.  
Ici j'indique à la factory inlineformset, les 2 *models* qui
m'interessent en commençant par le parent et continuant par l'enfant
(tout deux finalement liés par ma FK qu'on a vu dans le model plus haut)

A présent je dispose d'un **FormSet** avec Parent et Enfant.  
Toute la smala va se retrouver dans le même formulaire sous vos yeux
ébahis.

Maintenant que sont liés les *models* et que sont définis les *forms*,
coté **views.py** reste à exploiter le **ExamDetailsFormSet**.

Mais comme je suis "jusqueboutiste", je ne me contenterai pas d'une
simple fonction pour gérer celui-ci, j'utilise une **CreateView**, cette
[CBV](https://docs.djangoproject.com/en/dev/topics/class-based-views/ "Class Based View")
donne ceci (explications de texte plus bas):

```python
class ExamsCreateView(CreateView):
    """
        to Create Exams
    """
    form_class = ExamsForm
    template_name = "dj_diabetes/exams_form.html"

    def form_valid(self, form):
        if self.request.POST:
            formset = ExamDetailsFormSet(self.request.POST, instance=self.object)
            if formset.is_valid():
                self.object = form.save(user=self.request.user)
                formset.instance = self.object
                formset.save()

        else:
            formset = ExamDetailsFormSet(instance=self.object)

        return HttpResponseRedirect(reverse('exams'))

    def get_context_data(self, **kw):
        data = Examinations.objects.all().order_by('-created')
        #paginator vars
        record_per_page = 15
        page = self.request.GET.get('page')
        # paginator call
        data = page_it(data, record_per_page, page)

        context = super(ExamsCreateView, self).get_context_data(**kw)
        context['action'] = 'add_exam'
        context['data'] = data

        if self.request.POST:
            context['examsdetails_form'] = ExamDetailsFormSet(self.request.POST)
        else:
            context['examsdetails_form'] = ExamDetailsFormSet(instance=self.object)
        return context
```

dans le template on obtient enfin ceci (attention c'est verbeux, mais
zavez un snapshot plus bas ;) :

```python
{% extends "base.html" %}
{% load url from future %}
{% load i18n %}
{% block title %}{% trans "My Glucose Manager" %}{% endblock %}
{% block content %}
    
        
        
        {% csrf_token %}
        {{ form.non_field_errors }}
        
        {% if action = 'add_exam' %}
         {% trans "Exams" %}
        {% else %}
         {% trans 'Edition of the examination' %}
        {% endif %}
        
            
            
                {% if form.examination_types.errors %}
                {{ form.examination_types.errors }}
                {% endif %}
                {% trans "Type" %}
                
                {{ form.examination_types }}
                
            

            
                {% if form.comments.errors %}
                {{ form.comments.errors }}
                {% endif %}
                {% trans "Comments" %}
                
                  {{ form.comments }}
                
            

            
                {% if form.date_examination.errors %}
                {{ form.date_examination.errors }}
                {% endif %}
                {% trans "Date" %}
                
                  {{ form.date_examination }}
                
            

            
                {% if form.hour_examination.errors %}
                {{ form.hour_examination.errors }}
                {% endif %}
                {% trans "Hour" %}
                
                  {{ form.hour_examination }}
                
            
        
        
        
        
         {% trans "Examinations details" %}
            
            {{ examsdetails_form.management_form }}
            
            
                {% trans "Title" %}
                {% trans "Value" %}
            
            {% for form in examsdetails_form %}
            
                {{ form.id }}
                    
                        {% if form.title.errors %}
                        {{ form.title.errors }}
                        {% endif %}
                        
                          {{ form.title }}
                        
                    
                
                
                    
                        {% if form.value.errors %}
                        {{ form.value.errors }}
                        {% endif %}
                        
                          {{ form.value }}
                        
                    
                
                        
            {% endfor %}
            
            
           
        
            
                {% if action = 'add_exam' %}                
                {% trans "Add it" %}
                {% else %}
                {% trans "Edit it" %}
                {% endif %}
            
        
        
    
    
         {% trans "Last examinations" %}
        
            
                {% trans "Date" %}
                {% trans "Type" %}
                {% trans "Comments" %}
                {% trans "Actions" %}
            
        {% for line in data %}
            
                {{ line.date_examination }}
                {{ line.examination_types.title }}
                {{ line.comments }}
                 
            
        {% endfor %}
        
        
            
                {% if data.has_previous %}
                    {% trans "previous" %}
                {% endif %}
                    
                    {% blocktrans with page_number=data.number total_of_pages=data.paginator.num_pages %}
                    Page {{ page_number }} of {{ total_of_pages }}
                    {% endblocktrans %}
                    
                {% if data.has_next %}
                    {% trans "next" %}
                {% endif %}
            
                
    
{% endblock %}
{% block extrajs %}

//<![CDATA[
$(function(){
    $('#id_date_examination').datepicker({
            format: 'yyyy-mm-dd'
    });
});
//]]>

{% endblock %}
```

Explications de texte :

Le lecteur averti aura remarqué que ma CBV ne se contente pas que
d'afficher un formulaire, puisque dans le "context" (modifié dans la
methode get\_context\_data), j'ai rajouté la liste de tous les examens
(en les paginant par dessus le marché, je vous ai dit
"jusqueboutiste").  
La page contient donc un formulaire de saisie + la liste complète des
examens.

Tout cela donne ce rendu :

[![My Glucose Manager - Les Examens](/static/2014/06/glucose_manager_exams-1024x782.png)](/static/2014/06/glucose_manager_exams.png)

Voilà j'espère que le triplet **FormSet** de **ModelForm** et **CBV** ne
sera plus un secret pour vous ;)

Edit le 2/7 @ 10:30:  
[on](http://linovia.com/fr/) m'a gentiment suggéré un truc pour alléger
le code des forms.

Faire un *form(self.request.POST or None)*

ce qui transforme ceci

```python
    def form_valid(self, form):
        if self.request.POST:
            formset = ExamDetailsFormSet(self.request.POST, instance=self.object)
            if formset.is_valid():
                self.object = form.save(user=self.request.user)
                formset.instance = self.object
                formset.save()

        else:
            formset = ExamDetailsFormSet(instance=self.object)

        return HttpResponseRedirect(reverse('exams'))
```

en cela

```python
    def form_valid(self, form):
        formset = ExamDetailsFormSet((self.request.POST or None), instance=self.object)
        if formset.is_valid():
            self.object = form.save(user=self.request.user)
            formset.instance = self.object
            formset.save()

        return HttpResponseRedirect(reverse('exams'))
```

ca evite tous les tests sur *if self.request.POST* et instancie le form
une fois quelque soit le cas de figure.

