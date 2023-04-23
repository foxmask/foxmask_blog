Title: Intégration continue de Github à Pypi via Travis-CI
Date: 2016-03-04 19:00
Author: foxmask
Tags: pypi, travisci, github
Category: Techno
Slug: integration-continue-de-github-a-pypi-via-travis-ci
Status: published
Summary: Travis CI is magic, moins on en fait plus il en fait à notre place !

L'an passé, lors de la release [0.11.0](https://blog.trigger-happy.eu/django-trigger-happy-0.11.0.html) de [TriggerHappy](https://trigger-happy.eu), je n'étais pas parvenu à faire fonctionner [Travis-CI](https://travis-ci.org/foxmask/django-th/) comme je l'escomptais, pour qu'il publie tout seul cette version sur [PyPi](http://pypi.python.org). 

Du coup je m'étais bien pris la tête pour préparer le terrain pour la version suivante.

Et cette nuit, lors de la sortie de la [0.12.0](https://blog.trigger-happy.eu/django-trigger-happy-0.12.0.html) j'étais zo zanges :)

Donc "Comment ça marche la fusée ariane ?" dirait [Michel Chevalet](https://fr.wikipedia.org/wiki/Michel_Chevalet)

Tout simplement en 2 temps :

1) le fichier .travis.yml sur son repository github

```yml

deploy:
  provider: pypi
  user: votre_login_pypi
  password:
    secure: le_mot_de_passe_crypte
  on:
    Tags: true

```

ici je ne vous ai mis que la tâche `deploy` chargée de s'occuper de l'installation de vos sources sur pypi sous la forme d'une archive, en respectant le nommage défini dans votre `setup.py`


![creation de l'archive](/static/2016/03/django_th_uploaded_on_pypi_0.png)



2) sur Travis-CI, détection de l'application d'un tag sur le projet, via le déclencheur `on: Tags: true`, et enchaînement de la tâche `deploy`

![deployment sur pypi](/static/2016/03/django_th_uploaded_on_pypi.png)


C'est tout QQ et tout simple comme on aime et, évidemment très efficace !
