Title: A la recherche d'une alternative opensource d'Evernote
Date: 2016-05-07 18:00
Author: foxmask
Tags: evernote, opensource
Category: Techno
Slug: evernote-opensource-alternative
Status: published
Summary: Après avoir mis un coup de pied au derrière de Pocket, vient le tour de Evernote ;)

En ce samedi (relativement) ensoleillé, j'ai demandé par ci par là si chacun connaissait une alternative opensource
 à Evernote fournissant un client Android, et cerise sur le gateau avec une API 
 (pour évidemment passer les notes de Evernote à la futures solutions choisies)

Le but étant d'avoir l'appli à portée de main facilement.

Voici les réponses obtenues :

| solution      | Langage | API | Client Android |
| ------------- |---------|-----|----------------| 
| [Laverna](https://github.com/Laverna/laverna) | JavaScript | non | non |
| [Paperwork](https://github.com/twostairs/paperwork) | PHP | [oui](https://laverna.cc/index.html) | [oui](https://github.com/theSoenke/Paperwork-Android) |
| [ownCloud](https://owncloud.org/) | PHP | n/a | [oui](https://play.google.com/store/apps/details?id=com.owncloud.android) |
| [Turtl](https://github.com/turtl/js) | JavaScript | [oui](https://github.com/turtl/api) | [oui](https://play.google.com/store/apps/details?id=com.lyonbros.turtl) |
| Simplenote | | | | 

Voici mon retour :

* Laverna semble fun (facile à installer, modulo le choix du "storage") mais pas de client android ni api
* ownCloud est "too much" pour juste un outil de prise de notes (entre autre)
* Turtl est sympa mais la doc de l'API ... se résume à une page qui me laisse sans voix https://turtl.it/docs/server/
* simplenote n'est pas opensource

Le choix ... mais : 

 * paperwork : 
 
J'ai facilement ([à partir de cette page](https://github.com/twostairs/paperwork/wiki/Installing-Paperwork-on-Debian-7)) pu installer, mais quand j'ai mis PostgreSQL en guise de RDBMS ... *[boom](https://github.com/twostairs/paperwork/issues/615)*

Du coup je suis le bec dans l'eau :P
