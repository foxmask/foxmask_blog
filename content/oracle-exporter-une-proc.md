Title: Oracle Exporter une Proc 
Date: 2013-01-03 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-exporter-une-proc
Status: published

Le script suivant, nommons le export\_pkg, vous permet d'exporter une
proc de votre choix :

    SET heading off
    SET pagesize 0
    SET linesize 255
    SET trimspool ON
    SET feedback off
    SET verify off
     
     
    spool &&1\.pkg
    SELECT 'CREATE OR REPLACE ' FROM dual;
    SELECT TEXT FROM user_source WHERE TYPE='PACKAGE' AND NAME= '&&1' ORDER BY line ASC;
    SELECT '/ ' FROM dual;
    SELECT ' ' FROM dual;
    SELECT 'CREATE OR REPLACE ' FROM dual;
    SELECT TEXT FROM user_source WHERE TYPE='PACKAGE BODY' AND NAME= '&&1' ORDER BY line ASC;
    SELECT '/ ' FROM dual;
    SELECT 'exit; ' FROM dual;
    spool off;
    exit;

Il s'utilise ainsi :

sqlplus login/pass @export\_pgk.sql TOTO

et vous créera TOTO.pkg avec le contenu de la proc contenu dans le
schema "login"

