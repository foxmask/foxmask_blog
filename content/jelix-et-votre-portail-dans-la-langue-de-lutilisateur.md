Title: Jelix et votre portail dans la langue de l'Utilisateur
Date: 2009-03-08 11:00
Author: foxmask
Category: Techno
Tags: Jelix
Slug: jelix-et-votre-portail-dans-la-langue-de-lutilisateur
Status: published

Je ne vais pas ici répéter la [documentation sur le plugin coord
"autolocale", plugin permettant de gérer automatiquement
l'internationalisation de vos
templates](http://jelix.org/articles/fr/manuel-1.1/locales).

Le propos de ce billet consiste à montrer comment avec Jelix, jAuth et
jCommunity en particulier, on peut changer la langue de l'utilisateur et
ainsi obtenir des pages dans pour sa langue.

jCommunity donc, fourni des évènements, dont un permettant d'enregistrer
toutes modifications sur le compte de l'utilisateur, cet evenement est
`jcommunity_save_account`.

Dans la class de mon listener `authhavefnubb.listener.php` j'aurai donc
ce qui suit à chaque modification de mon compte :

``` {.php}
function onjcommunity_save_account ($event) {
global $gJConfig;
// recuperation des données saisies dans mon formulaire
$form = $event->getParam('form');
if ( $form->getData('member_language') != '') {
$_SESSION['JX_LANG'] = $form->getData('member_language');
$gJConfig->locale = $form->getData('member_language');
}
// un petit message d'info signalant que le profil est mis à jour
jMessage::add(jLocale::get('havefnubb~member.profile.updated'),'ok');
}
```

l'astuce ici est de mettre
`$gJConfig->locale = $form->getData('member_language');` avant le
` jMessage::add` pour que le message qui vient juste apres soit traduit
immédiatement dans la langue choisie, sinon ce dernier apparaitrait
"encore" dans la langue précédante ou celle du portail.

ensuite on opérera de la même façon avec les évènement de jAuth que sont
AuthLogin (lors de la connexion) et AuthLogout (lors de la déconnexion)

``` {.php}
function onAuthLogin ($event) {
...
$_SESSION['JX_LANG'] = $user->member_language;
$gJConfig->locale = $user->member_language;
}
 
function onAuthLogout ($event) {
// suppression de la langue dans la session courante pour récupérer celle du portail
$_SESSION['JX_LANG'] = '';
unset($_SESSION['JX_LANG']);
}
```

et l'on définira notre fichier events.xml comme suit :

``` {.xml}
<listener name="authhavefnubb">
<event name="AuthLogin" />
<event name="AuthLogout" />
<event name="jcommunity_save_account" />
</listener>
```

Ainsi donc avec une petite dizaine de lignes dans un listener et 3
noeuds XML on a permit à tout utilisateur de notre site d'avoir des
pages dans sa langue favorite.

