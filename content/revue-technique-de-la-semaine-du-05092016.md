Title: Revue Technique de la semaine du 05/09/2016
Date: 2016-09-08 08:00
Author: foxmask
Category: Techno
Tags: Django, indexerror, python, samsung, pixel, apple, docker, firefox
Slug: revue-technique-de-la-semaine-du-05092016
Status: published

Cela faisait un bon moment que je ne m'etais pas penché sur une revue technique, depuis ma migration Wordpress => Pelican à vrai dire :)

Donc voici un petit tour de la technosphere des sujets, projets (et autre bidules machins trucs) croisés sur le chemin 

Wallabag 2.0.8
==============

[Wallabag](https://wallabag.org) nous gratifie d'une version 2.0.8 avant une potentielle 2.1

Sam et Max
=========

'ils' sont de retour avec de nouveaux billets dont le dernier aborde UUID : [Vérifier qu'un UUID est valide en Python](http://sametmax.com/verifier-quun-uuid-est-valide-en-python/)

Django
======

... et une nouvelle release
---------------------------

[une version 1.10.1 contentant quelques bugfix](https://www.djangoproject.com/weblog/2016/sep/01/bugfix-release/)

... et Docker
-------------

[Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)


... et le framework message
---------------------------

* [Django Tips #14 Using the Messages Framework](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)
* [Django Tips #13 F() Expressions](https://simpleisbetterthancomplex.com/tips/2016/08/23/django-tip-13-f-expressions.html)

... et sa config gunicorn
-------------------------

[Deploying Django with Gunicorn and Supervisor](https://samoylov.tech/2016/08/31/deploying-django-with-gunicorn-and-supervisor/)
Billet que j'ai trouvé trop trop trop court comparé à un de [mes vieux billets](https://foxmask.trigger-happy.eu/post/2015/06/19/supervisor-celery-django-orchestration/)


Python
======

La couverture de ce livre [Python 201](http://www.blog.pythonlibrary.org/2016/09/06/python-201-is-officially-published/), m'a fait penser à un coaching culinaire par Ratatouille :) N'en demeure pas moins qu'il existe ... pour les dev intermediaires.

7 trucs pour ecrire du code plus meilleur ;)

<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">7 Simple <a href="https://twitter.com/hashtag/Tricks?src=hash">#Tricks</a> to Write Better <a href="https://twitter.com/hashtag/Python?src=hash">#Python</a> Code <a href="https://t.co/uqEN50U7nI">https://t.co/uqEN50U7nI</a> <a href="https://t.co/dk2NDVVhZd">pic.twitter.com/dk2NDVVhZd</a></p>&mdash; Nicolas RAMY (@darkelda) <a href="https://twitter.com/darkelda/status/770554167932968960">30 août 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


IndexError  
==========

Comment pourquoi que ca marche-t-il (pas) mon code, S.O.S d'un codeur en détresse :  

voici les 5 derniers sujets traités ou en cours sur
[IndexError.net](http://IndexError.net)

* [Facebook API](http://indexerror.net/4267/facebook-api)
* [Ajouter des données aux fields d'un form](http://indexerror.net/4257/ajouter-des-donn%C3%A9es-aux-fields-dun-form)
* [Architecture : faut-il limiter les methodes accessibles d'un objet ?](http://indexerror.net/4265/architecture-faut-limiter-methodes-accessibles-dun-objet)
* [Comment trier les logs de ses différentes applis ?](http://indexerror.net/4259/comment-trier-les-logs-de-ses-diff%C3%A9rentes-applis)
* [decorateur async await](http://indexerror.net/4203/decorateur-async-await)
* [vos types customisés utiles](http://indexerror.net/4198/vos-types-customis%C3%A9s-utiles)


Meetup
======

La rentrée scolaire annonce son lot de rencontres, dont une le 13/09 : [Paris Devops](https://www.meetup.com/fr-FR/Paris-Devops-Meetup/events/233922902/)


Firefox
=======

On nous promettrait un Firefox [7x plus rapide que l'actuel](https://techcrunch.com/2016/09/02/multi-process-firefox-brings-400-700-improvement-in-responsiveness/) grâce au multiprocessing, qui arriverait entre la version 49 et la 51.
On pourrait déjà testé la fonction en l'activant depuis "about:config" en changeant le paramètre "browser.tabs.remote.autostart" à True.
Un temps sur mobile, le multiprocessing a été retiré car produisant un bottleneck, mais avec cette amélioration sur la version desktop, le mutliprocessing sur la version sur mobile pourrait faire son retour.



Smartphone
==========

Coté smartphones, pendant que [Samsumg met le feu](http://www.frandroid.com/marques/samsung/375914_galaxy-note-7-de-samsung-bientot-bannis-vols-americains), [Apple se mouille 30minutes 'max'](http://www.frandroid.com/marques/apple/376170_apple-watch-series-2-officielle) et nous fait des écouteurs [sans fils](https://twitter.com/TheRealSheldonC/status/773787951260114944) et Google rebaptise sa gamme [Nexus en Pixel](http://www.frandroid.com/marques/google/375266_google-lancerait-cet-automne-pixel-pixel-xl-a-place-nexus) pour faire moins geek et plus grand publique.


Ce n'est qu'un au revoir
========================

Un dinosaure qui disparait d'internet, [Readability](http://www.readability.com) ferme ses portes le 30 de ce mois, à vos API, à vos migrations de service, de préférence vers Wallabag ;)

C U
===

A bientôt !
