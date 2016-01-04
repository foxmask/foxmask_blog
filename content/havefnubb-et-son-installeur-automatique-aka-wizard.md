Title: HaveFnuBB! et son installeur automatique aka wizard
Date: 2009-09-01 01:00
Author: foxmask
Category: Techno
Tags: HaveFnuBB, Jelix
Slug: havefnubb-et-son-installeur-automatique-aka-wizard
Status: published

[Dans un précédent billet](/post/2009/08/24/Le-mardi-c-est-jelix) vous
m'aviez demandé de vous présenter l'installeur de mon forum HaveFnuBB!

Voici donc le *Système d'installation d'HaveFnuBB!* :

Le système d'installation se compose des étapes suivantes :

1.  ) Vérifications des pré-requis système
2.  ) Configuration du Forum
3.  ) Configuration de la Base de données
4.  ) Installation de la Base de données
5.  ) Création du compte Administrateur
6.  ) Fin

  
**INSTALLATION** :  
  
  
Techniquement les étapes consistent en :

-   Un seul contrôleur, 4 forms (\*.forms.xml), 3 fichiers de config
    (\*.ini.php)

entre parenthèses, se trouve le nom de la méthode du contrôleur
"default" du module "hfnuinstall"

**Etape 1** (*check*) - Vérifications :

-   version\_compare(phpversion(),'5.0','\>=')
-   function\_exists('mysql\_connect')

  
**Etape 2** (*config*) - Nom, description, langue et thème principaux,
etc...

-   lecture/écriture du fichier de config defaultconfig.ini.php
-   lecture/écriture du fichier de config havefnu.ini.php

  
**Etape 3** (*dbconfig*) - Info sur les noms: du serveur, de la base,
de l'utilisateur de la base et son mot de passe

-   lecture/écriture du fichier de config dbprofils.ini.php

  
**Etape 4** (*installdb*) - exécution du script install.mysql.sql

-   la structure de chaque module possède un dossier install/ ,
    renfermant à son tour
    -   sql/install.**driver**.sql
    -   update/**version**/install.**driver**.sql

  
**Etape 5** (*adminaccount*) - Infos admin :

-   lecture/ecriture du fichier de config havefnu.ini.php
-   appels des méthodes "core" de Jelix pour créer un utilisateur

  
**Etape 6** (*end*) - Message de fin ;)

  
**MISE A JOUR** :  
  
  
La système de mise à jour, se charge :

-   au minimum de mettre la version à jour dans havefnu.ini.php (le
    fichier de config principal du forum)
-   sinon s'occupe de mettre à jour d'autres fichiers de configuration,
    et exécuter les scripts SQL.

A chaque étape, l'installeur vérifie si la version actuelle est
différente et enchaine les étapes sinon s'arrête.

-   puis fini par vider le cache

  
Bien évidement, on ne peut pas exécuter 2 fois de suite l'installation,
puisque la vérification de la version est toujours faite.  

**EPILOGUE** :  
  
  
Si vous accédez à la racine de votre forum et qu'il n'est pas installé,
Jelix routera l'utilisateur directement sur l'installeur.  
Ceci se fait grâce à l'intervention du plugin Coordinateur (qui pourra
faire l'objet d'un autre article) vérifiant si le forum est installé.  
  
  
Pour plus d'infos je vous invite à consulter [le code
ici](http://forge.jelix.org/projects/havefnubb/browser/trunk/havefnubb/modules/hfnuinstall/controllers/default.classic.php)
ou bien venir en parler [sur le forum lui
même](http://www.havefnubb.org) ;)

**NOTA BENE** :  
L'installeur n'a rien à voir avec la prochaine feature de Jelix,
l'installeur touzazimut, de modules, plugins etc.. ;)

Mais pour en avoir pas mal discuté en Janvier et codé appmgr, réadapter
l'installeur d'HaveFnuBB avec Jelix 1.2 ne me posera aucun problème :P

