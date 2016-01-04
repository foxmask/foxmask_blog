Title: Importer un dump Oracle sans l'exporter physiquement avant
Date: 2014-07-02 15:13
Author: foxmask
Category: Techno
Tags: oracle
Slug: importer-un-dump-oracle-sans-lexporter-physiquement-avant
Status: published

Donc s'il vous arrive (comme bibi) d'être short en place disque pour
faire vos backups oracle pour ensuite importer le(s) schéma(s), une
solution ultime subsiste, quand même, pour nous autre "pauvres" petits
"exportateurs" de données :P

Comment ça ?  
La subtilité réside dans la possibilité d'Oracle à importer les données
dans le schéma cible, via un
[DBLink](http://fr.wikipedia.org/wiki/DBLink " un DBLink, ou database link est un objet d'une base de données permettant d'exécuter des requêtes sur une autre base de données, qu'elle se trouve physiquement sur la même machine ou qu'elle soit distante.").

Pas croyable hein ?

let's voyons this right maintenant:

Creation du DBLink sur le serveur "cible" :

```sql
CREATE DATABASE LINK chicago 
   CONNECT TO admin1 IDENTIFIED BY windy
   USING 'CHI';
```

Ici, le nom du schema "source" est **admin1**, le nom du DBLink chicago.

Ensuite vient l'import lui même sur le serveur "cible"

```sql
impdp admin2/market TABLES=customers,sales DIRECTORY=dpump1
  NETWORK_LINK=chicago
```

ici l'import (la commande impdp) demande à oracle de se connecter avec
le user admin2, d'importer 2 tables, provenant du schéma se cachant
derrière le DBLink "chicago"

Oracle exportera donc admin1, **sans stocker le dump dans un fichier
physique**, depuis le serveur nommé "CHI" (ou l'alias qui est défini
dans le tnsnames.ora de votre serveur oracle), puis l'importera
localement dans le schema admin2 et le tour est joué ;)

L'intéret est que je n'aurai pas à exporter mes centaines de giga sur un
serveur sans place disque (ou pas assez) pour stocker le dump puis le
transferer sur le serveur cible et l'importer. Là, tout se fait d'une
traite.

Si on a plusieurs schémas, il faut que le user du dblink ait les droits
d'y accéder sur la source.  
Si c'est le cas, ensuite on peut faire :

```sql
impdp admin2/market SCHEMAS=schema1,schema2 
  REMAP_SCHEMA=schema1:mon_nouveau_schema1,schema2:mon_nouveau_schema2 
  DIRECTORY=dpump1
  NETWORK_LINK=chicago
```

et roule ma poule

