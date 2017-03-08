Title: Incontournables Pythonerie : BigBrother is logging you
Date: 2013-03-11 10:00
Author: foxmask
Category: Techno
Tags: python, pythonerie
Slug: incontournable-pythonerie-bigbrother-is-logging-you
Status: published

Comme chacun sait, il est ûber bradiqueu de suivre ce que fait son
programme, pour tenter de diagnostiquer tout problème protentiel dans
son application.  
Pour cela on exploite tous plus ou moins la même chose avec nos
langages respectifs, le plus répandu en JAVA par exemple, étant
[log4j](http://logging.apache.org/log4j).

En Python donc, on dispose du module
[Logger](http://docs.python.org/2/library/logging.html "Documentation sur le module Logger").

Comment marche un système de journalisation :

-   on défini un nom de fichier dans lequel sera ajouté tous les
    évènements de son programme
-   on défini un niveau de journalisation parmi
    INFO,DEBUG,WARN,ERROR,CRITICAL
-   on défini un formatage des lignes de journalisation

Voici comment tout cela se passe avec Logger :

**Où logger & les niveaux de log**

Un exemple le plus basique qui soit, consiste à afficher un message dans
la console à l'exécution du script :

```python
import logging
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
```

vous affichera un beau

```shell
WARNING:root:Watch out!
```

Cela est bien sympathique mais la plupart du temps on veut mettre tout
cela dans un fichier de log, ceci s'effectue comme suit :

```python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

A présent plus rien ne s'affiche à la console mais votre fichier
example.log contient bien comme attendu :

```log
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
```

Dans la foulée, on en a profité pour définir le niveau de journalisation
à DEBUG (via level=logging.DEBUG), ce qui nous a permit d'avoir toutes
les traces dans le fichier de log

Il est par ailleurs tout à fait possible d'utiliser la journalisation au
travers de plusieurs modules :

```python
# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
```

```python
# mylib.py
import logging

def do_something():
    logging.info('Doing something')
```

ce qui affichera :

```log
INFO:root:Started
INFO:root:Doing something
INFO:root:Finished
```

**Formatage des logs**  
Après avoir vu où logger et quel(le)s (niveaux d') infos, voici à
présent le formatage de ses chers log:

```python
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG),\ 
                    format='%(asctime)s %(message)s')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

ceci vous produire une ligne affichage la date courant + le message :

```log
2013-02-22 14:43:08,486 This message should go to the log file
2013-02-22 14:43:08,487 So should this
2013-02-22 14:43:08,487 And this, too
```

Enfin voici un exemple complet avec en plus un fichier de configuration
de log définissant par module, où mettre les logs (console / fichier) et
quels niveaux de détail ces logs auront :

**logging.conf:**

```ini
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

Ce fichier de configuration des log défini, on l'exploite ensuite dans
son script comme ceci :

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
```

Ce qui produira comme log :

```log
2013-02-22 14:57:30,744 - simpleExample - DEBUG - debug message
2013-02-22 14:57:30,745 - simpleExample - INFO - info message
2013-02-22 14:57:30,745 - simpleExample - WARNING - warn message
2013-02-22 14:57:30,745 - simpleExample - ERROR - error message
2013-02-22 14:57:30,745 - simpleExample - CRITICAL - critical message
```

la première colonne contient la date, la seconde, le script
utilisé/logger utilisé, la troisième le niveau d'info de log, et enfin
la ligne de log elle même qu'on a écrit dans le code.

**Quelques subtilités**, vous permettent :

1\) d'avoir un fichier de log par exécution avec l'option filemode="w"
comme ceci :

```python
logging.basicConfig(filename='example.log',level=logging.DEBUG, filemode="w")
```

2\) de définir le niveau de log sur la ligne de commande si cela vous
botte via --log=INFO par exemple

3\) d'avoir des lignes de log utilisant des variables comme ceci

```python
logging.warning('%s before you %s', 'Look', 'leap!')
```

qui affichera

```log
Look before your leap!
```

4\) de jouer sur le format d'affichage de la date comme ceci :

```python
logging.basicConfig(filename='example.log',level=logging.DEBUG,  
                   format='%(asctime)s %(message)s',  
                   datefmt='%m/%d/%Y %I:%M:%S %p')
```

Ce billet est très largement inspiré de la doc, très bien faite, et
m'aura permit de vous présenter un nouveau volet indispensable à vos
développements ;)

