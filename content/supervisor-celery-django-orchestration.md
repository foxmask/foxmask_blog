Title: Supervisor Celery Django : Orchestration
Date: 2015-06-19 10:30
Author: foxmask
Category: Techno
Tags: Celery, Django, Supervisor
Slug: supervisor-celery-django-orchestration
Status: published

Dans ce billet je vais aborder un triplet que chacun connait surement et
a déjà dû le mettre en place, mais j'irai posé là, comme à mon habitude,
un retour d'xp qui m'est propre et pourrait servir à de nouveaux venus
sur [django](https://www.djangoproject.com/) et l'administration de nos
instances avec ce framework.

une intro vite fait sur ces outils tout de même au cas où je parlerai
chinois ;)

-   Celery  

    > est un système distribué simple, flexible et fiable pour traiter
    > de grandes quantités de messages, tout en fournissant des
    > opérations avec les outils nécessaires pour maintenir un tel
    > système.

-   Supervisor  

    > est un système client / serveur qui permet à ses utilisateurs de
    > surveiller et de contrôler un certain nombre de processus sur les
    > systèmes d'exploitation de type UNIX.

*Comme tout à chacun (d'entre nous) on cherche à maintenir nos
applications "en vie" en les faisant démarrer comme services et les
animées par des tâches (récursives ou non). C'est là le but de ces
outils !*

### [Celery](https://celery.readthedocs.org)

Donc pour démarrer on aura besoin dans son projet django de créer le
fichier suivant permettant tout simplement d'aller à la pêche aux tâches
des applications django indiquées dans le settings.INSTALLED\_APPS.

**celery.py**

```python
from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')

app = Celery('mon_projet')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

Ensuite on pourrait avoir besoin de tâches récurrentes qui doivent être
définies dans le settings de son projet (et pas dans celery.py comme je
l'ai cru en parcourant la doc celery)

**mon\_projet/settings.py**

```python
CELERYBEAT_SCHEDULE = {
    'add-every-hour-cache': {
        'task': 'mon_app.tasks.read_data',
        'schedule': crontab(minute='27,54'),
    },
    'add-every-hour-publish': {
        'task': 'mon_app.tasks.publish_data',
        'schedule': crontab(minute='59'),
    },
}
```

Bizarreries :

Ici j'étais parti pour écrire, telle une vraie crontab,

```python
CELERYBEAT_SCHEDULE = {
    'every-hour-put-in-cache': {
        'task': 'mon_app.tasks.read_data',
        'schedule': crontab(minute='*/27'),
    },
    'add-every-hour-publish': {
        'task': 'mon_app.tasks.publish_data',
        'schedule': crontab(minute='*/60'),
    },
}
```

Seulement au lancement du "beat" je me suis mangé une erreur sur le
contenu de `minute` qui doit être compris en 1 et 59... Or dans une
crontab je peux tout aussi bien écrire `*/360` sur le range "`minutes`"
si ca me chante :P  
Ensuite le `*/27` foire tout aussi bien. Le beat démarre à 27 minutes,
puis 54 minutes .... et 00 ...  
Même comportement avec `*/59` (à la place de \*/60), il démarre bien à
59 minutes .... puis à 00 ...

Enfin, ensuite voici un exemple de tâches qui pourrait être déclenchées
à intervalle régulier  
**mon\_app/tasks.py**

```python
from __future__ import unicode_literals
from __future__ import absolute_import

from celery import shared_task

@shared_task
def read_data():
        ....


@shared_task
def publish_data():
        ...
```

au lancement du beat (qui gère la crontab) on obtient donc :

```python
 $ celery -A th beat -l debug
celery beat v3.1.18 (Cipater) is starting.
__    -    ... __   -        _
Configuration ->
    . broker -> redis://localhost:6379/10
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%DEBUG
    . maxinterval -> now (0s)
[2015-06-18 21:32:50,117: DEBUG/MainProcess] Setting default socket timeout to 30
[2015-06-18 21:32:50,117: INFO/MainProcess] beat: Starting...
[2015-06-18 21:32:50,134: DEBUG/MainProcess] Current schedule:



[2015-06-18 21:32:50,134: DEBUG/MainProcess] beat: Ticking with max interval->5.00 minutes
[2015-06-18 21:32:50,169: DEBUG/MainProcess] beat: Waking up in 5.00 minutes.
```

le lancement du worker donne ceci à son tour

```python
$ celery -A th worker --autoscale=10,3 -l debug
[2015-06-18 21:36:40,087: DEBUG/MainProcess] | Worker: Preparing bootsteps.
[2015-06-18 21:36:40,094: DEBUG/MainProcess] | Worker: Building graph...
[2015-06-18 21:36:40,095: DEBUG/MainProcess] | Worker: New boot order: {Beat, Timer, Hub, Queues (intra), Pool, Autoscaler, StateDB, Autoreloader, Consumer}
[2015-06-18 21:36:40,116: DEBUG/MainProcess] | Consumer: Preparing bootsteps.
[2015-06-18 21:36:40,117: DEBUG/MainProcess] | Consumer: Building graph...
[2015-06-18 21:36:40,136: DEBUG/MainProcess] | Consumer: New boot order: {Connection, Agent, Events, Mingle, Gossip, Tasks, Control, Heart, event loop}
[2015-06-18 21:36:40,140: WARNING/MainProcess] /home/sites/trigger-happy.eu/local/lib/python2.7/site-packages/celery/apps/worker.py:161: CDeprecationWarning: 
Starting from version 3.2 Celery will refuse to accept pickle by default.
 
 -------------- celery@monserver v3.1.18 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-2.6.32-042stab106.4-x86_64-with-debian-8.1
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         th:0x7f85f6883b50
- ** ---------- .> transport:   redis://localhost:6379/10
- ** ---------- .> results:     disabled
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . celery.backend_cleanup
  . celery.chain
  . celery.chord
  . celery.chord_unlock
  . celery.chunks
  . celery.group
  . celery.map
  . celery.starmap
  . mon_app.tasks.publish_data
  . mon_app.tasks.put_in_cache
  . mon_app.tasks.read_data

[2015-06-18 21:36:40,165: DEBUG/MainProcess] | Worker: Starting Hub
[2015-06-18 21:36:40,165: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:40,165: DEBUG/MainProcess] | Worker: Starting Pool
[2015-06-18 21:36:40,177: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:40,178: DEBUG/MainProcess] | Worker: Starting Consumer
[2015-06-18 21:36:40,179: DEBUG/MainProcess] | Consumer: Starting Connection
[2015-06-18 21:36:40,206: INFO/MainProcess] Connected to redis://localhost:6379/10
[2015-06-18 21:36:40,206: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:40,207: DEBUG/MainProcess] | Consumer: Starting Events
[2015-06-18 21:36:40,238: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:40,238: DEBUG/MainProcess] | Consumer: Starting Mingle
[2015-06-18 21:36:40,238: INFO/MainProcess] mingle: searching for neighbors
[2015-06-18 21:36:41,246: INFO/MainProcess] mingle: all alone
[2015-06-18 21:36:41,247: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:41,247: DEBUG/MainProcess] | Consumer: Starting Gossip
[2015-06-18 21:36:41,251: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:41,251: DEBUG/MainProcess] | Consumer: Starting Tasks
[2015-06-18 21:36:41,258: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:41,258: DEBUG/MainProcess] | Consumer: Starting Control
[2015-06-18 21:36:41,261: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:41,261: DEBUG/MainProcess] | Consumer: Starting Heart
[2015-06-18 21:36:41,262: DEBUG/MainProcess] ^-- substep ok
[2015-06-18 21:36:41,262: DEBUG/MainProcess] | Consumer: Starting event loop
[2015-06-18 21:36:41,263: WARNING/MainProcess] celery@monserver ready.
[2015-06-18 21:36:41,263: DEBUG/MainProcess] | Worker: Hub.register Pool...
[2015-06-18 21:36:41,264: DEBUG/MainProcess] basic.qos: prefetch_count->8
```

si on est joueur comme moi, on peut rajouter au lancement du worker un
petit coup de `--autoscale=10,3`

```python
$ celery -A th worker --autoscale=10,3 -l info
```

ce qui fera qu'au démarrage du beat, il demarrera 3 workers d'un coup et
si les ressources systemes le permettent, pourra monter à 10 workers
d'un coup :)

J'ai testé, c'est très efficace.

Dans la liste des tasks de "mon\_app" on voit que j'ai pas, deux tasks
comme je l'ai montré, mais trois.  
En effet `read_data` lance `put_in_cache`, et c'est là que les 10
workers font la teuf parce que j'ai ecrit ce qui suit :

```python
@shared_task
def read_data():
    data = UnModele.objects.all()
    for stuff in data:
        put_in_cache.delay(stuff)
```

C'est une task (`read_data`) qui en enchaine d'autres

Ici, grosso modo ici je récupère tous les flux RSS de `UnModele` et pour
chaque flux j'enclenche la mise en cache en rafale puisque 10 workers
bossent pour moi.  
Pour finir l'histoire, du coup par la suite, `publish_data` recupere
les données dans le cache (un Redis bien évidement) et les envoie à
travers les services Twitter, Pocket, Evernote etc...  
Je vous laisse imaginer le gain de temps de traitement par rapport à un
traitement sans cache et en série.

### [Supervisor](http://supervisord.org/)

je n'aborderai pas ici toutes les possibilités de la bête mais juste
comment intégrer Supervisor à des projets Django  
voici à quoi ca ressemble dans le fichier
/etc/supervisor/conf.d/mon\_projet.conf

```python
[program:mon_projet_gunicorn]
user = foxmask                                                   ; User to run as
directory = /home/sites/mon-projet/mon_projet
command = /home/sites/mon-projet/bin/gunicorn_start             ; Command to start app
autostart = true
autorestart = true
redirect_stderr=true
stdout_logfile = /home/sites/mon-projet/logs/gunicorn-start.log ; Where to write log messages
stderr_logfile = /home/sites/mon-projet/logs/gunicorn-start-err.log ; Where to write log messages

[program:mon_projet_worker]
user = foxmask                                                        ; User to run as
directory=/home/sites/mon-projet/mon_projet
command=/home/sites/mon-projet/bin/celery -A th worker --autoscale=10,3 -l info
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/sites/mon-projet/logs/mon_projet-worker.log
stderr_logfile=/home/sites/mon-projet/logs/mon_projet-worker-err.log

[program:mon_projet_beat]
user = foxmask                                                        ; User to run as
directory=/home/sites/mon-projet/mon_projet
command=/home/sites/mon-projet/bin/celery -A th beat -l info
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/sites/mon-projet/logs/trigger-happy-beat.log
stderr_logfile=/home/sites/mon-projet/logs/trigger-happy-beat-err.log
```

-   `command` gere le lancement du process cible
-   `directory` est le dossier où on a mis le projet django
-   `autostart` et `autorestart` permettent de lancer automatiquement la
    `command` quand supervisor démarre comme par exemple au demarrage du
    serveur, quant à autorestart, il lance aussi `command` après un
    plantage ou un kill du process

pour Celery j'ai defini 2 `program` (un pour les workers un pour le
beat) afin de séparer les logs et les process plutot que de lancer
celery comme ceci :

```python
celery worker -B
```

Ce qui n'est pas recommandé par la doc de Celery.

un autre exemple de conf où j'ai utilisé supervisor : **sentry** :

```python
[program:sentry-web]
user = foxmask
directory=/home/sites/sentry/
command=/home/sites/sentry/bin/sentry --config=/home/sites/sentry/conf/sentry.conf.py start
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/sites/sentry/sentry.log
stderr_logfile=/home/sites/sentry/sentry-err.log

[program:sentry-worker]
user = foxmask
directory=/home/sites/sentry/
command=/home/sites/sentry/bin/sentry --config=/home/sites/sentry/conf/sentry.conf.py celery worker -B
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/sites/sentry/sentry.log
stderr_logfile=/home/sites/sentry/sentry-err.log
```

la façon de lancer le worker n'est pas recommandée mais utilise une
version de celery plus ancienne.

### Alternatives à Celery

Il existe bien d'autres alternatives à celery

On peut aussi s'orienter vers des systèmes de queueing alternatifs
listés ici <http://queues.io/>

<p>
Dont  
<lu>

<li>
[RQ: Simple job queues for Python](http://python-rq.org/)  
par l'[auteur](http://nvie.com/) du [fameux git
worklow](http://nvie.com/posts/a-successful-git-branching-model/)

</li>
<li>
[Voire carrément exploiter redis
directement](http://sametmax.com/redis-pourquoi-et-comment/)

</li>
</ul>
### Alternative à Supervisor

On trouve [Circus](https://circus.readthedocs.org/) mais je n'ai pas
réussi à le faire fonctionner (ca remonte à des mois)

