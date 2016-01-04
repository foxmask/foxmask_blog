Title: de PHP à Python : de composer à setuptools
Date: 2013-01-28 10:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, python
Slug: de-php-a-python-de-composer-a-setuptools
Status: published

[Comme introduit dans ce billet](/post/2013/01/14/de-php-a-python-tous-ensemble/ "de PHP à Python : tous ensemble"),
voici donc le premier billet de la série **de PHP à Python**.

**Gérer des dépendances à son projet ? il y a aussi une application pour
cela !**

**de PHP ...**

Cette application se nomme
[Composer](http://getcomposer.org/ "Composer")

Voici un extrait de la doc de Composer qui illustrera l'analogie qui
suit pour la version python

Le fichier
**[composer.json](http://getcomposer.org/doc/00-intro.md#using-composer)**
est disponible en principe sur chacun des dépôts des projets qu'on peut
trouver sur github et packagist.

C'est le fichier sur lequel tout repose.

[composer.json](https://raw.github.com/foxmask/de_php_a_python/de_composer_a_setuptools/composer.json "télécharger les sources"):

```php
{
    "repositories": [
        {
            "type": "package",
            "package": {
                "name": "smarty/smarty",
                "version": "3.1.7",
                "dist": {
                    "url": "http://www.smarty.net/files/Smarty-3.1.7.zip",
                    "type": "zip"
                },
                "source": {
                    "url": "http://smarty-php.googlecode.com/svn/",
                    "type": "svn",
                    "reference": "tags/Smarty_3_1_7/distribution/"
                },
                "autoload": {
                    "classmap": ["libs/"]
                }
            }
        }
    ],
    "require": {
        "smarty/smarty": "3.1.*"
    }
}
```

ici on comprendra qu'on s'est rajouté une dépendance sur smarty qui
n'est pas sur packagist mais sur un repository "privé".

**... à Python**
Cette application se nomme
[Setuptools](http://packages.python.org/distribute/setuptools.html)

L'homologue python sur lequel tout repose est le script
**[setup.py](https://raw.github.com/foxmask/de_php_a_python/de_composer_a_setuptools/setup.py "télécharger les sources")**
dont voici un exemple :

```python
from setuptools import setup, find_packages

setup(
    name='fox_php_lib',
    version='0.1',
    description='Fox dessine un mouton',
    author='foxmask',
    author_email='devnull@foxmask.info',
    url='https://github.com/foxmask/fox_php_lib',
    download_url='https://github.com/downloads/foxmask/fox_php_lib/fox_php_lib0.1.tar.gz',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
```

Ce setup permet (quasiment comme son homologue) :

-   De décrire un module, une lib
-   De télécharger l'archive, décrite au paramètre **download\_url**,
    via une commande particulière
-   De télécharger les dépendances (lors de l'installation), décrite au
    paramètre **packages** via une fonction find\_packages() qui
    parcourira mon application et identifiera les dépendances et les
    installera
-   les meta données
    **name**,**version**,**description**,**author**,**author\_email**,**classifiers**,
    sont assez explicites pour savoir ce qu'on y met ;)
-   De définir des **classifiers** utiles pour retrouver et "ranger" ses
    contributions sur Pypi (cf plus bas)

Comme on le voit sur la première ligne du script on a une ligne de code
python, plus tard on a la méthode find\_packages(), donc oui on a toute
latitude d'utiliser du python pour "peupler" ses variables.

A présent comment s'en servir ?

on tape simplement :

```shell
python setup.py install
```

qui installera votre lib/module/app comme attendue

pour composer, on taperait :

```shell
php composer.phar install
```

w00t :)

Une fois installée, on peut vérifier que la lib est dispo en tapant :

```python
foxmask@foxmask:~$ python
Python 2.6.6 (r266:84292, Dec 26 2010, 22:31:48)
[GCC 4.4.5] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from fox_php_lib import python
>>> python()
[2013-01-14 22:26:49.669036] Python ca rox
```

ce que fait cette lib est juste ce qui suit
([test.py](https://raw.github.com/foxmask/de_php_a_python/de_composer_a_setuptools/test.py "télécharger les sources")):

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

def python():
    print "[%s] Python ca rox" % datetime.now()

if __name__ == "__main__":
    python()
```

Dans la foulée de la création de notre setup.py, on peut très
allégrement publier sa lib / son appli sur [Python Package Index aka
"Pypi"](http://pypi.python.org/pypi), mais cela pourra faire partie d'un
autre billet sur son utilisation.

**presque le mot de la fin**
une dernière information quant à la publication de ce billet qui est
très largement inspiré du très bon article de [sam & max : Créer un
setup et mettre sa lib python en
ligne](http://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/)

**un dernier mot**
n'étant pas un utilisateur (même pas averti:P) de Composer, je me suis
basé sur la doc et l'aide précieuse
[d'Artemiz](https://twitter.com/armetiz) pour son support à sa
compréhension ;)

nota : [les sources de l'article sont disponibles sur
github](https://github.com/foxmask/de_php_a_python/tree/de_composer_a_setuptools)

