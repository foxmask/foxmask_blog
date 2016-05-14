Title: Panda, Le gros nounours noir et blanc est passé 
Date: 2016-05-14 13:00
Author: foxmask
Category: Techno
Tags: TriggerHappy, python, Pandas
Slug: le-gros-nounours-noir-et-blanc-est-passe
Status: published

En lisant ma pile d'article de veille techno dans mon instance [wallabag](https://walabag.org), je suis tombé sur une article mesurant le temps passé sur ses projets.
Rien de nouveau au soleil puisque tout à chacun connait bien [pandas](https://pypi.python.org/pypi/pandas) :)

Cependant, après un petit coup de `pip install git-pandas` et en exécutant [ce script panda](https://github.com/wdm0006/git-pandas/blob/master/examples/hours_estimate.py) on peut donc mesurer le temps passé directos sur ses dépots, et donc pour bibi, il en ressort ceci 

```bash

$ python hours_estimate.py |grep -v 0.00000

            committer       hours         repository
0             foxmask    2.603889          django-th
3       Olivier Demah  134.288056          django-th
4             FoxMaSk    3.017500          django-th
0       Olivier Demah    3.000000  django-th-ansible
0       Olivier Demah    3.877222       wallabag_api
0       Olivier Demah    8.882778        dj-diabetes
1             foxmask    1.000000        dj-diabetes
```

* En tout 140heures pour Trigger Happy.

  Si je pars sur des journées de 6heures ca fait 23jours ou 46jours en codant "à temps perdu", en gros un bon moi et demi non stop quoi.

* 4hres pour l'API [wallabag](https://github.com/foxmask/wallabag_api)
* 9hres pour le projet de "[gestion de son diabete au quotidien](https://github.com/foxmask/dj-diabetes)"

Pas de quoi fouetter un chat, mais ca donne une idée du temps que j'ai dépensé ;)
