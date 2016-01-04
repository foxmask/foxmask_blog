Title: Quête  WampWS et Autobahn - épisode 1
Date: 2015-02-27 14:45
Author: foxmask
Category: Techno
Tags: autobahn, crossbar, python, TriggerHappy, wampws
Slug: quete-wampws-et-autobahn-episode-1
Status: published

**Une contré fort fort lointaine**

*L'était une fois ... des druides, des gueux, des recettes magiques et
un gentilhomme*

En chemin pour une contré fort fort lointaine, un gentilhomme (qu'on
appellera *DaveLooper*), passa par maintes tribulations et turpitudes
tantôt armé de son **lance pierres Perl**, tantôt de son **arbalète
PHP**, tantôt de son **épée Python**.

Il se fraya un chemin à travers bois parce que les grands routes n'avait
guère grâce à ses yeux.

C'est ainsi que grâce à son épée, il parvint à se tailler des outils,
tel TriggerHappy, un tireur toujours content, né à partir d'une
partition entonnée par un troubadour nommé Django, qui lui servirent à
se forger de nouvelles armes plus ou moins affûtées.

La dernière arme en date fut
[WampWS](http://wamp.ws/ "Web Application Protocol Messaging") un projet
foufoufou, qui fait rêver à l'arme absolue.  
Si vous voulez découvrir, en langage profane, ce qu'un gueux peut
attendre de ce projet, [ruez vous chez sam et
max](http://sametmax.com/presentation-de-wamp-round-2/)

Comme *DaveLooper* n'en est même pas à se forger le pommeau de cette
dernière, il est loin de l'extase, mais il aime ripailler, et partager,
du coup, il s'en va vous narrer comment il a déjà pu débuter ce morceau.

Le socle de base de cette nouvelle arme est encore TriggerHappy.

Il reste fidèle à son outil fétiche. - Il s'en va l'améliorer.

L'idée est donc de reprendre le MCD existant, et de bâtir autour, une
arme qui utiliserait le maillage de côte de
[crossbar](http://crossbar.io/ "Unified Application Router")/[WampWS](http://wamp.ws/ "Web Application Protocol Messaging")
via [autobahn](http://autobahn.ws/).

Pour ce faire *DaveLooper* a beaucoup échange de pigeons voyageur avec
le druide détenant la recette de wampws, et ce dernier lui fourni les
jarres qu'il jugeât les plus à même de remplir l'office.

Ces derniers sont :  
Polymer + autobahnJS \<=\> crossbar =\> autobahnjs + twisted +
txpostgres =\> postgresql.

Le choix évoqué par l'érudit se justifie par la scalabilité.

Ça fait un paquet de jattes à connaitre avant d'arriver à un résultat
honorable diriez vous à *DaveLooper*.

mais tout de même :

-   Crossbar s'installe aisément, reste à creuser la doc pour obtenir
    une configuration digne de nom.
-   Polymer+Autobahn sera l'étape suivante pour voir comment ça se
    goupille en récupérant les données de la base et en les affichant
    avec Polymer
-   Autobahn+twisted+txpostgres : c'est cet ensemble que *DaveLooper*
    s'en va vous décrire.

Il a préféré tâter le back-end avant le front au cas où le back-end
aurait été un désastre, le front aurait été oublié.

Donc, le principe est le suivant avec cette stack : crossbar oriente les
requêtes entre des composants applicatifs, et ceux ci se parlent en
temps réel et de façon asynchrone

En 2 lignes voilà crossbar prêt

```shell
crossbar init
```

à ne faire que la première fois que vous installez crossbar

```shell
crossbar start
```

pour chaque lancement de l'outil

Une fois fait, on peut à son tour démarrer les composants qui trépignent
à se faire des causeries.

[On en lance
un](https://github.com/tavendo/AutobahnPython/blob/master/examples/twisted/wamp/basic/pubsub/basic/frontend.py)
:

```shell
python frontend.py
session attached
Got event: 0
Got event: 1
Got event: 2
Got event: 3
Got event: 4
Got event: 5
disconnected
```

[puis
2](https://github.com/tavendo/AutobahnPython/blob/master/examples/twisted/wamp/basic/pubsub/basic/backend.py)
:

```shell
python backend.py
session attached
.
.
.
.
.
.
.
.
.
.
.
```

et hoooo ça se cause vindiou.

Simple efficace. What else ?  
Ben on se le demande ? allez on se le demande :D

Pour partir sur du plus concret et proche de ce que *DaveLooper* a mis
en branle avec l'heureux tireur "TriggerHappy", il se dit

> bien, quand le projet a démarré, seul Evernote causait avec des flux
> RSS. Repartons donc sur ces traces 'pour voir' ce que ces jarres
> recommandés par le druide peuvent réaliser

Le pattern utilisé sera donc publisher/subscriber. Où Evernote sera le
composant subscriber du composant RSS, le publisher.

Déroulement :

Pour obtenir les items des flux RSS, on récupère de la table qui les
contient d'abord les URL de ces flux, puis on parcourt les flux
eux-mêmes, et pour chaque item on "publish" le contenu de l'article au
subscriber.

Quand les données parviennent au composant subscriber, il n'a plus qu'à
les enregistrer.

On va donc voir ci dessous tout cette machinerie, puis [comment on
requête une base postgresql de façon
asynchrone](http://crossbar.io/docs/Database-Programming-with-PostgreSQL/).

**le backend, the RSS Component**

```python
# -*- coding: utf-8 -*-
import arrow
import sys

from components.lib.feedsservice import Feeds
from txpostgres import txpostgres
from twisted.internet.defer import inlineCallbacks, returnValue

from autobahn import wamp

from twisted.python import log
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession


class RssComponent(ApplicationSession):

    """
        An application component that publishes an event
    """

    @inlineCallbacks
    def onJoin(self, details):
        
        print("session attached")

        pool = txpostgres.ConnectionPool(None,
                                         port=5432,
                                         database='th',
                                         user='th',
                                         password='th')

        yield pool.start()
        print('DB Connection pool started')
        self.db = pool

        # register all procedures on this class which have been
        # decorated to register them for remoting
        regs = yield self.register(self)
        print('registered {} procedures'.format(len(regs)))

        while True:
            feeds = yield self.call('eu.trigger-happy.rss.feeds_url')
            for data in feeds:
                for item in data['data']:
                    print('publishing {}'.format(item))
                    self.publish(u'eu.trigger-happy.rss',
                                 {'trigger_id': data['trigger_id'], 'user_id': data['user_id'],'item': item})
            yield sleep(120)

    @wamp.register(u'eu.trigger-happy.rss.feeds_url')
    @inlineCallbacks
    def get_feeds_url(self):
        """
            get the URL stored in the database
        """
        query = "SELECT date_triggered, name, url, trigger_id, user_id FROM "
        query += "django_th_rss AS R, "
        query += "django_th_triggerservice AS TS "
        query += " WHERE R.trigger_id=TS.id "
        query += " AND TS.status = True "  #  get only the activated triggers
        query += " ORDER BY TS.date_triggered DESC "
        rows = yield self.db.runQuery(query)
        feeds = []
        print('get the feeds url...')
        for feed in rows:
            print('get feeds from {0} => {1}'.format(feed[1], feed[2]))
            if feed[0] <= self.right_now():
                feeds.append({'trigger_id': feed[3], "user_id": feed[4],
                          'data': Feeds(**{'url_to_parse': feed[2]}).datas()})
        returnValue(feeds)

    def right_now(self):
        """
            TODO import settings from a file or smth to get the TZ details
        :return:
        """
        return arrow.utcnow().replace(hour=0, minute=0, second=0).to('Europe/Paris')


if __name__ == '__main__':
    log.startLogging(sys.stdout)
    from autobahn.twisted.wamp import ApplicationRunner
    runner = ApplicationRunner(url="ws://127.0.0.1:8080/ws", realm="realm1")
    runner.run(RssComponent)
```

**le frontend - the Evernote Component**

```python
from __future__ import unicode_literals

import arrow
import sys
import json

# evernote API

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types
from evernote.edam.error.ttypes import EDAMUserException

# postgresql driver
from txpostgres import txpostgres

# autobahn
from autobahn import wamp
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks, returnValue

from autobahn.twisted.wamp import ApplicationSession

from sanitize import sanitize


class EvernoteComponent(ApplicationSession):

    """
        An application component that subscribes and receives events
    """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        pool = txpostgres.ConnectionPool(None,
                                         port=5432,
                                         database='th',
                                         user='th',
                                         password='th')

        yield pool.start()
        print('DB Connection pool started')
        self.db = pool

        # register all procedures on this class which have been
        # decorated to register them for remoting
        regs = yield self.register(self)
        print('registered {} procedures'.format(len(regs)))

        @inlineCallbacks
        def on_event(data):
            print (json.dumps(data, indent=4))
            yield self.call('eu.trigger-happy.evernote.save', data)

        try:
            yield self.subscribe(on_event, u'eu.trigger-happy.rss')
            print("subscribe topic")
        except Exception as e:
            print("could not subscribe to topic: {0}".format(e))

        #yield self.subscribe(on_event, u'eu.trigger-happy.pocket')
        #yield self.subscribe(on_event, u'eu.trigger-happy.twitter')


    def onDisconnect(self):
        print("disconnected")
        reactor.stop()

    @wamp.register(u'eu.trigger-happy.evernote.token')
    @inlineCallbacks
    def get_token(self, user_id):
        """
        get the token of the user that owns the trigger
        need to link the table with django_th_triggerservice to get the user id
        :param user_id:
        :return: a generator
        """
        query = "SELECT token FROM django_th_userservice "
        query += " WHERE name_id='ServiceEvernote' "
        query += " AND user_id={0}".format(user_id)
        rows = yield self.db.runQuery(query)
        for row in rows:
            token = row
        returnValue(token)

    @wamp.register(u'eu.trigger-happy.evernote.trigger')
    @inlineCallbacks
    def get_trigger(self, trigger_id):
        """
            get information for the current trigger
            such as notebook, tag, description

        :param trigger_id:
        :return: a generator
        """
        query = "SELECT notebook, tag, TS.description FROM django_th_evernote AS E, "
        query += " django_th_triggerservice AS TS "
        query += " WHERE E.trigger_id=TS.id  "
        query += " AND trigger_id='{0}'".format(trigger_id)
        print(query)
        rows = yield self.db.runQuery(query)
        for notebook,tag,description in rows:
            print(notebook, tag, description)
            data = {'notebook': notebook, 'tag': tag, 'description': description}
        returnValue(data)

    @wamp.register(u'eu.trigger-happy.evernote.save')
    @inlineCallbacks
    def save_data(self, stuff):
        """
            save the data coming from the subscribed service
        :param stuff: contain a table of : user_id, trigger_id, item (the main content)
        :return: nothing
        """
        user_id = stuff['user_id']
        trigger_id = stuff['trigger_id']
        token = yield self.call('eu.trigger-happy.evernote.token', user_id)
        token = token[0]
        content = ''
        status = False
        data = stuff['item']

    """
    .... ici .... 
    le long traitement pour exploiter les data et les envoyer sur son compte evernote
    """

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    from autobahn.twisted.wamp import ApplicationRunner
    runner = ApplicationRunner(url="ws://127.0.0.1:8080/ws",realm="realm1")
    runner.run(EvernoteComponent)
```

Donc on lance le subscriber puis le publisher et quand le RssComponent
trouve des éléments à publier il les envoie directement au
EvernoteComponent  
Tout cela se lit dans les consoles respectives instantanément.

Voici pour le coté "bout de code concret qui marche"

**Écueils** :  
Comme à chaque fois qu'on débute avec de nouveaux outils, on se tape
sur les doigts en se ratant/pensant enfoncer le clou.

Écueil 1 : erreur 111, la fameuse erreur 111...

```shell
$ python frontend.py 
Traceback (most recent call last):
  File "frontend.py", line 62, in 
    runner.run(Component)
  File "...ocal/lib/python2.7/site-packages/autobahn/twisted/wamp.py", line 199, in run
    raise connect_error.exception
twisted.internet.error.ConnectionRefusedError: Connection was refused by other side: 111: Connection refused.
```

ca veut dire que le composant ne parvient pas à contacter ... crossbar
...  
Ouais ouais ouais crossbar.  
Comme DaveLooper avait déjà vu cette erreur par le passé en des temps
reculés, il se dit comme à l'époque, "bon la base est pas joignable"  
Mais à tord

Donc 2 choses à checker : le port ouvert par crossbar dans
.crossbar/config.json

```json
        "transports": [
            {
               "type": "web",
               "endpoint": {
                  "type": "tcp",
                  "port": 8090
               },
               "paths": {
                  "/": {
                     "type": "static",
                     "directory": ".."
                  },
                  "ws": {
                     "type": "websocket"
                  }
               }
            }
         ]
```

et celui qu'on a défini dans le script :

```python
    runner = ApplicationRunner(url="ws://127.0.0.1:8090/ws",...)
```

s'ils sont identiques, alors crossbar n'est pas démarré

Écueil 2 : debug  
Il est trop trop souvent arrivé à *DaveLooper* de voir ses petites
cailloux, les print, retraçant le cheminement de l'enchainement des
étapes ... S'arrêter sans rien dire du tout.  
Aussi est il allé se rendre dans quelques échoppes quérir de l'aide sur
sans en trouver...

Et comme Sam pourrait encore le dire en rigolant :

> chaque fois que *DaveLooper* pose une question, il fini par trouver la
> réponse de lui même

Ba oui *DaveLooper* est borné et cherche toujours jusqu'à la solution
quand les réponses se font rares.

Donc il a fini par trouver ceci :

```python
    runner = ApplicationRunner(
                        url="ws://127.0.0.1:8090/ws",
                        realm="realm1",
                        debug=False, # low-level WebSocket debugging
                        debug_wamp=False,  # WAMP protocol-level debugging
                        debug_app=False)  # app-level debugging
```

Je vous dispenserai les logs, ils sont s'y verbeux qu'on croirait qu'on
compile le kernel linux ;)

Du coup quand les print s'arrêtent *DaveLooper* est content de savoir
enfin pourquoi.

Écueil 3 : leS elf ;)

Quand utiliser ces 4 là et comment.

```python
yield self.subscriber()
yield self.publish()
```

De ce que *DaveLooper* a pu tester, les 2 premiers yield sont assez
explicites d'eux même.

```python
yield self.call()
self.method()
```

Par contre pour savoir quand faire self.call ou sel.method c'est une
autre histoire.  
Le self.call coté publisher aura permis de récupérer les données pour
le subscriber  
Cote subscriber self.call ne convient pas pour sauvegarder les données.
Pourquoi ?  
Parce qu'il fallait "décorer" la methode déclenchée lors du subscribe,
ici on\_event()  
et donc rajouter yield devant.

Sinon, si on n'a pas besoin d'appels RPC, on utilisera self.method()

*DaveLooper*, n'utilisant ces jarres que depuis samedi dernier, a eu mal
à comprendre tout ça sans [des explications fournies sur
indexerror](http://indexerror.net/860/wamp-self-call-vs-self-publish-subscribe-vs-self-method)

**To be continued**  
Nous voici donc arrivé au terme de ce petit voyage, de *DaveLooper*
toujours en quête de nouveauté, où en même temps, très peu et beaucoup
de choses ont été abordées.

Dans les prochains épisodes, DaveLooper a en tête quelques sujets comme
:

-   démarrer un projet de zéro proprement, ou tout du moins prêt à
    l'emploi
-   la configuration de crossbar, pour alléger le code ci dessus et
    retirer les appels fait en dur à une base donnée par exemple
-   le "mode debug" de crossbar/wamp
-   wamplet

nota : si vous avez réperé des coquille(tte)s dans le code, faites en
part en commentaire, comme ca fait que 5jours que *DaveLooper* utilise
le tout Crossbar/wamp/autobahn, il y a forcement beaucoup à améliorer,
et ca sera fait avec les prochains billets ;)

