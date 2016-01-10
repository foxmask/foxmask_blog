Title: Dans la série, j'ai migré vers Pélican
Date: 2016-01-05 12:00:00
Category: Techno
Author: foxmask
Slug: dans-la-serie-jai-migre-vers-pelican
Tags: python, pelican
Status: published
Summary: Dans cet article, je vais aborder comment je créé des billets et les publie automatiquement sans plus lever le petit doigt.

## Le Besoin
Le besoin est le suivant, [Pélican](http://getpelican.com) c'est cool parce que statique mais le travers c'est qu'on ne dispose d'aucun outil "web" pour produire un billet.
Certes, si je suis joueur je peux, via mon smartphone, me connecter sur le "blog", lancer vi et produire mon billet.md :-)
On voit le coté pratique de la chose :)

## Petite digression

Gordon, sur [irc://irc.freenode.net/sametmax](irc://irc.freenode.net/sametmax) m'a parlé de Lektor, un CMS à base de fichiers plats, sans aucune base de données. Le projet semble cool.
Ce qui m'a fait sourire dans l'explication de la création de ce CMS c'est que l'auteur tire sur WordPress et balaye méchament de la main toutes les solutions de generation de pages statiques pour un blog en disant que c'est orienté pour les developpeurs, soit !

Mais quand on regarde attentivement la doc, ce n'est pas très orienté pour les "non dev" pour autant. Pourquoi ? [Regardons le quickstart](https://www.getlektor.com/docs/quickstart/)

> The best way to get started with Lektor is to use the quickstart command to let Lektor generate a basic project layout for you.

Il faut taper une commande pour créer un projet. Ca suppose que l'utilisateur sait utiliser la ligne de commandes et ... ait accès à un shell pour héberger son site.
Or avec Wordpress, on décompresse l'archive, on transfert via FTP chez son hébergeur (sans accès SSH) et on a déjà accès à son blog.

Bref passons :)

## Billets depuis GitHub

### via des issues 

Bob m'a parlé d'une solution rigolote, à base d' "issues" github, qui permet de produire directement des billets en utilisant du coup l'interface "markdown" de GitHub et des tags pour gérer le statut du billet.

### via des nouveaux fichiers 

Du coup ca m'a donné l'idée d'également exploiter l'interface markdown de github, pour, ce coup-ci, créer directement des fichiers dans le dossier **content**.
Puis une fois fait, sur le serveur hébergeant le blog, déclencher, via une *crontab*, un *git pull*, et lancer la génération du nouveau billet.

La tâche dans ma crontab donne ceci :

```shell
0 0 * * * . /foxhome/.keychain/${HOSTNAME}-sh && . /foxblog/bin/activate && cd /foxblog/website && git pull && make html
```

(on passera sur le fait que j'ai un venv dans /foxblog:)

L'astuce ici consiste à utiliser **keychain**, pour que le *git pull* ne reste pas stuck sur la demande de votre passphrase lors de l'exécution de la tâche

En effet, après l'installation de keychain, on lanche la commande

```shell
keychain $HOME/.id_dsa
```

ce qui produit

```shell
$ keychain ~/.ssh/id_rsa

 * keychain 2.7.1 ~ http://www.funtoo.org
 * Starting ssh-agent...
 * Starting gpg-agent...
 * Adding 1 ssh key(s): /foxhome/.ssh/id_rsa
Enter passphrase for /foxhome/.ssh/id_rsa:
 * ssh-add: Identities added: /foxhome/.ssh/id_rsa

```

Cette commande n'est à taper qu'une seule fois, par exemple après un reboot du serveur.
Si vous la tapez une seconde fois il ne se passera rien :) il réaffichera la liste des clés déjà chargées

## Vous avez dit Offline ?

Enfin, s'il vous arrive d'être déconnecté et ne pouvez exploiter github pour produire vos billets, ben un bête editeur texte fait l'affaire :) bon si vous avez PyCharm, vous avez un super editeur qui vous montre le rendu en live de votre texte;)
Pour ma part je suis toujours fourré avec Evernote pour ce genre de chose, dans le bus et le train. 
Ca permet de relire plusieurs fois avant de commit 'n' fois pour rien le nouveau billet.

Avec tout ça, on est paré :)
