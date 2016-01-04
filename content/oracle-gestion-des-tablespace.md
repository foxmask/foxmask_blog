Title: Oracle Gestion des Tablespaces
Date: 2013-01-10 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-gestion-des-tablespace
Status: published

Quand on n'a pas demandé à Oracle de gérer l'espace disque avec l'option
auto extend sur ses tablespaces, il arrive (souvant) qu'on se mange des
erreurs parce que le tablespace est full.

Donc ;

Pour lister ses tablespace on tapera :

```sql
SELECT file_name FROM dba_data_files WHERE tablespace_name='MONBEAUTBSPC';
```

affichera

```sql
FILE_NAME
--------------------------------------------------------------------------------
/u02/oradata/INSTANCE/data01.dbf
/u02/oradata/INSTANCE/data02.dbf
...
```

Pour le tablespace temporaire on fait :

```sql
SELECT tablespace_name, file_name, bytes FROM dba_temp_files WHERE tablespace_name = 'TEMP';
```

Trouver la taille restant dans le tablespace

```sql
SELECT SUM(bytes)/1024/1024 AS Mo FROM dba_free_space WHERE tablespace_name='MONBEAUTBSPC';
        MO
----------
  5205.625
```

Si on constate que la taille n'est pas suffisante, pour les agrandir on
fera,

pour le tablespace MONBEAUTBSPC :

```sql
alter tablespace MONBEAUTBSPC add datafile '/u02/oradata/INSTANCE/data03.dbf' size 30720M;
```

pour le tablespace TEMP :

```sql
ALTER TABLESPACE temp ADD TEMPFILE '/u02/oradata/INSTANCE/temp02.dbf' SIZE 512m;
```
