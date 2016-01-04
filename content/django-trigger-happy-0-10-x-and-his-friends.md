Title: Django Trigger Happy 0.10.x and his friends
Date: 2015-04-23 11:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-10-x-and-his-friends
Status: published

I released a version 0.10.1 of the Trigger Happy project with :

**News :**

-   Search engine based on Haystack (when we have more than 30 triggers
    that begins to be useful:)
-   a *Holidays* mode, permits to pause all the triggers until you
    return, thus you will be really "disconnected" during your holidays
    :)

**Improvments :**

-   support Django 1.8
-   support python 3
-   support of some not well handled accented characters now fixed with
    a *html\_entities php like*
-   contribution from [Adrihein](https://github.com/Adrihein) on the
    layout of the application

**His friends too :**

-   module Twitter : /!\\ a column changed of type : bigint vs int
-   module Evernote : nothing special
-   module Pocket : nothing special
-   module RSS : nothing special
-   module Readability : nothing special
-   module Dummy : nothing special

**Next :**  
I was not very productive on the version because in the meantime, I
have lingered over  
[Crossbar.io](http://crossbar.io/) / [WAMP.WS](http://wamp.ws) /
[Autobahn](http://autobahn.ws/python/) to produce a sandbox
[wamp-th](https://github.com/foxmask/wamp-th).

This one works great !  
Some details need to be fixed and that should be ok ;)  
Once it's done, that should replace the "managment commands" which are
actually put in a crontab.

This should permit to speed up Trigger Happy again and make all funs
interactions :)

Have Fun !

[where to find the project](http://trigger-happy.eu/)  
[where to find the sources](https://github.com/foxmask/django-th/)  
[where to find the doc](https://trigger-happy.readthedocs.org/)

ps : I told myself there was no reason to not publish a post in English,
as the majority of you on github dont come from France ;)

