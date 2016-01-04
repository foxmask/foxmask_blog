Title: Oracle Trouver les tablespaces utilisés par un schéma
Date: 2013-02-14 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-trouver-les-tablespaces-utilises-par-un-schema
Status: published

Tout comme Roméo a sa Juliette, une base Oracle possède son tablespace
;)

Donc pour trouver ce(s) dernier(s) tout se résume à interroger la table
dba\_segment dont le tablespace\_name ne contient aucun de ceux des TB
"system".

```sql
SET linesize 300
SET pagesize 20
SET feedback off
 
SELECT sysdate, a.owner username, a.tablespace_name, round(b.total_space/1024/1024,2) "Total (MB)", round(SUM(a.bytes)/1024/1024,2) "Used (MB)", round(SUM(a.bytes/b.total_space)*100,2) "% Used"
FROM dba_segments a, (SELECT tablespace_name, SUM(bytes) total_space
                      FROM dba_data_files
                      GROUP BY tablespace_name) b
WHERE a.tablespace_name NOT IN ('SYSAUX', 'SYSTEM', 'UNDOTBS1', 'UNDOTBS2')
AND a.tablespace_name = b.tablespace_name
GROUP BY a.tablespace_name, a.owner, b.total_space/1024/1024
ORDER BY a.tablespace_name, a.owner;
```

Ceci permet ensuite d'interroger dba\_data\_files pour trouver les noms
de fichiers qui constituent le Tablespace cherché pour l'agrandir par
exemple.

