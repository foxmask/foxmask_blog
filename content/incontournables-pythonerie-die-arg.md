Title: Incontournables Pythonerie : Die Arg
Date: 2013-02-25 10:00
Author: foxmask
Category: Techno
Tags: python, pythonerie
Slug: incontournables-pythonerie-die-arg
Status: published

*"Die Arg"*, n'est pas le dernier opus de Bruce Willis ;) mais derrière
ce titre j'ai caché le [module
argparse](http://docs.python.org/dev/library/argparse.html "Module Argparse")
;)

*En préambule à ce billet, j'ai entrepris de produire des billets sur un
script j'exploite en prod dans mon quotidien.  
J'ai donc découpé ce script en petits bouts pour vous illustrer chaque
partie que j'ai exploité, et la première d'entres elles est ce qui
suit;)*

Ce dernier permet de traiter/interpreter les arguments entrés sur la
ligne de commandes, à la suite du nom de votre script.

Coté PHP, seuls les framework en propose(raie)nt, tels Jelix, ZF, SF,
CakePHP, etceteri etcetara

Avant de vous montrer le module argparse, je me dois de vous montrer à
quoi ressemble un script python sans l'usage de celui ci.

Le script ci dessous va afficher un texte succinct quand les paramètres
attendus ne seront pas au rendez vous ou vous affichera une phrase avec
ce qui a été saisi :

[test\_arg.py](https://github.com/foxmask/pythonerie/blob/die_arg/test_arg.py)

```python
from sys import argv

def main():
    #mettons ici un peu d'aide quand l'utilisateur ne s'en sortira pas
    usage = "To run the script enter -e environment name -r release name.   
           \nfor example : \npython test_arg -e foxenv -r v1.0-FINAL   
           \n\nYou can optionally use the switches :   
           \n -c /path/to/configfile to use an alternative configfile   
           \n -l /path/to/logging/config/file to use an alternative configfile  
for logging"
    env = ''
    release = ''
    #pas mis assez d'arguments
    if len(argv) < 2:
        #affichons donc l'aide
        print usage
        exit (0)

    #oops un pb ? on n'a pas encore le bon compte d'arguments
    if len(argv) < 5 and len(argv) > 2:
        print "the environment name ( specified with -e ) and release name  
( specified with -r ) are mandatory "
        exit (0)

    switch = argv[1]
    switch2 = argv[3]
    #où est quoi ? 
    #vérifions l'order des switches
    if switch == '-e' and switch2 == '-r':
        env = argv[2]
        release = argv[4]
    elif switch == '-r' and switch2 == '-e': 
        env = argv[4]
        release = argv[2]
    #j'ai tape portenawak - affichons ce qui ne va pas
    else:
        print "the environment name ( specified with -e ) and release name  
( specified with -r ) are mandatory "
    #tout est ok : 
    #affichage des valeurs entrées sur la ligne de commandes
    print "environment {0} release {1}".format(env,release)


if __name__ == '__main__':
    main()
```

Ainsi en tapant :

```shell
python test_arg.py
```

on obtient l'aide :

```shell
To run the script enter -e environment name -r release name.             
for example : 
python test_arg -e foxenv -r v1.0-FINAL             

You can optionally use the switches :             
 -c /path/to/configfile to use an alternative configfile             
 -l /path/to/logging/config/file to use an alternative configfile for logging
```

Ensuite

```shell
python test_arg.py -r 123.2 -e fox
```

donne :

```shell
environment fox release 123.2
```

Ok parfait ca marche mais c'est tiré par les cheveux, fastidieux et
quand on a plus complexe à traiter on n'est pas sorti de l'auberge.

Voici à présent la même version avec le module "optparse" (la version
fonctionnant avec ma debian et python 2.7, argparse étant pour la v3 de
python)

[test\_optparse.py](https://raw.github.com/foxmask/pythonerie/die_arg/test_arg.py)

```python
from optparse import OptionParser
import os

def main():
    #meme message d'aide en plus concis
    usage = "%prog -e environment name -r release name. \nfor example : \npython test_optparse -e envname -r 20130101"
    parser = OptionParser(usage)
    #ajout d'option de paramètres utilisables 
    parser.add_option("-e", "--env", dest="environment",
                      help="the environment name to use to build the delivery", metavar="ENV")
    parser.add_option("-r", "--rel", dest="release",
                      help="the release name of this delivery (used to name the final package like release-RELEASE-yyyymmdd)", metavar="RELEASE")
    parser.add_option("-c", "--conf", dest="configfile",
                    help="the path where the config file is located. This file should contain the name of the environment from which to download the archives. By Default the script will search in ./env_dirs.conf", default="./env_dirs.conf", metavar="CONFIG")
    parser.add_option("-l", "--log", dest="configlogfile",
help="the path where the config file for the loggging is located.", metavar="LOGGING_CONFIG")
    (options, args) = parser.parse_args()
    #je n'ai pas donné d'environement ni de release ... hophop error :)
    if options.environment == None or options.release == None:
        parser.error("options -e and -r are mandatory")
    else:
        print "environment {0} release {1}".format(options.environment,options.release)

if __name__ == '__main__':
    main()
```

Cours précis clair :)  
A présent en tapant la ligne précédente sans aucun argument on obtient
:

```shell
python test_optparse.py 
Usage: test_optparse.py -e environment name -r release name. 
for example : 
python make_delivery -e envname -r 20130101

test_optparse.py: error: options -e and -r are mandatory
```

la différence est que cette fois ci une erreur est retournée. (c'est le
message dans parse.error)

A présent le petit plus, pas dégueux, en tapant **python
test\_optparse.py -h** on obtient :

```shell
Usage: test_optparse.py -e environment name -r release name. 
for example : 
python test_optparse -e envname -r 20130101

Options:
  -h, --help            show this help message and exit
  -e ENV, --env=ENV     the environment name to use to build the delivery
  -r RELEASE, --rel=RELEASE
                        the profinance release name of this delivery (used to
                        name the final package like release-RELEASE-yyyymmdd)
  -c CONFIG, --conf=CONFIG
                        the path where the config file is located. This file
                        should contain the name of the environment from which
                        to download the archives. By Default the script will
                        search in ./env_dirs.conf
  -l LOGGING_CONFIG, --log=LOGGING_CONFIG
                        the path where the config file for the loggging is
                        located. By Default the script will search in
                        ~/MakeDelivery/logging.conf
```

Voilà, tout propre, nickel !

le reste fonctionne exactement pareil !

Merci (arg|opt)pargse ;)

[les sources de l'article sont disponibles sur
github](https://github.com/foxmask/pythonerie/tree/die_arg)

*La prochaine partie traitera du traitement des fichiers de
configuration*

