Title: Django Form sous ses plus beaux atours
Date: 2014-07-15 11:43
Author: foxmask
Category: Techno
Tags: Django, python
Slug: django-form-sous-ses-plus-beaux-atours
Status: published

Les forms django sont vraiment indéniablement très bien foutus.

Par contre si on aime l'aspect brute on est servie ;)

[![Django Forms sans habillage](/static/2014/07/form_sans_bt3.png)](/static/2014/07/form_sans_bt3.png)


La mouvance étant à ~~la fainéantise~~ Twitter Bootstrap3, je revêts les
plus beaux atours pour mes formulaires.

[![Django Forms "habillé" en prêt à porté (incomplet:P)](/static/2014/07/form_avec_bt3.png)](/static/2014/07/form_avec_bt3.png)


Pour l'exemple, voici une liste déroulante customisée  
Là je me la joue cool parce que pas de données d'une table liée à
rajouter :P

un bout du **forms.py**

```python
    breakfast_lunch_diner = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}))
```

Partout dans les forms on peut rajouter une classe qui sera gérée par
Bootstrap3 aisément comme par exemple rajouter un type email pour que
les mobiles switchent directement le clavier quand votre petit doigt
sélectionnera le champ de saisie "courriel".

```python
    customer_mail = forms.EmailField(widget=forms.TextInput(
        {'class': 'form-control', 'type': 'email'}))
```

Tout va bien dans le meilleurs des mondes tant que je n'ai pas à me
farcir l'habillage des listes déroulantes issues de tables liées par une
FK.

Là c'est une autre histoire... ou pas ;)

J'ai creusé la toile, cette inépuisable ressource, (merci les arraignées
;) à la recherche du truc qui ferait la différence. On m'avait suggeré
[form-crispy](http://django-crispy-forms.readthedocs.org/en/latest/) et
autre joyeuseté un peu too much pour le peu que j'avais à en tirer, et
la solution est viendu de
[StackOverFlow](http://stackoverflow.com/questions/21911873/django-add-css-class-to-input-field-in-admin)

Dans l'init du Form on rajoute tout simplement :

```python
    def __init__(self, *args, **kwargs):
        super(JeSuisSupperEnForm, self).__init__(*args, **kwargs)
        self.fields['mon_field_cette_fk'].widget.attrs['class'] = 'form-control'
```

Et hop roule ma poule  
[![Django Forms "habillé" par ce grand couturier qu'on appelle Bootstrap3](/static/2014/07/form_avec_bt3_complet.png)](/static/2014/07/form_avec_bt3_complet.png)

