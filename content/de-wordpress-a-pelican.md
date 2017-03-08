Title: De wordpress à pelican
Date: 2016-01-02 17:00
Category: General
Tags: pelican, python
Slug: de-wordpress-a-pelican
Authors: FoxMaSk
Summary: Un enième billets d'une migration de Wordpress à Pelican

Ce billet est surement le *beacoupdième* abordant le sujet ;-)

J'irai donc faire court dans la mesure du possible pour expliciter le *pourquoi*, le *comment*, et une *idée* qui a germé lors de l'utilisation de [pelican](http://getpelican.com "Generateur statique de site web")


Pourquoi ?
==========

La réponse est multiple, et un peu redondante avec le billet précédent.
J'ai voulu mettre fin à mon blog en wordpress parce que je ne vais pas continuer à conserver le domaine et l'hebergement associé. Comme je n'ai tout de même pas voulu tout mettre aux oubliettes, j'ai tout de même conserver un peu de ces 11ans de blog.
Le choix vers pelican s'est fait naturellement après l'avoir testé pour 2 autres blogs, celui pour "[la communauté sam et max](http://smcomm.trigger-happy.eu)" et celui du projet [trigger-happy](http://blog.trigger-happy.eu)


Comment ?
=========

Comme le dit la doc, en premier lieu il faut exporter son blog wordpress dans un fichier XML.
Après, pour l'importer, on choisit le format d'import : reStructuredText, Markdown.

```shell
pelican-import --wpfile foxmaskinfo.xml 
```

ainsi lancée, la commande part pour me traduire 900 billets en .rst

Mais là j'ai pris une sérieuse claque.
A chaque lancement de la commande je me coltinais des erreurs de formatage, des retour à la ligne inopinée, des urls tronquées pour des carriage return line feed inopinées.
Au bout de 2 jours, j'arrivais à finir ma migration d'import en ayant pris soin de remplacer toutes les urls http://foxmask.info et http://foxmask.bzh en '/' purement.
Mais un malencontreux et tardif (vu l'heure)

```shell
rm -f content/*
```
m'a coupé les pattes , 2j partis en fumée j'en pouvais plus, j'étais sur le point de laisser tomber la migration.

J'ai donc cherché une recette sur la toile, sur le best practice de cette migration et là je tombe sur [ce post](http://kevin.deldycke.com/2013/02/wordpress-to-pelican/) complet.
Et surtout j'étais passé à coté du format Markdown.
Donc nouveau plan de bataille :

* utiliser le format markdown
* gerer le remplacement de foxmask.(bzh|info) avec PyCharm afin qu'il gère le remplacement récursivement et tranquillement.


```shell
pelican-import --wpfile -m markdown foxmaskinfo.xml 
```

Et là, miracle : PAS UNE SEULE erreur de formatage à l'issue de cette migration, j'étais comme deux ronds de flan.

Ensuite, avec PyCharm, j'acheve la mise à jour des urls en 2min :P

Le reste de la migration c'est :

dans *pelicanconf.py*, gérer le chemin static de toutes les images que j'ai pu coller dans le blog

Puis après quelques ajustements de [themes](https://github.com/duilio/pelican-octopress-theme) et [plugin pelican](https://github.com/getpelican/pelican-plugins), voilà le blog prêt.

Une idée
========

Maintenant une idée toute QQ.

Pelican c'est cool parce que statique. Ya pas plus simple qu'une page HTML à servir pour un serveur HTTP.

Par contre niveau production de billet, pelican est très geek oriented.
Je ne m'imagine pas un utilisateur lambda de wordpress, passer à Pelican.
Déjà, les thèmes ne courrent pas les rues, et la saisie des billets n'est pas le plus fun.

Du coup j'm'ai dizamoimeme : pourquoi ne pas faire une interface web qui permette de pondre ses billets ? Pas un truc aussi ambitieux que l'interface de Wordpress, mais au moins :

* une page pour créer un article avec un editeur wysiwyg
* à l'enregistrement de l'article, créer le fichier .md
* générer la page html via la commande make html

avant de me lancer dans ce truc j'ai demandé sur [#pelican@freenode](irc://irc.freenode.net/pelican) si un tel projet existait, et j'ai eu droit à une réponse de normand... Donc bon je vois kiki va kor faire un truc con kwa.


