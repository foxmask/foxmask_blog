Title: Jelix et le module jCommunity
Date: 2009-09-15 07:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, Jelix
Slug: jelix-le-module-jcommunity-2
Status: published

En PHP, si une classe ou API existante vous plait mais que vous
souhaitez y apporter votre touche personnelle vous inclurez cette
dernière et la surchargerez pour éviter d'y toucher.

Exactement le même principe s'applique avec les modules Jelix. On
parlera alors "d'overload".

Un module n'étant pas une simple classe (mais composé de contrôleurs,
daos, forms, template, zones, classes, fichiers de traductions) tout ne
peut-être surchargé.

*Qu'est ce qui peut faire l'objet d'overload* ?

-   Les templates : pour modifier le rendu
-   les Dao : pour ajouter des propriétés (des colonnes/ tables ) et des
    factories (méthodes d'accès aux tables)
-   les forms : pour ajouter des champs de formulaires et leurs règles
    de contrôle associées
-   les locales : fichiers de traductions

*Avantages de l'"Overload"* :

-   **Extension des fonctionnalités** du module original
-   **Adaptabilité de tous les aspects du module** (exception faite du
    contrôleur)
-   **Facilité de mise à jour du module originel**, puisqu'on ne change
    aucune ligne de code de ce dernier

<!--more-->

Ainsi prenons comme exemple concret le module Jelix, jCommunity, et
voyons ce que l'on peut en tirer.

**Présentation** :

**jCommunity est le module de gestion des utilisateurs pour tout type de
site web**.  
Il inclut une gestion complète du workflow de :

-   Inscription/désincsription
-   Connexion/déconnexion

1\) **Overload des templates** :

**Question** :  
Ok c'est cool mais je veux adapter le rendu des templates de jCommunity
aux thèmes de mon site. comment faire ?

**Réponse**  
Par défaut le nom du thème se nomme default. Ainsi donc pour surcharger
un template on placera tout simplement la version modifiée de ce dernier
dans le dossier var/themes/default/jcommunity

Ainsi quand Jelix appellera le template du module, il ira voir d'abord
si une version existe dans le dossier des thèmes et l'utilisera.

**Comparer** : le template de la page de consultation d'un membre :

-   [jcommunity](http://forge.jelix.org/projects/jcommunity/browser/trunk/modules/jcommunity/templates/fr_FR/account_show.tpl)
    (l'originale)
-   [havefnubb](http://forge.jelix.org/projects/havefnubb/browser/trunk/havefnubb/var/themes/default/jcommunity/account_show.tpl)
    (l'overload)

2\) **Overload de Dao** :

**Question**  
La table jCommunity ne contient pas assez d'informations pour gérer mes
utilisateurs, comment "étendre" celle-ci ?  
**Réponse**  
Copions la Dao jcommunity/dao/user.dao.xml dans le dossier
var/overload/jcommunity/daos  
Changeons à l'intérieur tout ce dont on a besoin :

-   nom de la table et des nouvelles colonnes. Nouvelles méthodes Dao
    etc.
-   Comme précédemment Jelix ira voir d'abord si une Dao existe dans ce
    dossier.

tout cela en respectant à minima le nom des méthodes existantes dans la
DAO d'origine.

**Comparer** : la Dao account.dao.xml :

-   [jcommunity](http://forge.jelix.org/projects/jcommunity/browser/trunk/modules/jcommunity/daos/user.dao.xml)
    (l'originale)
-   [havefnubb](http://forge.jelix.org/projects/havefnubb/browser/trunk/havefnubb/var/overloads/jcommunity/daos/user.dao.xml)
    (l'overloaded)

3\) **Overload de forms** :

**Question** :  
Le formulaire gérant les données des utilisateurs est trop léger à
votre goût ?  
**Réponse** :  
Qu'à cela ne tienne on crée une copie du forms
jcommunity/forms/account.form.xml dans le dossier
var/overload/jcommunity/forms  
Ensuite on y rajoute les champs qu'il nous sied de voir afficher
(correspondant à notre DAO modifiée).  
Comme précédemment Jelix ira voir d'abord si un forms existe dans ce
dossier.

**Comparer** : le Forms account.forms.xml :

-   [jcommunity](http://forge.jelix.org/projects/jcommunity/browser/trunk/modules/jcommunity/forms/account.form.xml)
    (l'originale)
-   [havefnubb](http://forge.jelix.org/projects/havefnubb/browser/trunk/havefnubb/var/overloads/jcommunity/forms/account.form.xml)
    (l'overloaded)

4\) **Extension fonctionnelle du module**  
Ok tout fonctionne nickel  
On a pu tout surcharger comme souhaité  
Subsiste un dernier détail, après la surcharge de la couche de
présentation,  
on a besoin d'**étendre la couche fonctionnelle**.  
Et cela est rendu **possible grâce aux events Jelix**.

Par exemple, lors de l'inscription d'un membre, je souhaite vérifier que
celui ci n'est pas banni du site.  
Pour cela jCommunity, génère un événement
`jcommunity_registration_prepare_save`, envoyé juste avant
l'enregistrement de l'e-mail du membre.  
En répondant à cet événement (via un listener) on est en mesure de
procéder à cette vérification puis retourner au module jCommunty la
réponse, positive ou non.

([petit rappel sur les Events Jelix dans un billet
précédant](/post/2009/08/18/Jelix-et-la-Communication-inter-modules) )

5\) **Conclusion** :  
Ainsi, lors de l'appel à jCommunity, et grâce aux divers orverload, ce
sont bien vos propres ressources qui sont utilisées, tout en exploitant
pleinement le core/workflow de jCommunity.

