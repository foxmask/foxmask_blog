Title: Django Trigger Happy - une première 
Date: 2013-05-27 11:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy
Status: published

Voici le premier projet un peu plus conséquent que les petits modules
que je faisais de ci de là.

Ce dernier est entièrement inspiré du service IFTTT "If This Then That"
.

**Description**  
Le principe du service est d'effectuer une action (souvent, stocker une
information, ou la relayer) en fonction d'un événement se produisant
n'importe où sur internet à partir d'une source donnée.  
Ce projet peut être utiliser pour vos besoins propres tout comme votre
blog, ou vous pouvez également décider " d'héberger " les Triggers de
vos potes.

**Pourquoi ce projet ?**  
Comme à chaque fois que je me lance dans un truc c'est par réaction
(épidermique ?) d'une solution qui ne fonctionne pas comme
j'escomptais.  
Ici IFTTT marche bien, mais pas assez à mon goût, j'ai des problème
d'encoding UTF8 très très désagréable ;) genre "cet été je pars en
lozère" devient "cet t je pars en lozre"...  
Donc après avoir testé d'autres solutions genre CloudWork, j'étais ravi
... mais estomaqué du coût ! l'offre fonctionne au nombre de triggers à
journée. Or un trigger chez CloudWork ce n'est pas un trigger chez
IFTTT. Chez CloudWork un trigger c'est UN déclenchement, et non pas la
programmation d'un déclenchement. Donc quand on est limité à 100
triggers à raison d'un toutes les 10min ... bonjour la facture :P

**Exemple d'utilisation**  
Par exemple, vous suivez les billets d'un blog régulièrement, et vous
ne souhaitez pas en perdre une miette. Vous définissez alors un
"trigger" qui se déclenchera quand un nouveau billet paraîtra, alors
ensuite vous déciderez d'en faire ce que bon vous semble, comme le
publier sur vos réseaux sociaux favoris ou encore stocker le billet dans
Evernote ou ailleurs.

C'est très pratique car vous ne dépendez plus d'aucune solution de
lecteur de flux RSS par exemple comme Feedly, GoogleReader ou autre.

**Aujourd'hui**  
Actuellement "Trigger Happy" ne sait faire que 2 choses : lire des flux
RSS, et stocker ceux ci dans Evernote, dans le carnet de votre choix
avec le tag de votre choix.

**Mise en route**

1\) On procédera comme pour tout projet django avec un

```python
python manage.py syncdb
```

suivi du lancement du serveur.

On mettra dans une crontab (ou tout autre service de gestion de tâches
préprogrammées) le script fire.py à intervalle régulier, genre tous les
10min (mais en prenant bien garde de ne pas avoir des "pas" trop courts
afin de ne pas saturer le service cible qui pourrait vous bloquer
l'accès à leur service). Le script se chargera de collecter les
"nouvelles fraîches" pour vous les propager sur le(s) service(s)
cible(s).

2\) L'administrateur (ou même vous;) peut décider que tel ou tel service
soit mis à disposition ou non. Ceci permettant une modularité la plus
flexible possible.  
Donc, de là, la première chose à faire est d'aller dans l'admin et
activer les 2 services RSS et Evernote, en cochant la case "auth
required" pour d'Evernote. (cf explication ci dessous)

3\) Ensuite l'utilisateur, disposera des services qu'il devra à son tour
activer. Pour le service Evernote, comme l'administrateur aura coché la
case "auth required", l'utilisateur sera envoyé vers le service Evernote
pour demander que **l'utilisateur** autorise "Django Trigger Happy" de
créer des notes dans ses carnets.

4\) Une fois les services activés, il ne reste plus qu'à créer un trigger
avec le wizard existant, d'où on indiquera depuis quel flux RSS on veut
lire les sources de données, puis vers quel service on souhaite
stocker/publier ces données.

Si vous êtes accoutumé à IFTTT, vous vous rendez compte qu'il s'agit du
même processus ;)

**Demain**  
J'ai déjà prévu de pouvoir filtrer les flux RSS en fonction de
**contenu que je ne veux pas**. Imaginons un blog ou tout n'est pas SFW
:P ou plus simplement, sur le site de
[Pypi](https://pypi.python.org/pypi), énormément de projets publiés
arrivent avec une description "UNKNOWN" qui à mon goût ne mérite pas
qu'on s'y attarde puisque l'auteur n'a pas pris le temps de mettre une
description, il semblerait. Donc ce filtre permet d'éviter d'avoir un
contenu pollué vous l'aurez compris.

**Avenir**  
L'architecture produite me permet d'ajouter facilement un service tels
Twitter, Facebook, etc.

**et l'API**  
Pour le moment le projet débute tout juste mais je publierai un
prochain billet (et une page wiki) pour expliquer comment on s'ajoute un
service de plus, le plus aisément possible.

**Quelques Liens**

-   [Django Trigger Happy sur
    Pypi](https://pypi.python.org/pypi/django_th/) version 0.1
-   [Django Trigger Happy sur
    GitHub](https://github.com/foxmask/django-th)

**Last but not Least : Greetings !**  
Un petit mot de remerciements pour [Sam et Max](http://sametmax.com/) que
j'ai longuement sollicité et m'ont aidé sur l'archi à tenir ;)

