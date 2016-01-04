Title: Oracle et taille de schema, tablespace
Date: 2012-01-10 12:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-et-taille-de-schema-tablespace
Status: published

Pour obtenir la taille d'un schéma, avec son script
**size\_of\_schema.sql**

```sql
SELECT SUM(bytes)/1024/1024 FROM dba_segments WHERE owner='&1';
```

à l'invite, donnez lui le nom du schema et roule ;)

Pour obtenir le paramètre de la base "Undo Retention", avec son script
**undo\_retention.sql**

```sql
SELECT name,VALUE FROM v$parameter WHERE name='undo_retention';
```

On tape sur la vue v\$parameter qui contient une bonne partie des
paramètres de votre base oracle que vous avez dans l'init.ora

Taille du tablespace Undo avec son petit script **undo\_tablespace.sql**

```sql
SELECT (bytes/1024/1024/1024),FILE_NAME FROM dba_data_files WHERE tablespace_name='UNDO';
```

le tablespace UNDO et le paramètre Undo retention permettent la gestion
des rollback.  
l'undo retention est definie en minute, la duree pendant laquelle on
conserve une requête de rollback  
et l'undo tablespace lui gère les données qu'on annule.

Si l'un des 2 est trop petit, les rollback vont exploser.

