Title: Jelix - Token le révélateur !
Date: 2008-12-14 13:05
Author: foxmask
Category: Techno
Tags: Jelix
Slug: jelix-token-le-revelateur
Status: published

Depuis la v 1.1RC1 de [Jelix](http://www.jelix.org), l'apparition de la
"lutte" contre les
[CSRF](http://fr.wikipedia.org/wiki/Cross-Site_Request_Forgeries) avec
les tokens permettent non seulement de sécuriser vos formulaires ; tout
à fait automatiquement et de façon transparente ; mais pas seulement !

Comment cela ?

Supposons que nous éditions l'article 1 depuis l'url
http://localhost/article/edit/1

le code de la methode "edit" serait le suivant :

` function edit { // recuperation de l'id passé sur l'url $id = (integer) $this->param('id'); // si le bouton validate n'est pas utilisé, nous inititions le formulaire if ($this->param('validate') == '') {    $form = jForms::get('article~artdao',$id); } // le bouton validate a été pressé : else {    // récuperation de l'instance du formulaire    $form = jForms::fill('article~artdao');    $form->saveToDao('article~artdao',$id); } }`

Que ce passerait il avec ce code ?

\# L'acces à la page d'edition passerait impeccable.  
\# La sauvegarde des données ne se passerait pas bien et nous aurions
un message d'erreur :

` [exception 835]  Le token du formulaire n'est pas valide, vous devez remplir le formulaire correctement à partir du site. ..lib/jelix/forms/jFormsBase.class.php 142`  
on aura beau vider le cache de son application rien n'y fera.

Alors pourquoi ce message ?

Simplement parceque lors de l'initialisation de l'instance \$form (avec
jForms::get() nous avons passé en paramètre l'id , mais qu'on ne l'a pas
utiliser avec  
`    $form = jForms::fill('article~artdao');`  
donc, remplacez le code ci dessus, par ceci  
`    $form = jForms::fill('article~artdao',$id);`  
et le message d'erreur sur le token ne se produira plus.

Voici une façon détourner de vérifier que son formulaire est
correctement géré avec la fonction anti CSRF ;-)

