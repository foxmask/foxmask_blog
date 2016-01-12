Title: Centos et la galère galère des installations recentes PostgresSQL 9.4 et du driver psycopg2
Date: 2016-01-12 12:00
Author: foxmask
Category: Techno
Tags: centos, python, postgresql, psycopg2
Slug: centos-galere-galere-postgresql-pyscopg2
Status: published

Parfois il arrive qu'on croise des distributions qui nous rebutent... mais avec lesquelles il faut composer.

Aussi voici un rapide retour d'XP sur l'installation de PostgreSQL 9.4 pour Centos et de son driver psycopg2 pour son virtualenv...

Pour l'installation de PostgreSQL 9.4 je vous renvois [à la doc](https://wiki.postgresql.org/wiki/YUM_Installation) super bien faite que je ne vais pas vous remettre en intégralité ici

Ensuite pour l'installation du driver dans son virtualenv, c'est pas de la tarte, voici :

```shell

(foxmask)foxmask@localhost:~/icibase $ pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.6.1.tar.gz
    Complete output from command python setup.py egg_info:
    running egg_info
    creating pip-egg-info/psycopg2.egg-info
    writing pip-egg-info/psycopg2.egg-info/PKG-INFO
    writing top-level names to pip-egg-info/psycopg2.egg-info/top_level.txt
    writing dependency_links to pip-egg-info/psycopg2.egg-info/dependency_links.txt
    writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'
    warning: manifest_maker: standard file '-c' not found
    
    Error: pg_config executable not found.
    
    Please add the directory containing pg_config to the PATH
    or specify the full executable path with the option:
    
        python setup.py build_ext --pg-config /path/to/pg_config build ...
    
    or with the pg_config option in 'setup.cfg'.

```

c'est pas de la tarte, parce qu'evidement le setup.py du dossier courant concerne l'installtion de mon app et pas celle du driver

Alors on fera une recherche sur son moteur de recherche favori pour tomber sur [un post de stackoverflow](https://stackoverflow.com/questions/11618898/pg-config-executable-not-found) qui nous explique qu'il "suffit" d'installer le package python-devel ... 

Seulement quand le package est déjà là-bas, alors ne reste plus qu'une solution ... altéré le PATH ... 

Encore faut-il trouver où est planquée postgresql avec l'installation pas "ordinaire" resultante de la doc ci dessus

Comme chuis une trume pour mémoriser les noms de packages à rallonge de centos, je fais un :

```shell
(foxmask)foxmask@localhost:~/icibase $ ps aux|grep post
postgres  2274  0.0  0.1 324636 14452 ?        S    08:39   0:00 /usr/pgsql-9.4/bin/postmaster -D /var/lib/pgsql/9.4/data
```
donc plus qu'à faire un petit export PATH

```shell
(foxmask)foxmask@localhost:~/icibase $ export PATH=/usr/pgsql-9.4/bin/:$PATH
```

puis ENFIN, de relancer l'installation du driver,

```shell
(foxmask)foxmask@localhost:~/icibase $ pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.6.1.tar.gz
Building wheels for collected packages: psycopg2
  Running setup.py bdist_wheel for psycopg2
  Stored in directory: /home/ekip/.cache/pip/wheels/e2/9a/5e/7b620848bbc7cfb9084aafea077be11618c2b5067bd532f329
Successfully built psycopg2
Installing collected packages: psycopg2
Successfully installed psycopg2-2.6.1
```

and Voilà ! :)

