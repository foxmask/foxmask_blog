Title: Django FormWizard Dynamique
Date: 2013-10-07 16:54
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-formwizard-dynamique
Status: published

Intro
-----

Ce billet aura pour but d'illustrer une fonctionnalité de
[Django](https://docs.djangoproject.com/ "Django Framework") qu'est le
[FormWizard](https://docs.djangoproject.com/en/1.5/ref/contrib/formtools/form-wizard/ "Django FormWizard").

La particularité de ce dernier est qu'on ne se contente pas d'un
formulaire, mais qu'on veut en enchainer plusieurs comme par exemple
pour passer une commande sur un site de e-commerce.

Ça, ça se passe bien quand le scénario est figé dans le marbre et
qu'aucune déviance n'est possible, c'est à dire quand les étapes sont
connues d'avance.

Seulement arrive le moment où ce chemin tout tracé ne peut plus coller à
son besoin car les étapes qui suivent sont conditionnées par les étapes
courantes, comme dans la vie courante;)

Ainsi dans ce qui va suivre, je vais de nouveau aborder [Trigger
Happy](https://github.com/foxmask/django-th), ce petit projet, fait en
Django, permettant de grabber des info d'une source d'info de son choix
pour les envoyées vers un service tiers de son choix. Actuellement pour
rappel tout ce que le projet sait faire c'est récupérer des flux RSS et
envoyés ce qu'il a trouvé dans un carnet de note Evernote.

Le scénario était figé dans le marbre, il fallait bien commencé par un
embryon de bidule qui me permette d'éprouver la solution et
d'appréhender le framework ;) J'avais donc 3 pauvres pages :

-   une pour le nom du site qui fournissait l'url du flux RSS et le flux
    RSS itself ;)
-   une seconde pour indiquer dans quel carnet stocker le flux dans
    Evernote
-   et la dernière, une description du "trigger" pour être en mesure de
    le modifier à posteriori.

A présent que c'est fait, [suite à un
sondage](/post/2013/07/13/sondage-quels-services-utilisez-vous-le-plus/ "Sondage : quels services utilisez vous le plus ?"),
j'ai dû m'atteler à revoir le code, pour cette fois-ci le faire voler en
éclat et gérer le FormWizard, dynamiquement !

Mon scénario initial change de 2 pages de plus, mais restera à 5 pages
quoiqu'il arrive. Par ailleurs je connais 3 des 5 étapes d'avance :

-   choisir un service qui fourni l'information
-   (\*) nommer le service d'origine puis sélectionner l'information à
    utiliser
-   choisir un service qui stocke l'information
-   (\*)indiquer où stocker l'information dans le service choisi à
    l'étape précédente
-   donner une description au trigger

les informations statiques sont celles qui n'ont pas de (\*).

Ceci étant dit, ne vous attendez donc pas dans la suite de ce billet à
voir le code traiter d'une quantité de formulaires fluctuant à votre
gré. Non, là on restera à 5 pages, toutes obligatoires.

D'où je partais
---------------

voici en peu de lignes, le résumé du wizard statique "avant" que je ne
le remanie:

**views.py**

```python
from th_rss.forms import RssForm
from th_evernote.forms import EvernoteForm
from django_th.forms.base import ServicesDescriptionForm

FORMS = [("rss", RssForm),
         ("evernote", EvernoteForm),
         ("services", ServicesDescriptionForm), ]

TEMPLATES = {
    '0': 'rss/wz-rss-form.html',
    '1': 'evernote/wz-evernote-form.html',
    '2': 'services_wizard/wz-description.html'}


class UserServiceWizard(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        """
        Provides us with an instance of the Project Model to save on completion
        """
        if self.instance is None:
            self.instance = TriggerService()
        return self.instance

    def done(self, form_list, **kwargs):
        """
        Save info to the DB
        """

        trigger = self.instance
        trigger.provider = UserService.objects.get(
            name='ServiceRss',
            user=self.request.user)
        trigger.consummer = UserService.objects.get(name='ServiceEvernote',
                                                    user=self.request.user)
        trigger.user = self.request.user
        trigger.status = True
        # save the trigger
        trigger.save()
        #...then create the related services from the wizard
        for form in form_list:
            if form.cleaned_data['my_form_is'] == 'rss':
                from th_rss.models import Rss
                Rss.objects.create(
                    name=form.cleaned_data['name'],
                    url=form.cleaned_data['url'],
                    status=1,
                    trigger=trigger)
            if form.cleaned_data['my_form_is'] == 'evernote':
                from th_evernote.models import Evernote
                Evernote.objects.create(
                    tag=form.cleaned_data['tag'],
                    notebook=form.cleaned_data['notebook'],
                    status=1,
                    trigger=trigger)

        return HttpResponseRedirect('/')
```

Comme on le voit ici, tout est purement statique, ça marche pour ce que
ça fait mais il n'est pas du tout possible d'étendre les fonctionnalités
de l'application en pluggant un pauvre module de plus.

Où je suis parti
----------------

Ce qui suit m'a permit de modifier le FormWizard à la volée en
interceptant les données saisies dans la page de choix des services.  
**urls.py**  
tout d'abord j'ai mis les formulaires de mon wizard dans urls.py comme
ceci:

```python
    url(r'^service/create/$',
        UserServiceWizard.as_view([ProviderForm,
                                   DummyForm,
                                   ConsummerForm,
                                   DummyForm,
                                   ServicesDescriptionForm]),
```

si ca vous botte vous pouvez aussi la jouer comme ceci :

```python
    url(r'^service/create/$',
        UserServiceWizard.as_view('django_th.views.get_my_form_list'),
```

et définir une methode get\_my\_form\_list() dans votre views.py et
l'appeler dans l'\_\_init\_\_ de votre FormWizard.

Ici on notera que j'ai noté sciemment 2 fois DummyForm.  
L'intéret est tout con, quand le wizard se déroule il vous indique en
haut de chaque page:

-   etape 1/5
-   etape 2/5
-   etape 3/5
-   etape 4/5
-   etape 5/5

Donc si je ne mets pas des "faux" Form je vais avoir mon wizard qui
m'affichera 1/3,2/3,3/3,3/3,3/3, et ca sera le bordel dans le traitement
qui s'en suivra.

On notera aussi que je n'ai pas mis DummyForm 2 fois au pifomètre, non
!  
C'est à ces endroits que je les remplacerai par les form des services
choisis dans ProviderForm et ConsummerForm.

Voici à présent le FormWizard :  
**views.py**

```python
import importlib
def class_for_name(module_name, class_name):
   """
      import the class from the given module and class
   """ 
   m = importlib.import_module(module_name)
   c = getattr(m, class_name)
   return c

class UserServiceWizard(SessionWizardView):

    def __init__(self, **kwargs):
        self.form_list = kwargs.pop('form_list')
        return super(UserServiceWizard, self).__init__(**kwargs)

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = UserService()
        return self.instance

    def get_context_data(self, form, **kwargs):
        data = self.get_cleaned_data_for_step(self.get_prev_step(
                                                    self.steps.current))
        if self.steps.current == '1':
            service_name = str(data['provider']).split('Service')[1]
            #services are named th_
            #call of the dedicated ProviderForm
            form = class_for_name('th_' + service_name.lower() + '.forms',
                  service_name + 'ProviderForm')
       elif self.steps.current == '3':
            service_name = str(data['consummer']).split('Service')[1]
            #services are named th_
            #call of the dedicated ConsummerForm
            form = class_for_name('th_' + service_name.lower() + '.forms',
                  service_name + 'ConsummerForm')
        context = super(UserServiceWizard, self).get_context_data(form=form,
                                  **kwargs)
    return context
```

Ça marche super bien... j'ai bien écrasé le form DumyForm par celui que
me fourni le service que j'ai choisi dans la page précédente.  
C'est ce que récupere service\_name, puis j'appelle le form de mon
service via class\_for\_name.

Donc tout va bien... tant qu'on n'arrive pas à la méthode **done()** qui
gère elle, la validation de tous les formulaires saisis.  
Là j'ai eu beau me farcir (pendant des semaines de tests) toutes les
méthodes du FormWizard pour creuser dans laquelle je pouvais mettre la
"bonne liste" de Formulaire que je générai dynamiquement, rien y
faisait, **self.form\_list** restait immuable, impossible à changer...
sauf une, celle de la solution ...

The Right way to do it !
------------------------

A force de creuser pleins de solutions j'en suis arrivé à ne plus avoir
les idées claires pour un truc pourtant simplissime.  
J'ai donc demandé de l'aide via une barre chocolatée (aka un bounty)
sur StackOverFlow, ce qui m'a permit de trouver la voie !

Plutôt que tripatouiller *self.form\_list* du FormWizard puisqu'il était
tout le temps remis aux valeurs indiquées dans mon **urls.py**, il
fallait laisser choir **get\_context\_data()** pour le simplissime
**get\_form()** comme suit :

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
   #edition du billet le 16/10
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

c'est un peu verbeux et aurait pû être plus court pour tenir sur une
ligne mais en fait pep8 me faisait un caca nerveu alors j'ai alloué mes
vars *service\_name*, *class\_name*, *form\_name* tranquillou

Bon avec tout ça, là, on arrive au même point que ce que j'ai fait plus
haut avec le **get\_context\_data()**.  
Ici, le "plus" est que je récupère l'instance de ma classe avec les
données saisies du form ! (même si j'avais faire un form
class\_for\_name(...)(data) ca passait pas )

la méthode La Fée
-----------------

Reste ensuite à traiter toutes ces données dans la méthode **done()**.
La méthode done dans le FormWizard est la seule obligatoire à fournir
systématiquement. Toutes les autres ne sont pas nécessaire à son
fonctionnement, sauf celle ci qui si elle n'est pas définie pêtera une
erreur, recta. Et pour cause, c'est avec elle que vous vous chargerez de
vérifier la validité de vos données avant de les enregistrer.

La gymnastique ici, va consister à enregistrer les données sans
connaitre la moindre property des modèles correspondant aux services
sélectionnés.  
Enfin, quand je dis que je ne les connais pas, je ne les connais pas au
moment où je code. Je ne peux pas me permettre ici aussi, de hardcoder
le nom d'une seule d'entre elles, puisque tout est dynamique ici.

Comme dit plus tôt, je connais exactement 3 des 5 pages que je remplis,
donc je grabbe ces infos pour les stocker dans un premier modèle
**TriggerService**.  
Ensuite je grabbe les info saisies pour le formulaire que je nomme
"provider" puis celui de "consummer" et je donne à chacun de ces 2
modèles le lien vers le modèle **TriggerService** (c'est dans mon MCD
pour pouvoir revenir modifier mon trigger)

Now, follow me ;)

```python
import importlib
def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c

def get_service_model(what, data):
    """
        get the service name then load the model
    """
    service_name = str(data[what]).split('Service')[1]
    return class_for_name('th_' + service_name.lower() +
                          '.models', service_name)

def done(self, form_list, **kwargs):
    """
        Save info to the DB
        The process is :
        1) get the infos for the Trigger from step 0, 2, 4
        2) save it to TriggerService
        3) get the infos from the "Provider" and "Consummer" services
        at step 1 and 3
        4) save all of them
    """
    # get the datas from the form for TriggerService
    i = 0
    for form in form_list:
        # cleaning
        data = form.cleaned_data
        # get the service we selected at step 0 : provider
        if i == 0:
            trigger_provider = UserService.objects.get(
                name=data['provider'],
                user=self.request.user)
            model_provider = get_service_model('provider', data)
        # get the service we selected at step 2 : consummer
        elif i == 2:
            trigger_consummer = UserService.objects.get(
                name=data['consummer'],
                user=self.request.user)
            model_consummer = get_service_model('consummer', data)
        # get the description we gave for the trigger
        elif i == 4:
            trigger_description = data['description']
        i += 1

    # save the trigger
    trigger = TriggerService(
        provider=trigger_provider, consummer=trigger_consummer,
        user=self.request.user, status=True,
        description=trigger_description)
    trigger.save()

    model_fields = {}
    # get the datas from the form for Service related
    # save the related models to provider and consummer
    i = 0
    for form in form_list:
        model_fields = {}
        data = form.cleaned_data
        # get the data for the provider service
        if i == 1:
            for field in data:
                model_fields.update({field: data[field]})
            # additionnal properties
            model_fields.update({'trigger_id': trigger.id, 'status': True})
            model_provider.objects.create(**model_fields)
        # get the data for the consummer service
        elif i == 3:
            for field in data:
                model_fields.update({field: data[field]})
            # additionnal properties
            model_fields.update({'trigger_id': trigger.id, 'status': True})
            model_consummer.objects.create(**model_fields)
        i += 1

    return HttpResponseRedirect('/')
```

le début est surtout de la tambouille interne à mon workflow ; ce qui
import ici c'est l'usage de :

```python
model_provider.objects.create(**model_fields)
model_consummer.objects.create(**model_fields)
```

qui permet pour un modèle inconnu d'y stocker des properties via un
**kwargs** dont le contenu est tout aussi inconnu, mais valide !

Voilà ; le code peut allègrement être amélioré sans aucun doute ;)

Conclusion:
-----------

Ainsi, comme on peut le voir à présent, il n'y a aucune limite possible,
autre que de ne pas avoir accès à l'API d'un service tiers ;)  
Tout ce qui fourni de l'information et peut en stocker peut être
utiliser dans les 2 sens, que ca soit comme provider ou consummer.

A présent je vais pouvoir passer à pondre de nouveaux services comme
ceux indiqués dans le sondage :D  
J'aurai mis le temps mais le résultat en vaut la peine.

D'autres liens traitant du sujets
---------------------------------

Ci dessous, une liste de sujets sur le FormWizard par lesquels je suis
passé pour tenter de trouver mon bonheur qui pourraient quand même vous
servir, just in case :

-   [Dynamic number of step using Django
    Wizard](http://stackoverflow.com/questions/9777879/dynamic-number-of-steps-using-django-wizard/11455183#11455183)
-   [changer les formulaires de questionnaires à la
    volée](http://bpaste.net/show/l3CRJ6DMbp64qH3FISCO/)
-   <a href="http://stackoverflow.com/questions/3940138/how-to-pass-previous-form-data-to-the-constructor-of-a-dynamicform-in-formwizard?rq=1">How
    to pass previous form data to the constructor of a DynamicForm in
    FormWizard
-   [How do you dynamically create a formset based on previous
    step](http://stackoverflow.com/questions/8172398/django-formwizard-how-do-you-dynamically-create-a-formset-based-on-previous-st?rq=1)

**edit**  
J'adresse un petit merci pour l'écoute de chacun que j'ai pu
enquiquiner sur le sujet sur
[django-fr](irc://irc.freenode.net/django-fr) et les pistes fournies par
un certain Spoutnik ;)

