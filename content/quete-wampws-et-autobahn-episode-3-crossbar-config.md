Title: Quête WampWS et Autobahn - Episode 3 - Crossbar config
Date: 2015-05-12 11:00
Author: foxmask
Category: Techno
Tags: autobahn, crossbar, python, wampws
Slug: quete-wampws-et-autobahn-episode-3-crossbar-config
Status: published

Dans les épisodes précédants je vous ai montré qu'il était possible de
débuter un projet from scratch rapidement, et comment 2 composants se
parlaient.

Donc dans la continuité, de ces 2 épisodes, ici nous allons aborder
comment on configure crossbar, pour qu'il ait connaissance de nos
components, dès son démarrage.

Jusqu'à maintenant ([épisode
1](/post/2015/02/27/quete-wampws-et-autobahn-episode-1/))
on a pu voir que les composants pouvaient être démarrés indépendemment
et manuellement.

A présent on va voir comment on les démarre au boot de crossbar.

En intro à la "configuration" voici d'abord une version de l'épisode 1
"amélioré" qui va vous introduire des notions que l'on reportera dans la
config de crossbar ensuite.

dans chacun des 2 composants on avait :

```python
    def onJoin(self, details):
        pool = txpostgres.ConnectionPool(None,
                                         port=5432,
                                         database='th',
                                         user='th',
                                         password='th')
 
        yield pool.start()
        print('DB Connection pool started')
        self.db = pool
```

Or, mettre en dur des info de config dans le code, c'est sale.  
La version proprette donne plutôt ceci :

```python
    def onJoin(self, details):
        dbconfig = self.config.extra['database']
        self.db = txpostgres.Connection()
        try:
            yield self.db.connect(**dbconfig)
        except Exception as e:
           print("could not connect to database: {0}".format(e))
           self.leave()
           return
       else:
           print("PostgreSQL adapter connected to database")
[...]

if __name__ == '__main__':
    config = {
             'database': {
                 'port': 5432,
                 'database': 'foobar',
                 'user': 'foobar',
                 'password': 'foobar'},
             'TIME_ZONE': 'America/Chicago',
             }

    log.startLogging(sys.stdout)
    from autobahn.twisted.wamp import ApplicationRunner
    runner = ApplicationRunner(
                        url="ws://127.0.0.1:8080/ws",
                        realm="realm1",
                        extra=config)  # app-level debugging
    runner.run(RssComponent)
```

Et voilou.

Dans le détails cela donne :

dans le `onJoin`, on récupère `self.config.extra` qui provient du parm
"extra" qu'on voit à la fin du code, qui est disponible grâce à
crossbar.

```python
def onJoin(self, details): 
   ...
   dbconfig = self.config.extra['database']
   ...
```

ensuite on passe `dbconfig` à la connexion

```python
yield self.db.connect(**dbconfig)
```

ce qui donne pour le compoent Rss de l'épisode 1

```python
# -*- coding: utf-8 -*-
import arrow
import sys
import time
from datetime import datetime

# postgresql driver
from txpostgres import txpostgres

# autobahn
from twisted.python import log
from autobahn import wamp
from twisted.internet.defer import inlineCallbacks, returnValue
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession

# th_rss lib
from lib.feedsservice import Feeds


class RssComponent(ApplicationSession):

    """
        An application component that publishes an event
    """

    @inlineCallbacks
    def onJoin(self, details):
        # registering
        print("RSS session attached")
        self.register(self)

        dbconfig = self.config.extra['database']

        self.db = txpostgres.Connection()
        try:
            yield self.db.connect(**dbconfig)
        except Exception as e:
            print("could not connect to database: {0}".format(e))
            self.leave()
            return
        else:
            print("[th_rss] PostgreSQL adapter connected to database")

        # publishing
        while True:
            feeds = yield self.call(u'eu.trigger-happy.rss.feeds_url')
            for data in feeds:
                for item in data['data']:
                    self.publish(u'eu.trigger-happy.pushit',
                                 {'trigger_id': data['trigger_id'],
                                  'user_id': data['user_id'],
                                  'item': item})
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
        query += " WHERE R.trigger_id=TS.id AND TS.id=1 "
        query += " AND TS.consumer_id = "

        # subquery to get only the RSS provider
        query += " (SELECT id FROM django_th_servicesactivated WHERE "
        query += "name = 'ServiceRss' AND status = True) "

        query += " AND TS.status = True "  # get only the activated triggers
        query += " ORDER BY TS.date_triggered DESC "
        rows = yield self.db.runQuery(query)

        feeds = []
        print('get the feeds url...')
        for feed in rows:
            print('get feeds from {0} => {1}'.format(feed[1], feed[2]))
            data_parms = {'url': feed[2], 'date_triggered': feed[0]}
            if feed[0] <= self.right_now():
                feeds.append({'trigger_id': feed[3],
                              'user_id': feed[4],
                              'data': self.reworked_feeds(**data_parms)})
        returnValue(feeds)

    def right_now(self):
        """
        :return:
        """
        return arrow.utcnow().replace(hour=0, minute=0, second=0).to(
            self.config.extra['TIME_ZONE'])

    def reworked_feeds(self, **parms):
        """
            get the feeds and "translate" the time.struct_time()
            from Feedparser to a classical timestamp
        """
        data = Feeds(**{'url_to_parse': parms['url']}).datas()
        what = None
        my_date_time = datetime.fromtimestamp(time.mktime(
            (1980, 1, 1, 0, 0, 0, 0, 1, 0))
        )
        published = datetime.now()
        for feed in data:
            date_triggered = arrow.get(str(parms['date_triggered']),
                                       'YYYY-MM-DD HH:mm:ss').to(
                                       self.config.extra['TIME_ZONE'])

            if 'published_parsed' in feed:
                what = 'published_parsed'
                published = feed['published_parsed']
                my_date_time = datetime.utcfromtimestamp(
                    time.mktime(feed['published_parsed']))
            elif 'updated_parsed' in feed:
                what = 'updated_parsed'
                published = feed['updated_parsed']
                my_date_time = datetime.utcfromtimestamp(
                    time.mktime(feed['updated_parsed']))

            if my_date_time >= date_triggered.naive:
                # this is this property that cant be serialize
                # so we have to translate it to a timestamp and
                # replace the actual value with the new one
                if what is not None:
                    feed[what] = time.mktime(published)
            else:
                # drop that old data
                data.pop()
        return data


if __name__ == '__main__':
    config = {
             'database': {
                 'port': 5432,
                 'database': 'foobar',
                 'user': 'foobar',
                 'password': 'foobar'},
             'TIME_ZONE': 'America/Chicago',
             }

    log.startLogging(sys.stdout)
    from autobahn.twisted.wamp import ApplicationRunner
    runner = ApplicationRunner(
                        url="ws://127.0.0.1:8080/ws",
                        realm="realm1",
                        extra=config)  # app-level debugging
    runner.run(RssComponent)
```

A présent, je peux exécuter mon script en ligne de commande, il
utilisera ce qui est défini après le `if __name__`.  
Par rapport à la version de l'épisode 1 ca ne change pas grand chose au
fait d'avoir mis en dur la conf dans le code, sauf, sauf que maintenant,
je peux plugger mon component à crossbar, et c'est la conf définie dans
crossbar qui prévaudra. Ce qui me permet du coup d'avoir toute liberté
pour exécuter mon composant dans son coin avec sa conf de test et
l'utiliser avec crossbar avec une conf de prod par exemple.

Voyons maintenant comment ca se goupille dans crossbar  
Dans l'épisode 2 on en était resté à une configuration définissant
l'accès à un simple composant Hello.

Voyons ce que ca donne avec mon composant en plus :

```json
{
   "controller": {},
   "workers": [
      {
         "type": "router",
         "realms": [
            {
               "name": "realm1",
               "roles": [
                  {
                     "name": "anonymous",
                     "permissions": [
                        {
                           "uri": "*",
                           "publish": true,
                           "subscribe": true,
                           "call": true,
                           "register": true
                        }
                     ]
                  }
               ]
            }
         ],
         "transports": [
            {
               "type": "web",
               "endpoint": {
                  "type": "tcp",
                  "port": 8080
               },
               "paths": {
                  "/": {
                     "type": "static",
                     "directory": "../web"
                  },
                  "ws": {
                     "type": "websocket"
                  }
               }
            }
         ]
      },
      {
         "type": "container",
         "options": {
            "pythonpath": [".."]
         },
         "components": [
            {
               "type": "class",
               "classname": "components.th_rss.back.RssComponent",
               "realm": "realm1",
               "transport": {
                  "type": "websocket",
                  "endpoint": {
                     "type": "tcp",
                     "host": "127.0.0.1",
                     "port": 8080
                  },
                  "url": "ws://127.0.0.1:8080/ws"
               },
               "extra": {
                  "database": {
                     "host": "127.0.0.1",
                     "port": 5432,
                     "database": "foobar",
                     "user": "foobar",
                     "password": "foobar"
                  }
               }               
            },
            {
               "type": "class",
               "classname": "components.th_evernote.front.EvernoteComponent",
               "realm": "realm1",
               "transport": {
                  "type": "websocket",
                  "endpoint": {
                     "type": "tcp",
                     "host": "127.0.0.1",
                     "port": 8080
                  },
                  "url": "ws://127.0.0.1:8080/ws"
               },
               "extra": {
                  "database": {
                     "host": "127.0.0.1",
                     "port": 5432,
                     "database": "foobar",
                     "user": "foobar",
                     "password": "foobar"
                  }
               }
            }
         ]
      }
   ]
}
```

avec cette configuration, dès le lancement de crossbar, il chargera les
2 composants qui demarreront respectivement le code se trouvant dans le
`onJoin`

la valeur de classname est à rallonge et est un classique chemin python.

Cette config crossbar tient compte d'un fait important :

mes composants sont dans le path de crossbar et donc sont en python 2.7  
ceci m'est révélé par le paramètre

```json
         "options": {
            "pythonpath": [".."]
         },
```

Par contre, ce n'est pas parceque Crossbar n'est pas en python 3, que
Autobahn|Python ne l'est pas, donc je peux tout à fait avoir des
composants python 3 ailleurs, et si je veux que crossbar me charge mes
composants, je lui fourni le path vers ceux ci comme suit (par exemple)
:

```json
         "options": {
            "pythonpath": ["..","/home/foxmask/Django-Virtualenv/wamp-th/wamp-th/"]
         },
```

et ça ne dérangera pas Crossbar pour un sou (au contraire:)

un goodies en plus, on peut nommer le process qui se charge de gerer mes
components, pour cela j'ajoute à mon parm "options", "title" comme suit
:

```json
         "options": {
            "title": "triggerhappy",
            "pythonpath": ["..","/home/foxmask/Django-Virtualenv/wamp-th/wamp-th/"]
         },
```

enfin on trouve bien évidement les mêmes noeuds "config/extras"
qu'indiqués dans le `if __name__` de chacun des composants pour définir
une base de données différente (si besoin).

Voici donc qui clos cet épisode 3. Je n'ai pas abordé toutes les options
cette fois ci, je vous avouerai que je vous livre ici ce que j'ai
découvert, qui est tout frais, mais je n'hésiterai pas à faire un billet
de plus sur les nouveautés que j'aurai pu exploiter.

L'épisode 4 sera sur le mode debug de crossbar

