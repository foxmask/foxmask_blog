Title: Oracle bottant le train des réfractaires
Date: 2012-12-13 11:08
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-bottant-le-train-des-refractaires
Status: published

Voici le début d'une suite de billets dédiée à Oracle, One of my Job in
Professional life :)

Il était une fois un DBA qui en avait plein les bottes de demander aux
utilisateurs de bien vouloir se déconnecter du schéma pour remonter un
dump ... à leur demande de surcroit.

Ainsi donc il dégaina une requête pour leur envoyer un bon coup de pompe
dans le derrière.

Pour trouver la/les connexions existantes sur un schéma oracle on fait :

```sql
SELECT sid,serial#,osuser,status from v$session where username='&1';
```

et on indique le nom du schéma voulu.

Quand on a une session on peut encore se faire "à la main" le fameux :

```sql
alter system kill session ',';
```

Mais quand vous avez une ribambelle de têtes de mule, il faut employer
les grands moyens, et là, se faire la paire de kill à la main devient
pénible et on maudit encore plus ces utilisateurs.

Donc on produit un script SQL, nommons le **generate-kill.sql**, qui va
produire un "rapport" redirigeant les fautifs dans un script SQL qu'on
lancera ensuite.

```sql
set head off
spool kill_session.sql
select 'alter system kill session '''||sid||','||serial#||''';' from v$session where username = '&1';
spool off
exit
```

On se connecte en tant que sysdba et on tape

```sql
@kill_session.sql
```

bye bye :

```sql
System altered.

System altered.

System altered.

System altered.

System altered.

System altered.

System altered.

System altered.

System altered.

System altered.

System altered.
```

Et on peut enfin faire son **drop user/create user** pépère pour
remonter le dump .

