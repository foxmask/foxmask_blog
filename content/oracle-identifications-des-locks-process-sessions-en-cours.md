Title: Oracle Identifications des Locks, Process, Sessions en cours
Date: 2013-01-17 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-identifications-des-locks-process-sessions-en-cours
Status: published

Voici une requete SQL dans l'arsenal du DBA, nommons la **locks.sql**,
permettant d'identifier les locks en cours sur un schema oracle :

```sql
SELECT   /*+ choose */
          bs.username "Blocking User",
          bs.username "DB User",
          ws.username "Waiting User",
          bs.sid "SID",
          ws.sid "WSID",
          bs.sql_address "address",
          bs.sql_hash_value "Sql hash",
          bs.program "Blocking App",
          ws.program "Waiting App",
          bs.machine "Blocking Machine",
          ws.machine "Waiting Machine",
          bs.osuser "Blocking OS User",
          ws.osuser "Waiting OS User",
          bs.serial# "Serial#",
          DECODE (
             wk.TYPE,
             'MR', 'Media Recovery',
             'RT', 'Redo Thread',
             'UN', 'USER Name',
             'TX', 'Transaction',
             'TM', 'DML',
             'UL', 'PL/SQL USER LOCK',
             'DX', 'Distributed Xaction',
             'CF', 'Control FILE',
             'IS', 'Instance State',
             'FS', 'FILE SET',
             'IR', 'Instance Recovery',
             'ST', 'Disk SPACE Transaction',
             'TS', 'Temp Segment',
             'IV', 'Library Cache Invalidation',
             'LS', 'LOG START OR Switch',
             'RW', 'ROW Wait',
             'SQ', 'Sequence Number',
             'TE', 'Extend TABLE',
             'TT', 'Temp TABLE',
             wk.TYPE
          ) lock_type,
          DECODE (
             hk.lmode,
             0, 'None',
             1, 'NULL',
             2, 'ROW-S (SS)',
             3, 'ROW-X (SX)',
             4, 'SHARE',
             5, 'S/ROW-X (SSX)',
             6, 'EXCLUSIVE',
             TO_CHAR (hk.lmode)
          ) mode_held,
          DECODE (
             wk.request,
             0, 'None',
             1, 'NULL',
             2, 'ROW-S (SS)',
             3, 'ROW-X (SX)',
             4, 'SHARE',
             5, 'S/ROW-X (SSX)',
             6, 'EXCLUSIVE',
             TO_CHAR (wk.request)
          ) mode_requested,
        object_name ,
          TO_CHAR (hk.id1) lock_id1,
          TO_CHAR (hk.id2) lock_id2
FROM     v$lock hk, v$session bs, v$lock wk, v$session ws ,
V$LOCKED_OBJECT a ,
dba_objects b
WHERE    hk.BLOCK = 1
AND      hk.lmode != 0
AND      hk.lmode != 1
AND      wk.request != 0
AND      wk.TYPE(+) = hk.TYPE
AND      wk.id1(+) = hk.id1
AND      wk.id2(+) = hk.id2
AND      hk.sid = bs.sid(+)
AND      wk.sid = ws.sid(+)
AND      a.object_id=b.object_id
AND      HK.sid=a.SESSION_ID
ORDER BY 1;
```

Oui hein ! ça s'invente pas ;)

Une seconde **current\_request.sql** vous donnant les requêtes en cours
:

Avec Oracle 9i :

```sql
SELECT sesion.sid,
       sesion.username,
       optimizer_mode,
       hash_value,
       address,
       cpu_time,
       elapsed_time,
       sql_text
  FROM v$sqlarea sqlarea, v$session sesion
 WHERE sesion.sql_hash_value = sqlarea.hash_value
   AND sesion.sql_address    = sqlarea.address
   AND sesion.username IS NOT NULL
```

*Mais ca c'était avant*

Ci dessous la même en "encore plus longue" pour les versions oracle \>
9i

```sql
SELECT sql_text, STATUS FROM v$session, v$sqlarea WHERE v$session.sql_id=v$sqlarea.sql_id;
```

Ah oui ça tranche hein !

Pour avoir la liste des sessions en cours un petit script
**session.sql** :

```sql
SET echo off;
SET termout ON;
SET linesize 180;
SET pagesize 60;
SET newpage 0;
 
SELECT
   rpad(c.name||':',11)||rpad(' current logons='||
   (to_number(b.sessions_current)),20)||'cumulative logons='||
   rpad(substr(a.VALUE,1,10),10)||'highwater mark='||
   b.sessions_highwater Information
FROM
   v$sysstat a,
   v$license b,
   v$database c
WHERE
   a.name = 'logons cumulative'
;
 
ttitle "dbname Database|UNIX/Oracle Sessions";
 
SET heading off;
SELECT 'Sessions on database '||substr(name,1,8) FROM v$database;
SET heading ON;
SELECT
       substr(a.spid,1,15) pid,
       substr(b.sid,1,15) sid,
       substr(b.serial#,1,15) ser#,
       substr(b.machine,1,16) box,
       substr(b.username,1,50) username,
--       b.server,
       substr(b.osuser,1,28) os_user,
       substr(b.program,1,60) program
FROM v$session b, v$process a
 WHERE
b.paddr = a.addr
AND TYPE='USER'
ORDER BY spid;
ttitle off;
spool off;
```

Pour obtenir les requêtes en cours d'annulation (rollback),
**session\_undo.sql** :

```sql
COLUMN username FORMAT A15
 
SELECT s.username,
       s.sid,
       s.serial#,
       t.used_ublk,
       t.used_urec,
       rs.segment_name,
       r.rssize,
       r.STATUS
FROM   v$transaction t,
       v$session s,
       v$rollstat r,
       dba_rollback_segs rs
WHERE  s.saddr = t.ses_addr
AND    t.xidusn = r.usn
AND    rs.segment_id = t.xidusn
ORDER BY t.used_ublk DESC;
```

Voilà, ça sera tout pour aujourd'hui

