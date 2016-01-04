Title: Quête WampWS et Autobahn : Épisode 2 - démarrage en trombe
Date: 2015-05-07 22:29
Author: foxmask
Category: Techno
Tags: autobahn, crossbar, python, wampws
Slug: quete-wampws-et-autobahn-episode-2-demarrage-en-trombe
Status: published

Voici la suite de la quête WampWS et Autobahn [(relire l'épisode
1)](/post/2015/02/27/quete-wampws-et-autobahn-episode-1/),
dans cet épisode 2, une présentation permettant de démarrer, en deux
coups les gros, un projet crossbar pour **autobahn|python**

```python
foxmask@foxmask:~$ virtualenv crossbar
New python executable in crossbar/bin/python
Installing distribute.............................................................................................................................................................................................done.
Installing pip...............done.
foxmask@foxmask:~$ cd crossbar/
foxmask@foxmask:~/crossbar$ ls
bin  include  lib  local
foxmask@foxmask:~/crossbar$ source bin/activate
(crossbar)foxmask@foxmask:~/crossbar$ pip install crossbar
Downloading/unpacking crossbar
  Downloading crossbar-0.10.4.tar.gz (171Kb): 171Kb downloaded
  Running setup.py egg_info for package crossbar
[...]
```

résultat (non des moindres ;)

```python
(crossbar)foxmask@foxmask:~/crossbar$ pip freeze --local
Jinja2==2.7.3
MarkupSafe==0.23
PyTrie==0.2
PyYAML==3.11
Pygments==2.0.2
Twisted==15.1.0
autobahn==0.10.3
cffi==1.0.0b2
characteristic==14.3.0
crossbar==0.10.4
cryptography==0.8.2
distribute==0.6.24
enum34==1.0.4
mistune==0.5.1
netaddr==0.7.14
pyOpenSSL==0.15.1
pyasn1==0.1.7
pyasn1-modules==0.0.5
pycparser==2.12
requests==2.7.0
service-identity==14.0.0
shutilwhich==1.1.0
six==1.9.0
treq==15.0.0
txaio==1.0.0
zope.interface==4.1.2
```

à présent on demarre un projet comme on le ferait avec django-admin.py
de Django:

```python
(crossbar)foxmask@foxmask:~/crossbar$ crossbar init --template hello:python --app $PWD/letsgodancing
Crossbar.io application directory '/home/foxmask/crossbar/letsgodancing' created
Initializing application template 'hello:python' in directory '/home/foxmask/crossbar/letsgodancing'
Using template from '/home/foxmask/crossbar/local/lib/python2.7/site-packages/crossbar/templates/hello/python'
Creating directory /home/foxmask/crossbar/letsgodancing/hello
Creating directory /home/foxmask/crossbar/letsgodancing/.crossbar
Creating file      /home/foxmask/crossbar/letsgodancing/README.md
Creating file      /home/foxmask/crossbar/letsgodancing/setup.py
Creating file      /home/foxmask/crossbar/letsgodancing/MANIFEST.in
Creating directory /home/foxmask/crossbar/letsgodancing/hello/web
Creating file      /home/foxmask/crossbar/letsgodancing/hello/hello.py
Creating file      /home/foxmask/crossbar/letsgodancing/hello/__init__.py
Creating file      /home/foxmask/crossbar/letsgodancing/hello/web/index.html
Creating file      /home/foxmask/crossbar/letsgodancing/.crossbar/config.json
Application template initialized

To start your node, run 'crossbar start --cbdir /home/foxmask/crossbar/letsgodancing/.crossbar'
```

Et donc on n'a plus qu'à s'exécuter comme le suggère la dernière ligne
ci dessus

```python
(crossbar)foxmask@foxmask:~/crossbar$ crossbar start --cbdir /home/foxmask/crossbar/letsgodancing/.crossbar
2015-05-07 22:08:42+0200 [Controller   4481] Log opened.
2015-05-07 22:08:42+0200 [Controller   4481] ==================== Crossbar.io ====================
    
2015-05-07 22:08:42+0200 [Controller   4481] Crossbar.io 0.10.4 starting
2015-05-07 22:08:42+0200 [Controller   4481] Running on CPython using EPollReactor reactor
2015-05-07 22:08:42+0200 [Controller   4481] Starting from node directory /home/foxmask/crossbar/letsgodancing/.crossbar
2015-05-07 22:08:42+0200 [Controller   4481] Starting from local configuration '/home/foxmask/crossbar/letsgodancing/.crossbar/config.json'
2015-05-07 22:08:42+0200 [Controller   4481] Warning, could not set process title (setproctitle not installed)
2015-05-07 22:08:42+0200 [Controller   4481] Warning: process utilities not available
2015-05-07 22:08:42+0200 [Controller   4481] Router created for realm 'crossbar'
2015-05-07 22:08:42+0200 [Controller   4481] No WAMPlets detected in enviroment.
2015-05-07 22:08:42+0200 [Controller   4481] Starting Router with ID 'worker1' ..
2015-05-07 22:08:42+0200 [Controller   4481] Entering reactor event loop ...
2015-05-07 22:08:42+0200 [Router       4484] Log opened.
2015-05-07 22:08:42+0200 [Router       4484] Warning: could not set worker process title (setproctitle not installed)
2015-05-07 22:08:43+0200 [Router       4484] Running under CPython using EPollReactor reactor
2015-05-07 22:08:43+0200 [Router       4484] Entering event loop ..
2015-05-07 22:08:43+0200 [Router       4484] Warning: process utilities not available
2015-05-07 22:08:43+0200 [Controller   4481] Router with ID 'worker1' and PID 4484 started
2015-05-07 22:08:43+0200 [Controller   4481] Router 'worker1': PYTHONPATH extended
2015-05-07 22:08:43+0200 [Controller   4481] Router 'worker1': realm 'realm1' (named 'realm1') started
2015-05-07 22:08:43+0200 [Controller   4481] Router 'worker1': role 'role1' (named 'anonymous') started on realm 'realm1'
2015-05-07 22:08:43+0200 [Router       4484] Site starting on 8080
2015-05-07 22:08:43+0200 [Controller   4481] Router 'worker1': transport 'transport1' started
2015-05-07 22:08:43+0200 [Controller   4481] Starting Container with ID 'worker2' ..
2015-05-07 22:08:43+0200 [Container    4493] Log opened.
2015-05-07 22:08:43+0200 [Container    4493] Warning: could not set worker process title (setproctitle not installed)
2015-05-07 22:08:44+0200 [Container    4493] Running under CPython using EPollReactor reactor
2015-05-07 22:08:44+0200 [Container    4493] Entering event loop ..
2015-05-07 22:08:44+0200 [Container    4493] Warning: process utilities not available
2015-05-07 22:08:44+0200 [Controller   4481] Container with ID 'worker2' and PID 4493 started
2015-05-07 22:08:44+0200 [Controller   4481] Container 'worker2': PYTHONPATH extended
2015-05-07 22:08:44+0200 [Controller   4481] Container 'worker2': component 'component1' started
2015-05-07 22:08:44+0200 [Container    4493] subscribed to topic 'onhello': Subscription(id=400001378, is_active=True)
2015-05-07 22:08:44+0200 [Container    4493] procedure add2() registered: 
2015-05-07 22:08:44+0200 [Container    4493] published to 'oncounter' with counter 0
2015-05-07 22:08:45+0200 [Container    4493] published to 'oncounter' with counter 1
2015-05-07 22:08:46+0200 [Container    4493] published to 'oncounter' with counter 2
2015-05-07 22:08:47+0200 [Container    4493] published to 'oncounter' with counter 3
2015-05-07 22:08:48+0200 [Container    4493] published to 'oncounter' with counter 4
```

Petite explication de texte ici !  
On a démarré le "projet" sans voir une ligne de code: wtf ?

la ligne

```python
crossbar init --template hello:python
```

nous a produit, comme je le disais à la manière de django-admin.py, une
arbo "type", avec une appli toute simple

```python
(crossbar)foxmask@foxmask:~/crossbar$ ls -lR letsgodancing/
letsgodancing/:
total 16
drwxr-xr-x 3 foxmask foxmask 4096 mai    7 22:08 hello
-rw-r--r-- 1 foxmask foxmask   30 mai    7 22:07 MANIFEST.in
-rw-r--r-- 1 foxmask foxmask  136 mai    7 22:07 README.md
-rw-r--r-- 1 foxmask foxmask 1859 mai    7 22:07 setup.py

letsgodancing/hello:
total 20
-rw-r--r-- 1 foxmask foxmask 3205 mai    7 22:07 hello.py
-rw-r--r-- 1 foxmask foxmask 1913 mai    7 22:08 hello.pyc
-rw-r--r-- 1 foxmask foxmask 1569 mai    7 22:07 __init__.py
-rw-r--r-- 1 foxmask foxmask  141 mai    7 22:08 __init__.pyc
drwxr-xr-x 2 foxmask foxmask 4096 mai    7 22:07 web

letsgodancing/hello/web:
total 8
-rw-r--r-- 1 foxmask foxmask 5085 mai    7 22:07 index.html
```

dans `letsgodancing/hello/hello.py` on trouve notre application
**autobahn** qui comme on le voit à la fin des logs ci dessus, affiche
un compteur qui s'incrémente toutes les secondes :

```python
 
class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        # SUBSCRIBE to a topic and receive events
        #
        def onhello(msg):
            print("event for 'onhello' received: {}".format(msg))

        sub = yield self.subscribe(onhello, 'com.example.onhello')
        print("subscribed to topic 'onhello': {}".format(sub))

        # REGISTER a procedure for remote calling
        #
        def add2(x, y):
            print("add2() called with {} and {}".format(x, y))
            return x + y

        reg = yield self.register(add2, 'com.example.add2')
        print("procedure add2() registered: {}".format(reg))

        # PUBLISH and CALL every second .. forever
        #
        counter = 0
        while True:

            # PUBLISH an event
            #
            yield self.publish('com.example.oncounter', counter)
            print("published to 'oncounter' with counter {}".format(counter))
            counter += 1

            # CALL a remote procedure
            #
            try:
                res = yield self.call('com.example.mul2', counter, 3)
                print("mul2() called with result: {}".format(res))
            except ApplicationError as e:
                # ignore errors due to the frontend not yet having
                # registered the procedure we would like to call
                if e.error != 'wamp.error.no_such_procedure':
                    raise e

            yield sleep(1)
```

je ne vais pas vous faire peur tout de suite (krkrkrkrkr), juste vous la
faire courte.  
comment ce code est lancé par crossbar ?

lors du lancement de
`crossbar start --cbdir /home/foxmask/crossbar/letsgodancing/.crossbar`
crossbar lit le fichier config.json de ce dossier, `config.json` qui
contient la config de l'application `hello` ci dessus.

le voici :

```json
{
   "controller": {
   },
   "workers": [
      {
         "type": "router",
         "options": {
            "pythonpath": [".."]
         },
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
                     "directory": "../hello/web"
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
               "classname": "hello.hello.AppSession",
               "realm": "realm1",
               "transport": {
                  "type": "websocket",
                  "endpoint": {
                     "type": "tcp",
                     "host": "127.0.0.1",
                     "port": 8080
                  },
                  "url": "ws://127.0.0.1:8080/ws"
               }
            }
         ]
      }
   ]
}
```

Une fois crossbar démarré, l'application démarre sur `onJoin` et exécute
le tout (que je vous décrirai dans un prochain billet) pour arriver au
while true qui affiche le fameux compteur.

Ainsi paré on est fin prêt à broder pour attaquer de nouvelles
applications autobahn, aussi appelé "component".

Dans le prochain épisode je vous parlerai du fameux config.json où on
verra ce qu'on y mettre de plus et comment !

Si vous trépigner d'impatience ou avez des questions plus vaste (ou
carrément spécifique) [viendez me
rejoindre](http://indexerror.net/tag/autobahn) avec quelques centaines
d'autres ;)

