Title: Oracle des expdp et impdp en réseau, si c'est possible
Date: 2013-01-16 16:49
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-des-expdp-et-impdp-en-reseau-si-cest-possible
Status: published

A l'heure actuelle, la version d'Oracle est la 11G R2 (à tes souhaits
pourrait rétorqué 6P0 à R2D2 :P), et avec cette version il est de
coutume de ne plus employer pour ses sauvegardes/gestions de dumps, que
le fameux duo expdp et impdp pour produire ce qu'on appelle des
datapumps (à tes souhaits encore ;)

Tout ceci rend la gestion des dumps beaucoup plus funs qu'avec les
commandes exp/imp qu'on se trainaient depuis Oracle 8i&9i.

Par contre un inconvénient majeur pour tout radin qui se respecte, ca
bouffe l'espace disque !

**Avant expdp / impdp**

avec "exp", on pouvait compresser ses dumps like that :

```shell
mknod pipe p
gzip < pipe > FOX_DUMP.gz  &
nohup exp LOGIN/PASS file=pipe grants=n &
```

j'exporte mon dump dans le pipe qui le compresse à la volée, magie magie
;) Qui dit mieux ? ben pas oracle 11G :P

je vous note la même chose à l'envers pour un import avec imp

```shell
mknod pipe p
gunzip < FOX_DUMP.gz > pipe  &
nohup imp LOGIN/PASS file=pipe grants=n ignore=y fromuser=OLDLOGIN touser=LOGIN &
```

Bon ok on a pige la compression / décompression à la volée.

A présent supposons que j'ai vraiment des soucis de place disque, même
pour produire le dump compressé localement à mon serveur oracle.

On procédait ainsi : depuis une autre machine disposant des outils
oracle (il faut un minimum hein;)

```shell
mknod pipe p
gunzip < FOX_DUMP.gz > pipe  &
nohup imp LOGIN/PASS@FOX-SERV file=pipe grants=n ignore=y fromuser=OLDLOGIN touser=LOGIN &
```

Ici la subtilité réside dans ce qui suit le @ ; ceci demande à oracle
"vas voir dans le fichier tnsnames.ora et trouves moi la référence
FOX-SERV, puis quand tu l'as trouvé connectes-toi au serveur concerné".

Ceci marche aussi bien localement (pour invoquer une instance Oracle
local, l'ORACLE\_SID quoi) qu'en réseau car le tnsnames.ora contient
tout ce qu'il faut pour trouver le serveur, le port d'écoute et
l'instance

exemple :

```sql
FOX-SERVER = (DESCRIPTION =
            (ADDRESS_LIST =
                (ADDRESS = (PROTOCOL = TCP)(HOST = fox.somewhere.other.the.rainbow)(PORT = 1523))
            )
            (CONNECT_DATA =
                (SID = V11UTF8)
            )
    )   
```

Ainsi, il m'etait facile de balancer un dump à trifouilli-les-oies avec
exp :P

**Depuis expdp et impdp**  
Ok, super on a vu comment on gérait *avant*, à présent comment fait-on
?

Depuis l'arrivée du duo (ex|im)pdp, on ne peut plus :

-   compresser les dumps à la volée
-   exploiter le dernier cas précédemment évoqué, car la commande prend
    des arguments qui demandent à Oracle de vérifier "localement" ses
    ressources.
-   bon ya aussi plein d'autres trucs qu'on peut plus faire mais
    <abbr title="on s'en fou">OSEF</abbr> :P c'est pas le sujet du jour
    ;)

Le premier des paramètres oracle "vérifié" localement : **DIRECTORY**

**DIRECTORY** est un *objet oracle* et pas un path qu'on peut indiquer à
oracle à la volée pour lui dire "mon dump est là / est à mettre là", nan
nan ça ça marche plus !

Le directory oracle est donc localisable comme suit :

```sql
SQL> conn /AS sysdba
Connected.
SQL> select * from dba_directories;

OWNER                  DIRECTORY_NAME
------------------------------ ------------------------------
DIRECTORY_PATH
--------------------------------------------------------------------------------
SYS                ORACLE_OCM_CONFIG_DIR
/app/oracle/product/11.2.0.3.0/db/ccr/state

SYS                DATA_PUMP_DIR
/app/oracle/product/11.2.0.3.0/db/rdbms/log/
```

Donc comme on le voit ici, ce sont des dossiers propre à Oracle créés
lors de l'installation.

Mais moi je veux importer / exporter des dumps sur un NAS (allez :P)

Donc pour arriver à mes fins, j'ajoute une ligne dans mon /etc/fstab
pointant sur un des dossiers (qu'on dit "exportés") de mon NAS en NFS,
disons que le dossier sera dans */mnt/dump\_oracle* et je le "mount" (of
course)

Reste alors à ajouter ce dossier à oracle :

```sql
SQL> conn /AS sysdba
Connected.
SQL> create directory fox_dump_oracle as '/mnt/dump_oracle';

Directory created.

SQL>
```

A présent reste à finir ses affaires :

```shell
expdp LOGIN/PASS dumpfile=exp_FOX_SCHEMA.dmp directory=fox_dump_oracle logfile=fox_dump_oracle.log &
```

et là au joie, le dump partira clopin-clopant sur le NAS bouffer
l'espace disque ailleurs ;)

