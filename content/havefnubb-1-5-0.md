Title: HaveFnuBB 1.5.0
Date: 2012-04-02 09:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, HaveFnuBB, Jelix
Slug: havefnubb-1-5-0
Status: published

cette nouvelle version, 1 an après la précédente quasiment jour pour
jour,  
est marquée par de nombreuses corrections de bugs et d'importantes
améliorations de performances.

**Corrections**

*modules* :

-   havefnubb: moult petites corrections
-   moduleinfos : affiche à présent les infos des modules correctement
-   hfnurates : correction de la soumission des données ajax quand
    l'utilisateur n'est pas connecté

*fonctionnalités* :

-   le désabonnement n'était pas possible.
-   après l'abonnement à une discussion, on ne retournait pas à la page
    d'où on venait
-   suppression de la gestion des caches des zones des utilisateurs ne
    permettant pas l'affichage exact de leur information
-   dans le mail avertissant qu'un nouveau message auquel on est abonné
    contenait un le lien erroné menant à une page 404
-   disparition des Tags sur les discussions corrigée

**Améliorations** :

*installation*

-   l'installation du forum a été simplifiée pour fournir les
    informations "à propos",
-   affichage des informations de la version existante et celle à
    installer
-   l'installation de mise à jour / migration a été revue

*forum*

-   le recomptage des messages que l'on bouge d'un forum à l'autre a été
    améliorée
-   gestion des flux Atom
-   Ajout de meta keyword dans la configuration du forum
-   Gestion de la messagerie privée

*Performances* :

-   le Thème principal ne repose à présent plus sur le système de grille
    960gs dans un soucis de performance et d'amélioration de la rapidité
    du rendu, les autres thèmes restent inchangés et toujours basés sur
    960gs
-   le forum a été allégé dans la gestion de ses tables afin d'éliminer
    le maximum d'intermédiaires pour obtenir des informations simples et
    les restituer le plus vite possible. Ainsi la quantité de requêtes
    SQL a chuté drastiquement de même que les appels inutiles à des
    templates et zones. Par conséquent si vous aviez produit des thèmes,
    il faudra revoir le templae index.tpl pour y retirer l'appel d'une
    zone et la remplacer par une simple ligne HTML. (cf le index.tpl du
    thème par défaut pour plus d'infos).

**Installation de HaveFnuBB**

[Télécharger la version
1.5.0](http://www.havefnubb.org/downloads/downloads_files/havefnubb-1-5-0)

Une fois fait, au choix vous pouvez utilisez :

<ul>
<li>
le Wizard via l'interface web

</li>
-   pour une première installation rendez vous sur
    http://localhost/install.php
-   pour une mise à jour depuis une version 1.4.x, rendez vous sur
    http://localhost/update.php

<li>
La ligne de commandes

</li>
-   Pour l'installation :  
    `php lib/jelix-scripts/jelix.php --havefnubb installapp `
-   Pour la mise à jour  
    `php lib/jelix-scripts/jelix.php --havefnubb installapp `  
    Ah ba oui c'est bien la même commande ! ne vous avais je pas dit
    que Jelix était fun ? ;)

</ul>
Have Fnu !

