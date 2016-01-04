Title: Django Trigger Happy 0.11.0 English Version
Date: 2015-08-18 10:43
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-11-0-english-version
Status: published

Hi,  
Here is an English Version of my post I made Yesterday, that I couldnt
forget to publish ;)

So, Here comes a small update of my little project, micro ESB, allowing
to orchestrate data retrieval and publishing, while exploiting your own
Internet services (like Twitter to name one). Just to stay the master
and crontrol your data without having to give your access permissions to
anyone.

In celebration program :

**New Functions**

-   Its now possible to **produce RSS flux** from the data, retrieved by
    another service we will installed.  
    [![Installed
    Services](/static/2015/08/service_installe.png)](/static/2015/08/service_installe.png)
    For example from the Twitter service.  
    Typically we do a trigger for publishing on twitter, anything that
    comes from a site such as the week in chess, follow the news. Now
    you can do the opposite.  
    Follow hashtag \#chess, for example, and all that will be published
    on this subject, will eventually be generated in an RSS feed by
    TriggerHappy. I extend a hello to lonely friends of **[yahoo
    pipes](https://pipes.yahoo.com/pipes/)** to whom I did that, with a
    foot call from sam&max ;-)

-   **New service Integration** : **Trello**. "is the free, flexible,
    and visual way to organize anything with anyone." as it defines
    itself. You can then add card of things to do to organize your
    project. This adds a toy to the list of keys ring : Twitter,
    Evernote, RSS, Readability, Pocket
-   **Search engine** (based on haystack & elasticsearch).It is not
    luxury when you ended up having a lot of triggers, existential
    questions arise "well I had yet created a trigger that spoke of
    recipes Breton cuisine" ;-)
-   A function "**holidays**" which disables all the triggers, to enjoy
    his vacation for good ! Then, when you will come back from holidays,
    you disable the holidays mode which will reactivate the triggers
    that were enable before.

**Technical improvements**

-   No more Python2 anywhere. This force me to find solutions of other
    lib oauth2 authentication for the services like readability and
    Evernote. Blessing in disguise ! [requests
    oauthlib](https://requests-oauthlib.readthedocs.org/en/latest/) is
    the solution like anyone can imagine :-)
-   Django 1.8.x (naturally)
-   Reorganisation of services modules in one application rather than
    having a repository for each module, I ended up all together in
    filing trigger-happy.  
    Currently it's convenient for releasing and for unit testing, but
    my gut tells me that at one time I bite into fingers.
-   Managing a limit on the number of publications to a service. Example
    : I publish on Twitter more than 30 websites that I follow. At a
    given moment, the news of each of them come too much, that I publish
    too quickly on Twitter, this has the side effect, to "flood" the
    timeline of my friends and followers, who, instead of having a
    heterogeneous timeline ending by hate me to plublish quicker than
    que Lucky Luke. Now, "this" is over. We define a limit and when it's
    reached, we publish the rest later.

**Performances**

-   As I'm never satisfied of what I produce, even when I finish a thing
    I tell myself I can do even better. From this perspective,
    therefore, I articulated the code based on the "[framework
    cache](https://docs.djangoproject.com/en/1.8/topics/cache/)" of
    django which permits to use the backend of your choice. Thus, all
    retrieving of data of all the service, is put in the cache. Then, at
    the publishing moment, TriggerHappy will pick the data in the cache.
    Before that, all was synchrone.
    [Now](/post/2015/06/19/supervisor-celery-django-orchestration/)
    [Celery](http://celery.readthedocs.org/) orchestrates this
    retrieving of data and their publishing.


**[Documentation](http://trigger-happy.readthedocs.org/)**

-   Updated everywhere. Do not hesitate a moment to read it
-   To upgrade from the previoous release [everything is here, a
    migration that took me time to
    finalize](http://trigger-happy.readthedocs.org/en/latest/migration.html)


And tommorow ? [some new
service](https://github.com/foxmask/django-th/labels/module) are
planned, and [some other
ideas](https://github.com/foxmask/django-th/issues) :)

I also took the opportunity to rearrange tickets/labels/milestones on
github, an easy way to find what one seeks to facilitate
[contributions](https://github.com/foxmask/django-th/blob/master/CONTRIBUTING.md).

**Thanks !**  
Thank [to some
interested](https://github.com/foxmask/django-th/stargazers), [to some
curious](https://github.com/foxmask/django-th/watchers) and finally [to
contributors](https://github.com/foxmask/django-th/graphs/contributors)
who try to tiptoe ;)

links :

-   [Trigger Happy](http://trigger-happy.eu) home page
-   [Trigger Happy](https://github.com/foxmask/django-th) GitHub
    repository

