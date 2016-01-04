Title: Debian, amour et désamour
Date: 2012-12-17 14:31
Author: foxmask
Category: Techno
Tags: debian, linux
Slug: debian-amour-et-desamour
Status: published

Utilisateur de [Debian](http://www.debian.org) depuis *Le toutou
elastic* aka "Slink" (version 2.1), je n'ai jamais eu à me plaindre. Je
me suis toujours éclater avec cette distribution Linux, même si j'ai
croisé sur le chemin SlackWare, Mandrake, RedHat, Suse etc...

J'utilise actuellement Debian Squeeze (version 6 donc) que j'ai pu
installer sur mon HP en passant par ... windows... parce que le BIOS des
HP est inaccessible, oui ma bonne dame. Donc je n'ai aucun moyen de
booter le PC depuis un média quelconque "CD/DVD/Clé USB". C'est donc
depuis windows seven, je dis bien, que j'ai installé l'installeur debian
pour ajouter ensuite au bootloader de windows un point d'entrée pour
booter sur l'installeur debian (vous avez bien suivi ? c'est tordu hein
;)

Donc à présent, quand je reboot j'ai 3 choix dans mon bootloader windows
:

1.  windows 7
2.  Debian GNU/Linux
3.  l'installeur Debian

Tout ça marchait très bien, mais comme Wheezy va sortir dans peu de
temps j'ai voulu mettre à jour ma version, et là, la catastrophe.

Après un

    aptitude update

un

    aptitude upgrade 

m'affichait

    Résolution des dépendances... 
    ouverts: 378146 fermés: 658730 reportés: 344 en conflit: 1436 

ca durait 2 heures, ça m'a gonflé, j'ai tout arrete et fait un simple

    apt-get dist-upgrade

J'ai eu droit à un probleme de depedance sur default-java (un truc du
genre)  
j'ai fait un

    dpkg -P default-java

et relancer le dist-upgrade, et tout se finissa comme dans un rêve

Hé bien Nan !

X était planté, j'attéri dans une bonne vieille console 80 colonnes,
comme j'avais lancé l'upgrade depuis une session X, X a été mis à jour
et je ne voyais plus où l'upgrade s'était arrété alors qu'un ps -auxf
m'affichait toujours le process en cours...

UN gros kill du PID + un apt-get
--JENESAISPLUSQUOIPOURTOUTREMETTREDEQUERRE

Et l'upgrade se finissa oui

Comme par magie X se lança je pu accéder à gnome 3. Youpi !

Mais en fait non !

Avec Gnome2, ma Nvidia (une GT 220) était prise en charge, et mon
processeur (le ventilateur) ne faisait AUCUN bruit. Par bruit j'entends
(trop fort:P) comme quand un process lourd se lance vous voyez le genre,
style j'extrais des pistes d'un CD avec abcde, ou encode une connerie en
avi avec ffmpeg. C'est le même "son" que fait le PC au boot tant que
l'OS (windows / linux) n'a pas fini de se charger et afficher
l'interface graphique (de l'un des deux OS).

A présent, avec Gnome3, ce bruit est constant, ce qui me fait dire que
Debian Wheezy n'a pas chargé le module NVIDIA approprié sinon je
n'entendrais plus un bruit.

J'ai regardé la doc sur le wiki debian concernant NVIDIA, un beau bug de
la commande nvidia-xconfig flingue la conf de X (créé un fichier
xorg.conf vide). Si je tente d'en créer un avec juste la section Monitor
pour ajouter le nom du driver, je ne peux plus accéder à X en rebootant.
Obliger de faire un "mode sans échec" et virer le fichier pour que GDM
redémarre.

Comme le BRUIT m'insupporte, je suis reparti pour me réinstaller une
debian squeeze, et là, pratiquement à la fin, grub veut pas s'installer,
lilo non plus. Dès lors qu'on ne fait pas ce que l'installeur s'attend
comme opération, grub se vrille ; obliger de tout recommencer, ce qui
m'exaspère apres 3 installations \_pour rien\_

Donc une question à vous lecteur(s) :

1.  Avez vous une telle carte graphique et si oui pouvez vous me montrer
    votre /etc/X11/xorg.conf ?
2.  Si non, quelle distribution utilisez vous autre que Ubuntu, qui
    utilise Gnome3 ? Et par dessus le marché, cerise sur le cake, qui
    possède un installeur sous windows ? (saloperie de HP ... :P)

Dans tout cela je ne vous ai pas dit pourquoi je voulais mettre une
Debian Wheezy :

Parce que j'ai besoin des nouvelles versions de Python \> 2.6 (et
accessoirement PHP :D) pour pouvoir fournir des applications
fonctionnelles à souhait et parce que la squeeze, une fois la wheezy
sortie, ne sera plus "autant" maintenu, comprendre que les nouveautés on
devra tirer un trait dessus.

**Edit : 22h51**  
Bon je m'en suis enfin sorti apres 3 nouvelles installations et en me
reprenant la tête avec le driver fourni par Debian qui est une vraie
plaie sur mon 64bits...

**Analyse post-mortem :**

Quelque soit la config utilisée avec les pack deb l'écran blinkait
indéfiniment.

J'avais pris tous les pack deb nvidia ; taper nvidia-xconfig ; editer le
fichier /etc/X11/xorg.conf mais rien y a fait.

Hier pour anticiper le coup, j'avais download le driver chez nvidia.com
directement.

Ensuite j'ai lancé l'installeur après avoir installé gcc et
kernel-header et choisi l'installation via DKMS

Grosse erreur !

Il en avait rien à faire de mes kernel-headers.

**Solution :**  
arreter X

    /etc/init.d/gdm3 stop

lancer

    ./NVIDIA-.....run 

et à l'invite NE PAS UTILISER DKMS

La compilation se passe les doigts dans le nez !  
Ensuite un bon coup de

    nvidia-xconfig

pour pondre le fichier /etc/X11/xorg.conf

Puis un petit

    modprobe nvidia

lancer gdm3

    /etc/init.d/gdm3 start

Et là comme par enchantement le processeur se tait et "la lumière" soit
!

Me voilà de retour sur une Debian Squeeze ... et j'attendrai de pied
ferme une Wheezy STABLE !

