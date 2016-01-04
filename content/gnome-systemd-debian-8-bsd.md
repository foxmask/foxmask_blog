Title: Gnome SystemD, Debian 8, *BSD
Date: 2015-05-03 14:45
Author: foxmask
Category: Techno
Tags: bsd, debian, linux, systemd
Slug: gnome-systemd-debian-8-bsd
Status: published

Il était une fois une distrib que j'utilise depuis plus de 10ans ... et
qui, comme elle prend un chemin de traverse qui ne me sied guère, va
dégager de mes ordinateurs...

Comme je ne suis qu'une poussière l'ocean, les dev de debian s'en
foutent bien largement de mon avis puisque leur choix est fait. C'est
bien justement parce qu'ils s'en foutent que je m'en vais vous dire tout
le bien que j'en pense.

Le chemin de traverse est systemd, le super génialissime
["administrateur de système et de
services"](http://www.freedesktop.org/wiki/Software/systemd/)

Qu'est-ce qui me déplait tant dans ce truc ?

1.  ) il provient de RedHat ...
2.  ) il a été poussé par Gnome ...
3.  ) Debian n'a pas daigné conserver la compatibilité avec SysV
4.  ) les logs en binaires : ca pu
5.  ) Linus Torvalds [n'aime pas ca non
    plus](http://www.zdnet.com/article/linus-torvalds-and-others-on-linuxs-systemd/),
    même s'il dit que ce n'est pas un si gros problème...
6.  ) [le pauvre petite
    canard](http://www.zdnet.fr/actualites/systemd-et-les-t-du-c-de-la-communaute-open-source-39807395.htm)
    veut nous faire pleurer...
7.  ) [Google
    inside](http://linuxfr.org/news/debian-8-jessie-l-ecuyere-est-en-selle#comment-1601253)
8.  ) le fait que systemd apparaisse sur Freedesktop.org, dénote d'un
    fait indéniable, tous les window manager qui passeraient par le
    projet Freedesktop adhéreraient à l'utilisation de Systemd...

Et j'en passe et des meilleures.

Donc j'ai passé un moment ce weekend à faire des tests d'installations :

-   Mettre à jour Debian 7.8 à 8 puis [virer
    systemd](http://without-systemd.org/)
-   Installer Debian 8 "KDE"
-   Installer FreeBSD 10
-   Installer OpenBSD 5.7

Dans le premier cas : virer systemd désinstalle gnome intégralement.
Youpi ! ... Ca rend le desktop dans un état ...

Dans le second cas : virer systemd ok mais remettre KDE .... pffff

FreeBSD ne detecte pas mon firmware wifi du portable... J'ai quand meme
pu finir par faire mon installation avec un cable ethernet, et démarrer
GDM, DBUS et je ne sais plus quel service, mais une fois sur le GDM,
impossible de récupérer une console par CTRL-ALT-1 ou 2 ou 3, la carte
graphique par en sucette.  
Quand je me connecte "normalement" depuis GDM, le desktop freeze par
intermitence... Ca rend le portable inutilisable...

OpenBSD, après des heures de téléchargement pour installer gnome, puis
xorg, pas moyen de lancer GDM ou gnome-session.  
J'ai juste eu droit au window manager par defaut : fvwm2.

Comme je galère pour passer de Linux à BSD, et comme la communauté
Linux, n'est pas tendre en vous sortant des RTFM à tirelarigot, je ne me
suis même pas essayé à demander de l'aide sur BSD.

Du coup j'ai remis une debian 7.8 en attendant un jour meilleur pour
peut-etre tenter une nouvelle installation BSD. J'ai un an avant la fin
du support de Wheezy :P

Cela dit comme systemd est fortement lié au window manager, j'ai
l'impression que les BSD et Linux sont mal partis.

Si un window manager veut perdurer dans une distrib, il va lui falloir
passer à systemd pour exister. Et si des OS ne s'y mettent pas qu'est ce
qu'il leur arrivera ?

Je ne suis pas un famillier de BSD mais si Gnome&KDE utilise systemd,
comment les BSD vont ils gérer ?  
Le desktop sous fvwm2 et xfce ...  
Probable que les BSD ne sont pas pour le desktop après tout, que c'est
pas pour les non adminsys.  
Mais la console ca va 5min hein, lire ses mails avec mutt, en passant
par procmail/fetchmail, sendmail/postfix un moment ca lasse, thunderbird
c'est pratique :P

Mon utilisation est simple: je produis des appli web ou pas avec python
et un IDE.  
Je veux pouvoir utiliser sur mes pc @ home ce que j'aurai en prod. Être
"iso-conf", de sorte que si ca merde quelque part, que je n'ai pas à
remettre en question l'OS et la version des services en place.  
C'est peut-être une déformation professionnelle mais au moins ça permet
de ne pas se poser de question lors de la mise en prod.

Et vous que pensez vous de tout ça ?

-   Debian toujours ?
-   BSD \> Debian/Linux ?
-   BSD est fait pour le desktop ? si oui lequel et avec quel window
    manager périn ?

En gros je me pose un tas de questions... et c'est pas fini

