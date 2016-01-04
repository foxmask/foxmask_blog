Title: Django, Le Magic System T'y Es Fou ! 
Date: 2014-09-23 11:00
Author: foxmask
Category: Techno
Tags: Django, python
Slug: django-le-magic-system-ty-es-fou
Status: published

Voici viendu la billet django de la rentrée, zenfin !

Comme on n'en fini jamais de faire le tour de django, après avoir poussé
jusqu'au bout du bout [la gestion des
forms](/post/2013/10/16/django-formwizard-dynamique-encore-plus-loin/ "Django FormWizard Dynamique, encore plus loin"),
me voici parti sur une nouvelle aventure, celle de la [Management
Commands](https://docs.djangoproject.com/en/1.7/howto/custom-management-commands/).

Dans la suite nous verrons comment, avant de tomber sur ces "Management
Commands", je m'y prenais (pas parfaitement) pour packager des batches
avec mes applications, puis nous verrons ensuite comment on produit un
batch à la sauce Django, sans effort.

**Avant** : Pas de Magie, juste un truc qui marche, mais archaïque &
rigide.

Le batch se nomme "**fire.py**" et fait 100 lignes à tout casser.

*Comment est-il lancé ?*

1.  Ce script est appelé depuis un virtualenv.
2.  j'ai besoin que python trouve le settings.py de mon appli d'où

    ```python
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_th.settings")
    ```

3.  et pour les besoins de la v 1.7 de Django il m'a fallu rajouter

    </p>
    ```python
    import django
    django.setup()
    ```

Ce qui donne

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import datetime
import time
import arrow

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_th.settings")
import django
django.setup()
from django.conf import settings
from django_th.services import default_provider
from django_th.models import TriggerService
from django.utils.log import getLogger

# create logger
logger = getLogger('django_th.trigger_happy')


def go():
    """
        run the main process
    """
    trigger = TriggerService.objects.filter(status=True)
    if trigger:
        for service in trigger:
            # flag to know if we have to update
            to_update = False
            # flag to get the status of a service
            status = False
            # counting the new data to store to display them in the log
            count_new_data = 0
            # provider - the service that offer datas
            service_name = str(service.provider.name.name)
            service_provider = default_provider.get_service(service_name)

            # consumer - the service which uses the data
            service_name = str(service.consumer.name.name)
            service_consumer = default_provider.get_service(service_name)

            # check if the service has already been triggered
            if service.date_triggered is None:
                logger.debug("first run for %s => %s " % (str(
                    service.provider.name), str(service.consumer.name.name)))
                to_update = True
            # run run run
            else:
                # 1) get the datas from the provider service
                # get a timestamp of the last triggered of the service
                datas = getattr(service_provider, 'process_data')(
                    service.provider.token, service.id, service.date_triggered)
                #consumer = getattr(service_consumer, 'save_data')

                published = ''
                which_date = ''

                # flag to know if we can push data to the consumer
                proceed = False

                # 2) for each one
                for data in datas:
                    # if in a pool of data once of them does not have
                    # a date, will take the previous date for this one
                    # if it's the first one, set it to 00:00:00

                    # let's try to determine the date contained in the data...
                    published = to_datetime(data)
                    if published is not None:
                        # get the published date of the provider
                        published = arrow.get(
                            str(published), 'YYYY-MM-DD HH:mm:ss').to(settings.TIME_ZONE)
                        # store the date for the next loop
                        # if published became 'None'
                        which_date = published
                    #... otherwise set it to 00:00:00 of the current date
                    if which_date == '':
                        # current date
                        which_date = arrow.utcnow().replace(
                            hour=0, minute=0, second=0)
                        published = which_date
                    if published is None and which_date != '':
                        published = which_date
                    # 3) check if the previous trigger is older than the
                    # date of the data we retreived
                    # if yes , process the consumer

                    # add the TIME_ZONE settings
                    date_triggered = arrow.get(
                        str(service.date_triggered), 'YYYY-MM-DD HH:mm:ss').to(settings.TIME_ZONE)

                    # if the published date if greater or equal to the last
                    # triggered event ... :
                    if date_triggered is not None and published is not None and published.date() >= date_triggered.date():
                        # if date are the same ...
                        if published.date() == date_triggered.date():
                            # ... compare time and proceed if needed
                            if published.time() >= date_triggered.time():
                                proceed = True
                        # not same date so proceed !
                        else:
                            proceed = True

                        if proceed:
                            if 'title' in data:
                                logger.info("date {} >= date triggered {} title {}".format(
                                    published, date_triggered, data['title']))
                            else:
                                logger.info(
                                    "date {} >= date triggered {} ".format(published, date_triggered))

                            #status = consumer(
                            #    service.consumer.token, service.id, **data)

                            to_update = True
                            count_new_data += 1
                    # otherwise do nothing
                    else:
                        if 'title' in data:
                            logger.debug(
                                "data outdated skiped : [{}] {}".format(published, data['title']))
                        else:
                            logger.debug(
                                "data outdated skiped : [{}] ".format(published))

            # update the date of the trigger at the end of the loop
            sentance = "user: {} - provider: {} - consumer: {} - {}"
            if to_update:
                if status:
                    logger.info((sentance + " new data").format(
                        service.user,
                        service.provider.name.name,
                        service.consumer.name.name,
                        service.description,
                        count_new_data))
                    update_trigger(service)
                else:
                    logger.info((sentance + " AN ERROR OCCURS ").format(
                        service.user,
                        service.provider.name.name,
                        service.consumer.name.name,
                        service.description))
            else:
                logger.info((sentance + " nothing new").format(
                    service.user,
                    service.provider.name.name,
                    service.consumer.name.name,
                    service.description))
    else:
        print("No trigger set by any user")


def update_trigger(service):
    """
        update the date when occurs the trigger
    """
    now = arrow.utcnow().to(settings.TIME_ZONE).format('YYYY-MM-DD HH:mm:ss')
    TriggerService.objects.filter(id=service.id).update(date_triggered=now)


def to_datetime(data):
    """
        convert Datetime 9-tuple to the date and time format
        feedparser provides this 9-tuple
    """
    my_date_time = None

    if 'published_parsed' in data:
        my_date_time = datetime.datetime.fromtimestamp(
            time.mktime(data.published_parsed))
    elif 'updated_parsed' in data:
        my_date_time = datetime.datetime.fromtimestamp(
            time.mktime(data.updated_parsed))
    elif 'my_date' in data:
        my_date_time = arrow.get(str(data['my_date']), 'YYYY-MM-DD HH:mm:ss')

    return my_date_time


def main():
    default_provider.load_services()
    # let's go
    go()

if __name__ == "__main__":

    main()
```

*Avantage(s)*  
La commande à taper est un simple ./fire.py dès lors que le fichiers
settings est trouvé par le script tout passe tout seul

*Inconvénient(s)*  
Le packaging est empirique, il faut rajouter au setup.py la prise en
compte de ce batch par :

```python
 entry_points={
 'console_scripts': [
 'trigger-happy = django_th.fire:go',
 ],
 }
```

afin que la commande soit disponible sous la main dès l'installation via
un

```python
pip install django_th
```

Point noir que tout le monde aura vu, le script appelle en dur le
fichier de settings de django\_th. Ce qui empêche une intégration
parfaite avec une autre application Django voisine déjà installée. Ou
alors il faut retoucher au batch une fois installer pour changer le nom
du settings à utiliser.

**Après** Le "Magic System" :  
Comme j'en ai eu marre de me coltiner le gros point noir au milieu de
la tronche, j'ai voulu trouvé Ze moyen de ne plus me prendre la tête
avec ce settings à définir dans mon batch. Et c'est à ce moment là que
j'ai croisé les Management Commands.  
Au début le terme et leur définition dans la doc m'a fait penser que
c'était dédié à la partie backend de l'appli. Mais en rererererelisant
attentivement, je me suis aperçu que ça collait parfaitement à mon
besoin, qui est de faire du traitement de données, autrement que via
l'interface web.

J'ai donc appliqué, au pied de la lettre, l'archi de la doc, pour donc
déplacer mon fire.py dans un sous-sous-dossier management/commands de
mon appli django\_th, sous le nom fire\_th.py

*Avantage(s):*

1.  Plus d'appel en dur d'un settings qui n'est pas celui de mon
    application courante.
2.  La commande est dispo de facto, dès lors que l'application est
    présente dans **INSTALLED\_APPS** dans le settings.py.
3.  pas de modification du setup.py nécessaire
4.  5.  Pour s'en assurer on tapera python manage.py help pour trouver
    la commande ;)

Ce script a donc été modifié en :

1.  supprimant l'appel du settings
2.  supprimant "def main" jusqu'à la fin du script
3.  remplaçant la fonction go() par handle() requise par BaseCommand
4.  déplaçant les 2 fonctions update\_trigger() et to\_datetime() au
    debut de la class Command
5.  remplaçant print() par self.stdout.write()

Ce qui donne :

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time
import arrow

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django_th.services import default_provider
from django_th.models import TriggerService
from django.utils.log import getLogger
# create logger
logger = getLogger('django_th.trigger_happy')


class Command(BaseCommand):

    help = 'Trigger all the services'

    def update_trigger(self, service):
        """
            update the date when occurs the trigger
        """
        now = arrow.utcnow().to(settings.TIME_ZONE).format('YYYY-MM-DD HH:mm:ss')
        TriggerService.objects.filter(id=service.id).update(date_triggered=now)

    def to_datetime(self, data):
        """
            convert Datetime 9-tuple to the date and time format
            feedparser provides this 9-tuple
        """
        my_date_time = None

        if 'published_parsed' in data:
            my_date_time = datetime.datetime.fromtimestamp(
                time.mktime(data.published_parsed))
        elif 'updated_parsed' in data:
            my_date_time = datetime.datetime.fromtimestamp(
                time.mktime(data.updated_parsed))
        elif 'my_date' in data:
            my_date_time = arrow.get(str(data['my_date']), 'YYYY-MM-DD HH:mm:ss')

        return my_date_time

    def handle(self, *args, **options):
        """
            run the main process
        """
        trigger = TriggerService.objects.filter(status=True)
        if trigger:
            for service in trigger:
                # flag to know if we have to update
                to_update = False
                # flag to get the status of a service
                status = False
                # counting the new data to store to display them in the log
                count_new_data = 0
                # provider - the service that offer datas
                service_name = str(service.provider.name.name)
                service_provider = default_provider.get_service(service_name)

                # consumer - the service which uses the data
                service_name = str(service.consumer.name.name)
                service_consumer = default_provider.get_service(service_name)

                # check if the service has already been triggered
                if service.date_triggered is None:
                    logger.debug("first run for %s => %s " % (str(
                        service.provider.name), str(service.consumer.name.name)))
                    to_update = True
                # run run run
                else:
                    # 1) get the datas from the provider service
                    # get a timestamp of the last triggered of the service
                    datas = getattr(service_provider, 'process_data')(
                        service.provider.token, service.id, service.date_triggered)
                    consumer = getattr(service_consumer, 'save_data')

                    published = ''
                    which_date = ''

                    # flag to know if we can push data to the consumer
                    proceed = False

                    # 2) for each one
                    for data in datas:
                        # if in a pool of data once of them does not have
                        # a date, will take the previous date for this one
                        # if it's the first one, set it to 00:00:00

                        # let's try to determine the date contained in the data...
                        published = self.to_datetime(data)
                        if published is not None:
                            # get the published date of the provider
                            published = arrow.get(
                                str(published), 'YYYY-MM-DD HH:mm:ss').to(settings.TIME_ZONE)
                            # store the date for the next loop
                            # if published became 'None'
                            which_date = published
                        #... otherwise set it to 00:00:00 of the current date
                        if which_date == '':
                            # current date
                            which_date = arrow.utcnow().replace(
                                hour=0, minute=0, second=0)
                            published = which_date
                        if published is None and which_date != '':
                            published = which_date
                        # 3) check if the previous trigger is older than the
                        # date of the data we retreived
                        # if yes , process the consumer

                        # add the TIME_ZONE settings
                        date_triggered = arrow.get(
                            str(service.date_triggered), 'YYYY-MM-DD HH:mm:ss').to(settings.TIME_ZONE)

                        # if the published date if greater or equal to the last
                        # triggered event ... :
                        if date_triggered is not None and published is not None and published.date() >= date_triggered.date():
                            # if date are the same ...
                            if published.date() == date_triggered.date():
                                # ... compare time and proceed if needed
                                if published.time() >= date_triggered.time():
                                    proceed = True
                            # not same date so proceed !
                            else:
                                proceed = True

                            if proceed:
                                if 'title' in data:
                                    logger.info("date {} >= date triggered {} title {}".format(
                                        published, date_triggered, data['title']))
                                else:
                                    logger.info(
                                        "date {} >= date triggered {} ".format(published, date_triggered))

                                status = consumer(
                                    service.consumer.token, service.id, **data)

                                to_update = True
                                count_new_data += 1
                        # otherwise do nothing
                        else:
                            if 'title' in data:
                                logger.debug(
                                    "data outdated skiped : [{}] {}".format(published, data['title']))
                            else:
                                logger.debug(
                                    "data outdated skiped : [{}] ".format(published))

                # update the date of the trigger at the end of the loop
                sentance = "user: {} - provider: {} - consumer: {} - {}"
                if to_update:
                    if status:
                        logger.info((sentance + " new data").format(
                            service.user,
                            service.provider.name.name,
                            service.consumer.name.name,
                            service.description,
                            count_new_data))
                        self.update_trigger(service)
                    else:
                        logger.info((sentance + " AN ERROR OCCURS ").format(
                            service.user,
                            service.provider.name.name,
                            service.consumer.name.name,
                            service.description))
                else:
                    logger.info((sentance + " nothing new").format(
                        service.user,
                        service.provider.name.name,
                        service.consumer.name.name,
                        service.description))
        else:
            self.stdout.write("No trigger set by any user")
```

Le script est plus long de (vraiment) quelques lignes, mais le jeu en
vaut la chandelle.

**Enfin :**  
Reste plus qu'à taper sa commande

```python
python manage.py fire_th
```

**And Just in case**  
Une fois que vous aurez fini votre script, pour le tester, si vous
tapez comme, votre serviteur, la commande

```python
./fire_th.py
```

depuis le dossier management/commands, vous aurez une surprise au
premier *import mon\_appli.whatelse* présent dans votre script, vous
indiquant que le module n'existe pas.  
Et effectivement, en se remettant les neurones à leur place, on se
rendra compte qu'on se devra de taper

```python
python manage.py fire_th
```

depuis le folder contenant manage.py :P

**Conclusion:**  
Une nouvelle fonctionnalité tout simple mais c'est de la simplicité que
s'exprime toute la puissance de la chose ;)

**Hey pssssssssssttttttttt :**  
Tous les commentaires sont les bienvenus.

