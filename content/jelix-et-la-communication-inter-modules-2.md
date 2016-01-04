Title: Jelix et la Communication inter modules
Date: 2009-08-18 01:05
Author: foxmask
Category: Techno
Tags: Jelix
Slug: jelix-et-la-communication-inter-modules-2
Status: published

Une pépite parmi tant d'autres que renferme Jelix, est la communication
inter module.

Mais qu'est-ce que cela ?

Il arrive que des modules aient besoin de communiquer entre eux  
  
ou qu'ils aient besoin d'informations des uns et des autres.

Imaginons un cas simple, une interface d'administration listant les
modules (articles,wiki,news), présents sur son site favori.

La solution "Jelixienne" consiste à faire communiquer le module
d'administration avec tous les autres.

Le module d'administration va émettre un message et récupérera les
réponses des modules.

**Mise en place** :  
  
je ferai apparaitre ces infos sur une pages dédiées "Liste des
modules".  
  
Cette page sera constituée d'un template et les réponses des modules se
feront à l'aide de zones  
  
(**rappel** : les zones sont des portions de page)

Donc pour cela je défini un contrôleur "modules" avec une action "index"
par défaut :

**le contrôleur**

``` {.php}
class modulesCtrl extends jController {
 
function index() {
$rep = $this->getResponse('html');
$tpl = new jTpl();
$tpl->assign('modules',jEvent::notify('HfnuAboutModule')->getResponse());         $rep->body->assign('MAIN',$tpl->fetch('modules'));
return $rep;
}
}
```

la ligne intéressante ici est :

``` {.php}
$tpl->assign('modules',jEvent::notify('HfnuAboutModule')->getResponse());
```

cette ligne fait 3 choses en même temps :

1.  elle émet un message nommé `HfnuAboutModule`
2.  elle récupère les données du message émis
3.  elle assigne ses données à la variable "modules" du template.

la ligne suivante indique à Jelix, le nom du template "module", qui
affichera les données

``` {.php}
$rep->body->assign('MAIN',$tpl->fetch('modules'));
```

**le template**

``` {.html}
<h1>Liste des modules </h1>
{if count($modules)}
{assign $count = count($modules)}
{for $i=0; $i<$count;$i++}
<div class="two-cols">
<div class="col">
{$modules[$i]}
</div>
</div>
{/for}
{/if}
```

Bon ok on visualise un peu ce qui va se passer "à la fin" mais comment
nos modules "news","wiki","articles" vont ils répondre à l'evenement
`HfnuAboutModule` ?

A tout jEvent::notify, un listener peut répondre, donc nous allons
définir un listener comme suite en 2 temps :

1.  définition d'un fichier events.xml décrivant le nom de l'évènement
    et la classe y répondant, events.xml est donc le "liant"
2.  définition du listener lui-même.

**fichier events.xml**

``` {.xml}
<?xml version="1.0" encoding="iso-8859-1"?>
<events xmlns="http://jelix.org/ns/events/1.0">
<listener name="hfnuadmin">
<event name="HfnuAboutModule" />
</listener>   </events>
```

On retrouve bien ici le nom de l'évènement `HfnuAboutModule` auquel le
listener `hfnuadmin` va se charger de répondre

**le listener**

``` {.php}
class hfnuadminListener extends jEventListener{
 
function onHfnuAboutModule ($event) {
$event->add( jZone::get('hfnuadmin~about',array('modulename'=>'hfnuadmin')) );
}   }
```

lorsque `HfnuAboutModule` est déclenché, alors `onHfnuAboutModule` entre
en oeuvre et répond à l'event (via \$event-\>add())

\$event-\>add() peut recevoir tout type de données. Ici nous lui
retournons une zone ([que nous avons précédemment abordés dans mes 2
précédants
articles](/post/2009/07/15/Cr%C3%A9ation-de-Modules-G%C3%A9n%C3%A9riques-%22Jelix%22-%28partie-2/2%29))
nommée "about"

**la zone**

``` {.php}
class aboutZone extends jZone {
protected $_tplname='zone.about';
 
protected function _prepareTpl(){
$moduleName = $this->param('modulename');
 
if ($moduleName == '') return;
jClasses::inc('havefnubb~modulexml');
$moduleInfo = modulexml::parse($moduleName);                 $this->_tpl->assign('moduleInfo',$moduleInfo);             }
}
```

notre zone ici récupère le paramètre du nom du module, puis parse le
fichier module.xml et affecte le résultat au template zone.about

**le template**

``` {.html}
<h1>{$moduleInfo['name']}</h1>
<dl>
<dt>{@hfnuadmin~hfnuabout.about.version@} :</dt><dd> {$moduleInfo['version']} ({@hfnuadmin~hfnuabout.about.date.create@} {$moduleInfo['dateCreate']})</dd>
<dt>{@hfnuadmin~hfnuabout.about.label@} :</dt><dd> {$moduleInfo['label']|escxml}</dd>
<dt>{@hfnuadmin~hfnuabout.about.desc@} :</dt><dd> {$moduleInfo['desc']}</dd>
<dt>{@hfnuadmin~hfnuabout.about.notes@} :</dt><dd> {$moduleInfo['notes']}</dd>
<dt>{@hfnuadmin~hfnuabout.about.licence@} :</dt><dd> {if $moduleInfo['licenceURL'] != ''}<a href="{$moduleInfo['licenceURL']}">{$moduleInfo['licence']}</a>{else}{$moduleInfo['licence']}{/if}</dd>
<dt>{@hfnuadmin~hfnuabout.about.copyright@} :</dt><dd> {$moduleInfo['copyright']}</dd>
{foreach $moduleInfo['creators'] as $author}
<dt>{@hfnuadmin~hfnuabout.about.authors@} :</dt><dd> {if $author['email'] != ''}<a href="mailto:{$author['email']}">{$author['name']|escxml}{else}{$author['name']|escxml}{/if}</a></dd>
{/foreach}
<dt>{@hfnuadmin~hfnuabout.about.links@}</dt><dd><a href="{$moduleInfo['homepageURL']}">{@hfnuadmin~hfnuabout.about.homepageURL@}</a> - <a href="{$moduleInfo['updateURL']}">{@hfnuadmin~hfnuabout.about.updateURL@}</a></dd>
</dl>
```

Résultat :

Liste des modules

News!

Version :

       stable 1.1.2 (du 2008-12-16)

Libellé :

       Module de gestion de nouvelles

Description :

       Ce module permet de gerer les nouvelles de son site web

Notes :

       N/A

License :

       GNU General Public Licence

Copyright :

       2008 FoxMaSk

Auteurs :

       FoxMaSk

Liens :

       Page d'accueil du module - Lien mise à jour

Wiki

Version :

       stable 1.0.2 (du 2009-01-25)

Libellé :

       Wiki

Description :

       Wiki maison pour la documentation du site web

Notes :

       N/A

License :

       GNU General Public Licence

Copyright :

       2008 FoxMaSk

Auteurs :

       FoxMaSk

Liens

       Page d'accueil du module - Lien mise à jour

PS : ici je n'ai pas détaillé tous les events.xml des 3 modules ni les 3
listeners mais le code est le même ;)

**Conclusion** :

Voici donc la perle ; qui en quelques petites lignes ; a permis à tous
les modules de se "trouver" et réunir des infos au même endroit.

La même mécanique des jEvent::notify() permet par exemple d'enchainer
des actions après l'inscription d'un membre (tels que lui envoyer un
mail)  
jEvent::notify() permet également d'enrichir les fonctionnalités d'un
module A via d'autres modules B,C,D sans avoir à modifier le module A,
etc...

[en savoir plus sur la communication inter
module](http://jelix.org/articles/fr/manuel-1.1/events)

