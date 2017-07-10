Title: Fabric, et la contrib django pour acceder à tous vos joujoux
Date: 2017-07-10 14:00
Author: foxmask
Category: Techno
Tags: python, Fabric, django
Slug: fabric-contrib-django
Status: 


Dans mon [billet précédent](https://foxmask.trigger-happy.eu/post/2017/07/06/fabric-sa-var-env-nos-variables-dynamiques), j'évoquais l'existence d'une "contrib" Fabric pour intégrer Django au sein de ses tasks Fabric, mais qu'elle déconnait...

Après maints tests supplementaires et digging ze toile, j'ai entrevu la lumière après la lecture de 3 issues chez Fabric [#1509](https://github.com/fabric/fabric/issues/1509), [#1033](https://github.com/fabric/fabric/issues/1033), [#1207](https://github.com/fabric/fabric/issues/1207).

Tout compulsé ca donne ceci :


```python

# coding: utf-8
import sys
import os
# ajout du chemin où se trouve projetA
path = os.path.join(os.path.dirname(__file__), '../../projeta')
sys.path.insert(1, path)

# appel de la librairie django de Fabric pour appeler les objets Django
from fabric.contrib import django
django.project('projeta')

# import de django
import django
# setup django
django.setup()

# appel du model
from projeta.models import MonModel

def main():
    print(MonModel.objects.get(name='foobar'))

```
execution

```bash
$ fab main

foobar

Done.

```


Ceci fonctionne (pour un vhost) si vous avez collé votre appli "fabric" dans le même dossier que celui du projet Django, sinon adapter la ligne **path =** pour que ca match votre env




