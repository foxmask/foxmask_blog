Title: Django Trigger Happy 0.9.0 is out and Python 3.4.0
Date: 2014-05-14 10:37
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-9-0-is-out-python-3-4-0
Status: published

[cet article est aussi dispo en français
ici](/post/2014/05/14/django-trigger-happy-0-9-0-is-la-python-3-4-0/ "Django Trigger Happy 0.9.0 is là et Python 3.4.0")

**Intro :**  
Trigger Happy is a project (written in
[python](https://www.python.org/) with
[django](https://www.djangoproject.com/)) which aims to be a free and
opensource alternative to [IFTTT.com](https://ifttt.com/).

Trigger Happy can be defined as a micro
[ESB](http://en.wikipedia.org/wiki/Enterprise_service_bus "Enterprise Service Bus").

**And here we go** (again:) :  
2 months ago I published the version 0.8.3 which was the last release
working only with Python 2.7.x.  
Since the release of Python 3.4.0 and some very interesting features
(that I still try to exploit to improve Trigger Happy), I decided that
was the moment to dive into Python 3 with Django Trigger Happy. It’s now
a thing done. After 2 month to dig if all the existing services I used
were compatible, I finished by releasing a
[0.9.0](https://pypi.python.org/pypi/django_th/0.9.0).

So in the version, a few things changed in the core (almost nothing in
fact). I just consolidated the most part of the code to be able to be
used with python 3.4.x and third party lib for each service we would
like to use like [Evernote](https://evernote.com/),
[Pocket](http://getpocket.com/),
[Readability](https://www.readability.com/).

-   Actually just Pocket provides a Python 3 version installable from
    pip command.
-   Evernote provides also a Python 3 version [but only from
    github](https://github.com/evernote/evernote-sdk-python3), as no
    final official release from Pypi exists yet, we have to install it
    by hand, which is not very pretty simple compared to pip.
-   For readability [It should be Ok for python 3 too,
    soon](https://github.com/arc90/python-readability-api/issues/31).

All of this justify the choice to switch from Evernote to Pocket as the
default service used by Trigger Happy to store your
news/stuff/whatever.  
About the Front part, I migrated from
[Bootstrap](http://getbootstrap.com/) 2 to 3 and add some little things
to be easier to use.

All was not painless but now everything works fine (again;)

**Read the docs** :  
I also pushed the doc on
[readthedocs](http://trigger-happy.readthedocs.org/).

**Roadmap** :  
What Do I plan now ?

1.  Improving Trigger Happy to be faster by using
    [asyncio](https://docs.python.org/3/library/asyncio.html) or
    equivalent
2.  Improving the UI of Trigger Happy. When you see IFTTT and Trigger
    Happy, you can imagine the work to do to reach the same UX. But as
    i'm not a designer I do simple things, but things that work
3.  New service(s) ? : Some months ago I did a poll to know which
    website/service you will use with Trigger Happy, the winner was
    Twitter, but I was not motivated enough to do it. I think the time
    has come to try again to manage it
4.  Some ideas from your wishlist ?
5.  feel free [to fork it](https://github.com/foxmask/django-th),
    contribute, report bug

