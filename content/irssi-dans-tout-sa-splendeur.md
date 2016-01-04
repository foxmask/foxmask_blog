Title: IRSSI dans tout sa splendeur
Date: 2009-10-25 09:59
Author: foxmask
Category: Techno
Slug: irssi-dans-tout-sa-splendeur
Status: published

Utilisateur du [client
IRC](http://fr.wikipedia.org/wiki/Liste_de_clients_IRC)
[IRSSI](http://irssi.org) depuis *des siècles* on en découvre toujours
:)

Sur [Freenode](http://www.freenode.org) il arrive qu'on soit redirigé
sur \#freenode-fr après s'y être connecté

voici la config pour l'accès à freenode

    servers = ( {
          address = "irc.freenode.org";
         chatnet = "freenode";
         port = "6667";
         autoconnect = "yes";
         term_type = "utf-8";
         });

Donc Pourquoi la redirection vers ce channel ?

Parce qu'on ne s'est pas identifié au nickserv avant d'entrer sur le
channel. Pourtant vous avez bien ajouté à irssi *l'autosendcmd*
permettant de vous identifier au service nickserv

    chatnets = {
        freenode = {
            type = "IRC";
            nick = "votre_pseudo";
            autosendcmd = "/^msg NickServ IDENTIFY mot_de_passe";
            };};

Donc au démarrage de IRSSI, on lit bien

    09:45 [freenode] -NickServ(NickServ@services.)- Please identify via /msg NickServ identify <password>.
    09:45 [freenode] -NickServ(NickServ@services.)- You are now identified for FoxMaSk.
    09:45 [freenode] -!- FoxMaSk n=foxmask  You are now logged in. (id FoxMaSk, username n=foxmask, hostname foxmask.info)

Donc que se passe-t-il ?

Hé bien la connexion de IRSSI est *trop rapide*, et irssi enchaine
aussitôt l'accès au channel sitôt connecée sans avoir le temps de passer
par la case nickserv.

Donc l'option permettant de faire un pause après la connection et
l'indetification avant de joindre un channel est un *wait* qui s'utilise
comme suit :

    autosendcmd = "/^msg NickServ IDENTIFY mot_de_passe;wait 2000"

ce qui marquera une pause de 2secondes et là le tour est joué !

