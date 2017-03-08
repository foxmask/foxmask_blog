Title: Trigger Happy comment pondre son propre module
Date: 2013-12-09 15:49
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: trigger-happy-comment-pondre-son-propre-module
Status: published

**Intro:**

Tout comme vous avez des outils pour produire vos sites avec des CMS ou
Blogs, Trigger Happy entre dans une nouvelle catégorie d'outils vous
permettant de gérer cette fois ci l'interconnexion de services internet,
en fonction d'évènements :

-   sur la toile
-   sur vos propres comptes "internet".

Exemples :

-   Quand une nouvelle est publiée sur un site web, je souhaite qu'elle
    soit stockée dans mon compte Evernote ou Pocket, publiée sur
    Twitter, son mur Facebook, etc...
-   Quand j'ajoute une note dans mon compte Evernote, je souhaite
    l'envoyer dans mon compte Pocket
-   Quand un tweet sur un sujet tombe, l'envoyer dans mon compte
    Pocket/Evernote/Whatever
-   etc...

Tout ceci est très largement inspiré du très bon service IFTTT
permettant ces échanges.

Ce qui va suivre va donc vous montrer (avec du code "oui-oui"), comment
(vous) "brancher" un service de plus avec Trigger Happy et (presque) ne
plus vous en préoccuper ;)

**Pré-requis:**  
Ce qu'il vous faut posséder en premier lieu pour produire votre module
Trigger-Happy :

-   Connaitre Django
-   un compte sur le service "cible" (c'est possible sans, mais c'est
    mieux avec, on va dire hein)
-   et ... de l'huile de coude (encore que ça ne soit pas la mer à boire
    après ce qui suit)

**Quick start:**  
si vous êtes pressé, le plus simple est encore de voir le README du
module [Trigger Happy :
Pocket](https://github.com/foxmask/django-th-pocket), de cloner le
module et de changer partout "pocket" par "montrucquidechireduponey"
partout ;)

**Architecturationesse:**  
Le service que vous produirez se compose comme un module python. Pour
bien visualiser les explications ci dessous je prendrai comme exemple
[django-th-pocket](https://github.com/foxmask/django-th-pocket/).

L'architecturationnesseeee en elle-même est identique à celle d'un
dossier d'un module django.

Exemple :

```python
th_pocket/:
forms.py
__init__.py
models.py
my_pocket.py

th_pocket/templates/pocketform:
wz-1-form.html
wz-3-form.html

th_pocket/templates/pocketprovider:
edit_provider.html
```

**En détails, fichier par fichier**  
Pas de panique c'est court !

**En premier le modèle : models.py**

```python
# -*- coding: utf-8 -*-

from django.db import models
from django_th.models.services import Services


class Pocket(Services):

    tag = models.CharField(max_length=80, blank=True)
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=80, blank=True)
    tweet_id = models.CharField(max_length=80, blank=True)
    trigger = models.ForeignKey('TriggerService')

    class Meta:
        app_label = 'django_th'
```

ici 2 impératifs,  
1) appeler le modèle service de Trigger Happy pour en hériter, soit :

```python
from django_th.models.services import Services


class Pocket(Services):
...
```

2\) pour la lisibilite de votre base mettre un app\_label cohérent, soit
:

```python
    class Meta:
        app_label = 'django_th'
```

**En second, le formulaire : forms.py**  
C'est un simple formulaire Django, un ModelForm banal, qui appellera le
modèle susmentionné

```python
# -*- coding: utf-8 -*-

from django import forms
from th_pocket.models import Pocket

class PocketForm(forms.ModelForm):

    """
    for to handle Pocket service
    """

    class Meta:
        model = Pocket
        fields = ('tag',)


class PocketProviderForm(PocketForm):
    pass


class PocketConsummerForm(PocketForm):
    pass
```

Ici en sus, on fournit 2 classes supplémentaires *PocketProviderForm* et
*PocketConsummerForm* pour permettre lors de la création d'un Trigger,
de disposer du formulaire de Pocket, soit quand on décide que Pocket est
la source de données (donc le Provider) soit la cible (le Consummer)

**les Templates**  
Ensuite arrive les templates situés dans
th\_pocket/templates/pocketform. Ceux ci sont curieusement nommé
wz-1-form.html et wz-3-form.html

Explications : Trigger Happy créé ses triggers avec un Wizard constitué
de 5 étapes.

Etape 1 je choisi le service source (wz-0-form.html)  
Etape 2 j'indique où sont les informations du service choisi étape 1
(wz-1-form.html)  
Etape 3 je choisi le service cible (wz-2-form.html)  
Etape 4 je saisie les infos de stockage du service choisi étape 3
(wz-3-form.html)  
Etape 5 je nomme mon Trigger ;) (wz-4-form.html)

Les 2 formulaires ici sont donc pour les étapes 2 et 4.  
Quasiment tous les services peuvent servir de source ou cible, d'où la
présence de ces 2 formulaires.  
Ainsi en utilisant comme source de données Evernote j'appellerai le
form th\_evernote/templates/evernoteform/wz-1-form.html puis pour Pocket
comme "cible" th\_pocket/templates/pocketform/wz-3-form.html.

Le dernier formulaire
th\_pocket/templates/pocketprovider/edit\_provider.html permet quant à
lui de modifier des informations relatives à Pocket pour le Trigger
voulu. Chaque service disposant de son propre template pour la même
fonction.

**la Glue**  
Tout ceci permet d'indiquer, via les formulaires du wizard, d'où vient
l'information et où je la stocke. Mais il manque le plus important, la
glue entre tout ceci. C'est là le le rôle du module **my\_pocket.py**

Avant d'éventuellement vous faire mal aux yeux, je vais vous écrire en
français dans le texte, le but du module :

Celui ci permet 3 choses :

1.  ) authentifier "son" Trigger Happy aupres de Pocket (via la methode
    auth)
2.  ) récupérer les données depuis son compte Pocket, en l'occurence,
    les URL qu'on y aura mises (via la méthode process\_data)
3.  ) enregistrer les données provenant d'un service 'Provider' (via la
    méthode save\_data)

```python
# -*- coding: utf-8 -*-

# django_th classes
from django_th.services.services import ServicesMgr
from django_th.models import UserService, ServicesActivated
# django classes
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.log import getLogger

# pocket API
import pocket
from pocket import Pocket

import datetime
import time
"""
handle process with pocket
put the following in settings.py

TH_POCKET = {
'consummer_key': 'abcdefghijklmnopqrstuvwxyz',
}

"""

logger = getLogger('django_th.trigger_happy')


class ServicePocket(ServicesMgr):

    def process_data(self, token, trigger_id, date_triggered):
        """
        get the data from the service
        """
        datas = list()
        # pocket uses a timestamp date format
        date_triggered = int(
            time.mktime(datetime.datetime.timetuple(date_triggered)))

        if token is not None:

            pocket_instance = pocket.Pocket(
                settings.TH_POCKET['consummer_key'], token)

            # get the data from the last time the trigger have been started
            # timestamp form
            pockets = pocket_instance.get(since=date_triggered)

            if len(pockets[0]['list']) > 0:
                for pocket in pockets[0]['list'].values():

                    datas.append({'tag': '',
                                  'link': pocket['resolved_url'],
                                  'title': pocket['resolved_title'],
                                  'tweet_id': 0})

        return datas

    def save_data(self, token, trigger_id, **data):
        """
        let's save the data
        """
        from th_pocket.models import Pocket

        if token and len(data['link']) > 0:
            # get the pocket data of this trigger
            trigger = Pocket.objects.get(trigger_id=trigger_id)

            pocket_instance = pocket.Pocket(
                settings.TH_POCKET['consummer_key'], token)

            title = ''
            title = (data['title'] if 'title' in data else '')

            item_id = pocket_instance.add(
                url=data['link'], title=title, tags=(trigger.tag.lower()))

            sentance = str('pocket {} created').format(data['link'])
            logger.debug(sentance)

        else:
            logger.critical(
                "no token provided for trigger ID %s and link %s", trigger_id,
                data['link'])

    def auth(self, request):
        """
        let's auth the user to the Service
        """
        callbackUrl = 'http://%s%s' % (
            request.get_host(), reverse('pocket_callback'))

        request_token = Pocket.get_request_token(
            consumer_key=settings.TH_POCKET['consummer_key'],
            redirect_uri=callbackUrl)

        # Save the request token information for later
        request.session['request_token'] = request_token

        # URL to redirect user to, to authorize your app
        auth_url = Pocket.get_auth_url(
            code=request_token, redirect_uri=callbackUrl)

        return auth_url

    def callback(self, request):
        """
        Called from the Service when the user accept to activate it
        """

        try:
            # finally we save the user auth token
            # As we already stored the object ServicesActivated
            # from the UserServiceCreateView now we update the same
            # object to the database so :
            # 1) we get the previous objet
            us = UserService.objects.get(
                user=request.user,
                name=ServicesActivated.objects.get(name='ServicePocket'))
            # 2) then get the token
            access_token = Pocket.get_access_token(
                consumer_key=settings.TH_POCKET['consummer_key'],
                code=request.session['request_token'])

            us.token = access_token
            # 3) and save everything
            us.save()
        except KeyError:
            return '/'

        return 'pocket/callback.html'
```

enfin comme on peut l'apercevoir dans le code, des appels à la
configuration du module ont lieu, voici donc à quoi elle ressemblerait
pour le module Trigger Happy Pocket:

**settings.py**

```python
TH_SERVICES = (
   ...
    'th_pocket.my_pocket.ServicePocket',
   ...
)
INSTALLED_APPS = (
   ....
    'th_pocket',
   ...
)

# votre clé perso fournie par le service POCKET 
TH_POCKET = {
    'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
}
```

Si vous ne connaissez pas IFTTT et/ou pour les plus courageux qui se
sont donnés la peine de lire jusque là et/ou les curieux de comprendre
comme la machinerie tourne :  
**Sous le capot : mais comment ça marche-t-il-tu-c'truc ?**  
Il y a 2 parties:

-   la première visible, vous permet de "brancher" vos services entre
    eux via un wizard de 5 pages et de voir quand tel ou tel service a
    fourni des nouvelles neuves ;)
-   la seconde est un batch qui tourne à intervalle régulier qui va
    s'occuper d'aller récupérer ses fameuses "nouvelles neuves" et les
    expédier là où vous l'avez décidé

Comment ce batch s'en sort, alors que je ne sais pas d'avance quels sont
les services existants ?  
Ceci est géré par le biais de la variable TH\_SERVICES, indiquant les
services que VOUS avez ajouté (tout comme vous mettez le nom de
l'application "django" dans INSTALLED\_APPS). Ensuite "Trigger Happy" va
utiliser cette variable pour vous permettre de vous en servir dans le
Wizard mentionné plus tôt. Ensuite le batch récupère ces services
activés par vos soins, et utilise les "Glues" de chaque service existant
my\_pocket, my\_evernote, etc, et joue son scénario !

Voilà ! A présent vous êtes devenu maitre de vos données persos !

