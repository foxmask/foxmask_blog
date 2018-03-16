Title: Tableau comparatif d'outils de prise de notes partie 2 : Boostnote vs Joplin
Date: 2018-03-15 23:45
Author: foxmask
Tags: Boostnote, Joplin
Category: Techno
Slug: comparatif-editeurs-partie2-boostnote-vs-joplin
Status: published

Dans la [continuité du comparatif d'outils de prise de notes]({filename}/comparatif-editeurs.md), voici 2 editeurs libres utilisant absolument les mêmes techno et archi.
En effet tous deux  : 

* utilisent React Native 
* fournissent un client "lourd" pour le desktop, un client mobile, mais 0 app web
* utilisent le format markdown (enfin le markdown de github pour Boostnote pour etre précis)
* exploitent le stockage "sur le cloud" pour synchroniser ses notes.

Malgré cela ils se distinguent l'un de l'autre facilement.

<table class="table table-hover table-bordered table-striped">
<tr><th></th><th>Boostnote</th><th>Joplin</th></tr>
<tr><td>Stockage</td><td>Dropbox</td><td>One drive (dropbox en cours de portage)</td></tr>
<tr><td>Import Evernote</td><td>ever2boost se nomme l'outil, mais plante</td><td>Oui mais les pdf et docx ne sont pas gérés donc non synchronisés</td></tr>
<tr><td>Cloud</td><td>Pas pu tester le comportement de Dropbox puisque les imports Evernote plantent</td><td>limitation des tailles de fichiers à 4Mo sur Onenote, rend les notes vide de sens, donc ne sont pas synchornisées</td>
<tr><td>Recherche</td><td>Trouve immediatement les notes et surligne le terme rechercher</td><td>Trouve les notes comportant le terme sans les surligner</td></tr>
</table>

## [Boostnote](https://boostnote.io)

hélas, sans matière, sans mes notes migrées de evernote, le tour du proprietaire a été rapide.

Par exemple, il a un manque d'uniformisation entre la version desktop et mobile.

Sur mobile on a l'impression qu'on a perdu ses notes qui sont pourtant synchronisées sur dropbox, la faute au menu qui liste les "stockages" au lieu d'afficher directement leur contenu.
Par ailleurs, au lieu d'afficher le rendu d'une note dans la liste, pour l'heure, on nous affiche le code markdown.... sur une seule ligne...


<img src="/static/editeurs/boostnote.png" title="Editeur de text markdown Boostnote"/>

## [Joplin](http://joplin.cozic.net/)

Autant l'extraction des notes sur mon desktop a été hyper rapide (~25min pour 650Mo de 2500notes), autant la synchronisation de Joplin vers Onedrive est TRES longue

Mes notes ont été decortiquées par Joplin qui a comptabilisé 8500 objets à synchroniser (ce qui prend en compte, les dossiers, tags, tags dans les notes, images dans les notes etc)

J'ai eu 85000 objets synchronisés en 4 soirées (de 19h à 1h du matin + une, ce soir, de 20h à 23h40 ;).

<img src="/static/editeurs/joplin.png" title="Editeur de text markdown Joplin"/>


## Manques :

### Pour les 2 projets :

* Organiser les tag et dossiers en 'arbre' car la liste des dossiers et tags devient très longue et pollue visuellement
* Pas de widget sur mobile ni pour l'un ni pour l'autre. Limitation dû à React Native il semblerait.
* Sur Joplin les tags ne peuvent être créés depuis le mobile, bug lié à React native, donc bug qui impacterait aussi Boostnote

### Pour Boostnote :

* Pas de reminder


## Ce que sait faire l'un mais pas l'autre

### Boostnote 

on peut blogger depuis boostnote sur Wordpress :P

### Joplin 

les notes peuvent être chiffrées intégralement

transformer une note en reminder et inversement


## Conlusion

Ca serait sympa d'avoir un mix des deux, le desktop the Boostnote et la version mobile de Joplin

Boostnote est attrayant visuellement mais Joplin gagne pour moi car j'ai pu recuperer toutes mes notes Evernote, que ca synchronise (même si l'intégralité aura pris beaucoup de temps la première fois)

Il faudrait que je tarabiscote l'auteur de Joplin pour savoir comment je pourrai créer des notes en me passant du mobile et du destkop pour l'integrer à TriggerHappy :)

Le contenu des fichiers markdown est special du coup si je ne mets pas le bon hash dedans, c'est comme si j'avais pissé dans un violon.


PS : Un dernier détail qui ne gate rien, Joplin c'est français :P
