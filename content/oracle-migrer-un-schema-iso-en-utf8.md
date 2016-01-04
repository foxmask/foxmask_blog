Title: Oracle Migrer un schéma ISO en UTF8
Date: 2013-03-14 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-migrer-un-schema-iso-en-utf8
Status: published

Vous avez sous la main un dump en ISO et vous souhaitez l'importer en
UTF8, tout un programme !

La marche à suivre est la suivante :

1.  On importe le dump dans un schéma d'une base en ISO
2.  On exécutera un script byte\_to\_char.sql pour que le schéma prenne
    en compte l'UTF8
3.  On exportera le schéma en UTF8
4.  On importera le dump en UTF8 dans une base UTF8

**Import du dump**  
je vous laisse avec l'étape une, basique à souhait ;)

**Exécution du script byte\_to\_char.sql**

```sql
BEGIN
FOR i IN (SELECT
utc.TABLE_NAME,utc.column_name,utc.data_length,utc.data_type
FROM user_tab_cols utc, user_tables ut
WHERE ut.TABLE_NAME = utc.TABLE_NAME
AND utc.data_type IN ('VARCHAR2','CHAR')
AND char_used= 'B'
AND column_name NOT LIKE 'SYS_%')
loop
EXECUTE immediate 'alter table '||i.TABLE_NAME||' modify (
'||i.column_name||' '||i.DATA_TYPE||'('||i.data_length||' CHAR) )';
END loop;
END;
/
```

Ainsi, à l'issu de son exécution vos colonnes bytes seront en char ce
qui permettra lors de l'import, de prendre en compte les caractères
accentués sur plus d'un byte.

**Export du schéma en UTF8**

```shell
mknode pipeExp p
export NLS_LANG=AMERICAN_AMERICA.UTF8
gzip MY_UTF8.dmp.gz
nohup exp userid=LOGIN/PASS file=pipeExp grants=n &
```

l'important ici est la variable d'environnement NLS\_LANG à positionner
à AMERICAN\_AMERICA.UTF8

**Import du dump en UTF-8**  
idem ci dessus, c'est simple à souhait ;)

