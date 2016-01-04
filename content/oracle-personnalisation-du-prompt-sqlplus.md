Title: Oracle Personnalisation du Prompt SQL*Plus
Date: 2012-12-20 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-personnalisation-du-prompt-sqlplus
Status: published

Tout comme un admin système adore faire joujou en personnalisant son
prompt de son shell chéri en rajoutant le nom du host et l'heure, on
peut tout aussi bien le faire avec SQL\*Plus afin de savoir sur quelle
Instance Oracle on s'est connecté et avec quel Utilisateur et à quelle
heure.

Pour ce faire, on editera le fichier
\$ORACLE\_HOME/sqlplus/admin/glogin.sql pour ajouter :

    set sqlprompt "_user 'on' _date 'at' _connect_identifier > "

ce qui permettra d'afficher :

    -bash-3.2$ sqlplus /nolog

    SQL*Plus: Release 10.2.0.4.0 - Production on Tue Jan 19 14:42:05 2010

    Copyright (c) 1982, 2007, Oracle.  All Rights Reserved.

     on 19-Jan-11 at  > conn /as sysdba
    Connected.
    SYS on 19-Jan-11 at INSTANCE > 
