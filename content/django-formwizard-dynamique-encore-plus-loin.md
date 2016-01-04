Title: Django FormWizard Dynamique, encore plus loin
Date: 2013-10-16 16:05
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-formwizard-dynamique-encore-plus-loin
Status: published

Le FormWizard encore plus loin
------------------------------

[Dans le billet
précédent](/post/2013/10/07/django-formwizard-dynamique/ "Django FormWizard Dynamique")
traitant en détail de comment afficher un formulaire en fonction d'un
choix fait dans un formulaire précédent, j'ai poussé le bouchon encore
plus loin.

En effet, dans mon workflow des 5 formulaires, les formulaires 1 et 3
listent les services disponibles. Or bien évidement, quand j'en ai pris
un sur le formulaire 1, inutile de le réafficher dans ma liste sur le
formulaire 3.

Ainsi donc le code suivant qui fonctionne, ne convient plus à ce
"nouveau" prérequis :

```python
def get_form(self, step=None, data=None, files=None):
    """
        change the form instance dynamically from the data we entered
        at the previous step
    """
    if step is None:
        step = self.steps.current

    if step == '1':
        # change the form
        prev_data = self.get_cleaned_data_for_step('0')
        service_name = str(prev_data['provider']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ProviderForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
    elif step == '3':
        # change the form
        prev_data = self.get_cleaned_data_for_step('2')
        service_name = str(prev_data['consummer']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ConsummerForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
    else:
        # get the default form
        form = super(UserServiceWizard, self).get_form(step, data, files)
    return form
```

Il faut intervenir lors de l'affichage du formulaire 3, correspondant au
"step2", ce qui donne :

```python
def get_form(self, step=None, data=None, files=None):
    """
        change the form instance dynamically from the data we entered
        at the previous step
    """
    if step is None:
        step = self.steps.current

    if step == '1':
        # change the form
        prev_data = self.get_cleaned_data_for_step('0')
        service_name = str(prev_data['provider']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ProviderForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
   elif step == '2': 
        # je veux recuperer les données du premier formulaire 
        data = self.get_cleaned_data_for_step('0')
        # initialisation du form avec la liste deroulante sans la valeur saisie au step 0
        form = ConsummerForm(initial={'provider': data['provider']})
    elif step == '3':
        # change the form
        prev_data = self.get_cleaned_data_for_step('2')
        service_name = str(prev_data['consummer']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ConsummerForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
    else:
        # get the default form
        form = super(UserServiceWizard, self).get_form(step, data, files)
    return form
```

et dans mon **forms.py** ca donne :

```python
from django import forms
from django_th.models import ServicesActivated
from django.utils.translation import ugettext as _


class ServiceChoiceForm(forms.Form):

    def activated_services(self, provider=None):
        """
        get the activated services added from the administrator
        """
        services = ServicesActivated.objects.filter(status=1)

        choices = []
        datas = ()

        if provider is not None:
            services = services.exclude(name__exact=provider)

        for class_name in services:
            datas = (class_name, class_name.name.rsplit('Service', 1)[1])
            choices.append(datas)

        return choices


class ProviderForm(ServiceChoiceForm):

    provider = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.fields['provider'].choices = self.activated_services()


class ConsummerForm(ServiceChoiceForm):

    consummer = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(ConsummerForm, self).__init__(*args, **kwargs)
        # get the list of service without the one selected in
        # the provider form
        self.fields['consummer'].choices = self.activated_services(
            self.initial['provider'])


class ServicesDescriptionForm(forms.Form):

    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':
                                      _('A description for your new service')})
    )


class DummyForm(forms.Form):
    pass
```

... et le Fail !
----------------

Ainsi au formulaire 1 (step 0) j'utilise **ProviderForm** qui récupère
tous les services activés.  
Au formulaire 3 (step 2) j'utilise **ConsummerForm** qui récupère tous
les services en excluant celui saisi dans le formulaire 1

C'est le but du bout de code suivante de ma **views.py** :

```python
   elif step == '2': 
        # je veux recuperer les données du premier formulaire 
        data = self.get_cleaned_data_for_step('0')
        # initialisation du form avec la liste deroulante "moins" la valeur saisi au step 0
        form = ConsummerForm(initial={'provider': data['provider']})
```

Tout ça est super et ... ne marche pas !

Nan nan nan ca marche pas !

Ca fait une boucle infinie ... A chaque submit du formulaire 3 je
retourne dessus quoique je fasse...

Pourtant c'est tout beau tout propre hein ?

Après avoir bien creusé 2jours ; enquiquiné StackOverflow (pour rien
puisque pas eu de réponse :) et \#django-fr @ freenode (merci magopian
pour PDB :) j'ai entrevu la lumière que je vous montre à présent :

And ze Winner iz
----------------

La solution est dans la views.py... pour changer ;)

```python
   elif step == '2': 
        step0_data = self.get_cleaned_data_for_step('0')
        form = ConsummerForm(
            data, initial={'provider': step0_data['provider']})
```

tadaaaa !!!

Qu'est-ce qui change ?

avant :

"data" contenait les données saisies du formulaire 0. Donc en validant
le formulaire, django pensait que j'avais à faire à ProviderForm (pour
schématiser) et me sortait en background une erreur "champ obligatoire"
sur le field provider au lieu consummer. (un vrai sac de noeuds à
débuger)

après :

je récupère les données du formulaire 0, non pas dans ma variable
"data", mais dans une autre variable "step0\_data", et évite de toucher
à "data" passée à get\_form() pour ensuite les refiler proprement à mon
form "ConsummerForm()" qui exclue les données non souhaitées et le tour
est joué.

voici la méthode complète de **get\_form** dans **views.py** :

```python
def get_form(self, step=None, data=None, files=None):
    """
        change the form instance dynamically from the data we entered
        at the previous step
    """
    if step is None:
        step = self.steps.current

    if step == '1':
        # change the form
        prev_data = self.get_cleaned_data_for_step('0')
        service_name = str(prev_data['provider']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ProviderForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
   elif step == '2': 
        step0_data = self.get_cleaned_data_for_step('0')
        form = ConsummerForm(
            data, initial={'provider': step0_data['provider']})
    elif step == '3':
        # change the form
        prev_data = self.get_cleaned_data_for_step('2')
        service_name = str(prev_data['consummer']).split('Service')[1]
        class_name = 'th_' + service_name.lower() + '.forms'
        form_name = service_name + 'ConsummerForm'
        form_class = class_for_name(class_name, form_name)
        form = form_class(data)
    else:
        # get the default form
        form = super(UserServiceWizard, self).get_form(step, data, files)
    return form
```

et cette fois ci tout glisse jusqu'au bout !

Cheminements menant à la solution
---------------------------------

Ce qui m'a mis la puce à l'oreille c'est en comparant le code des autres
"step" (1 et 3) avec le step2 :

```python
        form = form_class(data)
```

en effet ici j'appelle la class "form\_class" d'un formulaire lambda
tout en lui passant les données de la variable "data".

la différence avec le step2 c'est qu'en plus il me fallait fournir une
valeur initiale via **initial={}**. J'avais bien capté ce qu'il fallait
faire pour passer une valeur initiale mais m'étais troué en passant au
travers du passage de data au form **ConsummerForm()**

Vala qui clot un nouveau chapitre sur mes pérégrinations FormWizard ;)

