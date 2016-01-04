Title: Django Trigger Happy 0.9.0 is là & Python 3.4.0
Date: 2014-05-14 11:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-9-0-is-la-python-3-4-0
Status: published

[this article is also available in english
here](/post/2014/05/14/django-trigger-happy-0-9-0-is-out-python-3-4-0/ "Django Trigger Happy 0.9.0 is out & Python 3.4.0")

**Intro :**  
Trigger Happy est un project (ecrit en
[python](https://www.python.org/) avec
[django](https://www.djangoproject.com/)) opensource qui a pour but
d'être une alternative libre de [IFTTT.com](https://ifttt.com/).

Trigger Happy peut être défini comme un micro
[ESB](http://fr.wikipedia.org/wiki/Enterprise_service_bus "Enterprise Service Bus").

**And here we go** (again:) :  
Il y a 2 mois je publiais la dernière version "uniquement" compatible
python 2.7.x  
Depuis la sortie de Python 3.4.0 et quelques intéressantes
fonctionnalités (que j'essaye encore d'exploiter pour améliorer Trigger
Happy), j'ai décidé que le moment de sauter le pas vers Python 3 était
venu avec Django Trigger Happy.  
C'est maintenant chose faite. Après 2 mois à creuser si tous les
services que j'utilisais étaient compatibles, j'ai fini par publier la
version [0.9.0](https://pypi.python.org/pypi/django_th/0.9.0).

Donc dans cette version, peu de chose du core ont changé (quasiment rien
en fait). J'ai essentiellement consolidé le code existant pour qu'il
soit utilisable avec Python 3.4.x et les lib tierces pour chaque service
que nous souhaitons utiliser comme [Evernote](https://evernote.com/),
[Pocket](http://getpocket.com/),
[Readability](https://www.readability.com/).

-   Actuellement, seul Pocket fourni une version installable pour Python
    3 version depuis la command pip
-   Evernote fourni aussi une version pour Python 3 [mais seulement
    depuis github](https://github.com/evernote/evernote-sdk-python3),
    car aucune version finale et officielle n'existe sur Pypi, on doit
    donc l'installer à la main ce qui n'est pas super pratique comparer
    à pip.
-   Pour readability [ca devrait être dispo assez
    vite](https://github.com/arc90/python-readability-api/issues/31).

Tout ceci justifie le choix de permuter (de Evernote à Pocket) le
service par défaut utilisé par Trigger Happy pour stocker vos news (par
exemple ou tout autre chose).  
Pour ce qui est de la partie front/web, j'ai migré de
[Bootstrap](http://getbootstrap.com/) 2 à 3 et ajouté quelques petites
choses pour que l'appli soit plus facile d'utilisation.

Enfin tout n'a donc pas été sans mal mais ça marche bien à présent.

**Read the docs** :  
J'ai enfin publié la doc sur
[readthedocs](http://trigger-happy.readthedocs.org/). Au cas où ;)

**Roadmap** :  
Et pour la suite ?

1.  Améliorer Trigger Happy pour qu'il soit plus rapide en utilisant
    [asyncio](https://docs.python.org/3/library/asyncio.html) ou un
    équivalent
2.  Améliorer l'UI de Trigger Happy. Quand vous regardez IFTTT et
    Trigger Happy, vous pouvez facilement imaginer la somme de travail à
    accomplir pour atteindre le même résultat. Mais comme je ne suis un
    designer je fais des choses simple, mais des choses qui marchent
3.  Nouveau(x) service(s) ? : Il y a quelque mois j'avais émis un
    sondage pour savoir quel service vous aimeriez le plus utilisez avec
    Trigger Happy, et le gagnant fut Twitter, mais je n'étais pas très
    motivé pour m'y mettre. Je pense qu'à présent je vais pouvoir y
    retourner ;)
4.  D'autres idées dans votre propre liste ?
5.  Vous pouvez aussi [forker le
    projet](https://github.com/foxmask/django-th), contribuer, reporter
    des bugs

edit: dans le pipe j'ai débuté une lib pour traiter des imports/exports
OPML

