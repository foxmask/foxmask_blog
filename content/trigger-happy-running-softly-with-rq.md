Title: Trigger Happy running softly with RQ
Date: 2016-02-15 19:30
Author: foxmask
Category: Techno
Tags: Django, TriggerHappy
Slug: trigger-happy-running-softly-with-rq
Status: published


## TriggerHappy and Celery

Actually, Trigger Happy works perlfectly with [Celery](http://celery.readthedocs.org/), but.... there is a but.

Sometimes, (once a week) celery stays stuck without any visible reason. 

No error logs occur, and even in DEBUG level, no log appear at all. The logfile remain as is (and yes the disk is not full:)

As this is very annoying for me, I went on [#celery@freenode](irc://irc.freenode.net/celery) to try to get some details about this behavior, before breaking everything ...

Here, we told me that this behavior was also met with AMQ as broker (when I currently use REDIS).

## TriggerHappy and RQ

So I decide to give a try to [Python-RQ](http://python-rq.org)

His (well known) author presents it as follow :

> Python RQ (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers
> This project has been inspired by the good parts of Celery, 

So to integrate RQ with TriggerHappy here is what I should do :

1. I installed django-rq that I added to *INSTALLED_APPS* in the **settings.py** file.
2. to not break the existing way (with Celery) that (almost) works perfectly, I changed few details in the tasks.py module :


before 
```python
from celery import shared_task

@shared_task
def reading(service):
    [...]

@shared_task
def publishing(service):
    [...]

```
after 

```python
try:
    from django_rq import job
except ImportError:
    from celery import shared_task

[...]

@job('default')
@shared_task
def reading(service):
    [...]

@job('high')
@shared_task
def publishing(service):
    [...]

```

Those tasks are executed by celery with the decorator **@shared_task** (with its own scheduler) or by the RQ with the **@job** decorator, through some crontab tasks, with management commands. As RQ asole use my_tasks.delay(), I dont have to change anything else, other than just adding a @job decorator.

I perfectly know that it's not satifying because if Celery or RQ is not installed, the decorator call with fail and the tasks wont happen.
It's just for testing purpose :) That way, I'm able to compare performance between the two solutions, one weight and one very light.


Surprisingly, the weight win by handling my reading tasks in less than a seconde for ~50triggers against 30sec for the light one. For the publishing tasks, they are neck and neck. But one thing hangs in the balance actually against celery, it is out of order once a week. The process are not dead, the log does not move, the query I made with celery inspect and so on, respond perfectly.

As my project is not so overloaded I can say that the cursor between something a "little bit slow" and something "out of order" is quickly choosen :)


So at least if you want to give a try to [RQ](http://python-rq.org) with TriggerHappy, the stuff that will need to be handle, will continue to work.

Here I provide the line I enter in my crontab :

```shell
*/12 * * * * . /my/env/bin/activate && cd /my/env/th/ && ./manage.py fire_read_data && ../bin/rqworker-default-burst.sh
*/15 * * * * . /my/env/bin/activate && cd /my/env/th/ && ./manage.py fire_publish_data && ../bin/rqworker-high-burst.sh
*/20 * * * * . /my/env/bin/activate && cd /my/env/th/ && ./manage.py fire_get_outside_data && ../bin/rqworker-low-burst.sh
```

and the content of, for example, rqworker-default-burst.sh

```bash
#!/bin/bash
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst & 
python manage.py rqworker default --burst & 
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
python manage.py rqworker default --burst &
```
Yes I like to spawn a lot :)

## A Question to finish

I take the opportunity of this post to ask you a question :

If I want to support Celery and RQ for my tasks, one should I write a decorator that could handle each of them.
Is there a way to write a generic decorator that will permit to be inherited to handle each of them ?

Thus in my tasks.py I'll be able to just do 

```python

from django_th.my_powerful_decorator import jobth


[...]

@jobth
def reading():
   [...]
```

and **jobth** will check which of the two Queueing system is here and handled the right decorator

