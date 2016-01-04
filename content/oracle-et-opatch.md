Title: Oracle et Opatch
Date: 2013-03-07 10:00
Author: foxmask
Category: Techno
Tags: oracle
Slug: oracle-et-opatch
Status: published

A une époque, patcher Oracle était un sinécure :P

Depuis avec OPatch c'est on ne peut plus simple !

On récupère un patch chez Oracle, on le décompresse, on tape opatch
apply et hop !

Donc après la décompression, ça donne :

```shell
cd path_ou_on_a_decompresse_le_path
```

application du patch oracle

```shell
opatch apply
```

Si vous rencontrez un erreur du genre :

```shell
OPatch cannot find a valid oraInst.loc file to locate Central Inventory.
```

Alors taper la commande suivante :

```shell
opatch apply -invPtrLoc /u01/app/oracle/product/11.2.0.1.0/db/oraInst.loc
```

le paramètre invPtrLoc indique à opatch, où se trouve le fameux "Central
Inventory"

ce qui donnera par exemple pour le patch 8795792

```shell
Invoking OPatch 11.2.0.1.6

Oracle Interim Patch Installer version 11.2.0.1.6
Copyright (c) 2011, Oracle Corporation.  All rights reserved.

Oracle Home       : /u01/app/oracle/product/11.2.0.1.0/db
Central Inventory : /u01/app/oracle/product/11.2.0.1.0/inventory
   from           : /u01/app/oracle/product/11.2.0.1.0/db/oraInst.loc
OPatch version    : 11.2.0.1.6
OUI version       : 11.2.0.1.0
Log file location : /u01/app/oracle/product/11.2.0.1.0/db/cfgtoollogs/opatch/opatch2011-07-29_15-37-22PM.log

Applying interim patch '8795792' to OH '/u01/app/oracle/product/11.2.0.1.0/db'
Verifying environment and performing prerequisite checks...

Voulez-vous continuer ? [y|n]
User Responded with: Y
All checks passed.
Entrez votre adresse électronique pour être informé des problèmes de sécurité,
installer et lancer Oracle Configuration Manager. Le processus est plus simple
pour vous si vous utilisez votre adresse électronique/nom utilisateur My
Oracle Support. Pour plus de détails, consultez la page
http://www.oracle.com/support/policies.html.
Adresse électronique/nom utilisateur : you@yourcompany.com
Indiquez votre mot de passe My Oracle Support pour recevoir les mises à jour de sécurité via votre compte My Oracle Support.
Mot de passe (facultatif) :           
Backing up files...

Application d'un patch au composant oracle.rdbms, 11.2.0.1.0...
Patch 8795792 successfully applied
Log file location: /u01/app/oracle/product/11.2.0.1.0/db/cfgtoollogs/opatch/opatch2011-07-29_15-37-22PM.log

OPatch succeeded.
```

Une fois fait, relancer la base Oracle que vous aurez bien évidemment
stoppée avant de commencer, je ne vous l'avais pas dit ? ba il faut tout
lire avant de commencer ;)

