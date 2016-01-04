Title: Debian 7 Wheezy - re mise à jour du driver NVIDIA
Date: 2013-05-06 18:16
Author: foxmask
Category: Techno
Tags: debian, linux
Slug: debian-7-wheezy-re-mise-a-jour-du-driver-nvidia
Status: published

Je viens de finir d'installer cette mise à jour de Debian Wheezy sur 2
PC ; un portable Dell Latitude sans aucun soucis mais comme d'hab mon PC
de bureau n'en fait qu'à sa tête...

Le soucis se situe à plusieurs endroits :

-   GRUB
-   Carte Graphique

**GRUB :**

La mise à jour m'a flingué grub sans que j'ai eu le temps de voir ce
qu'il s'était passé... au reboot j'étais stuck "dans le noir"...
condamné à refaire une installation from scratch ...

**NVIDIA GT 220**  
Comme on change de release Debian, on change de kernel, donc on est
"bon" pour se retaper l'installation du driver NVIDIA en version 304.64
pour 64Bits ; toutes autres versions antiérieures ne compilera tout
bonnement pas ne trouvant pas le fichier version.h dans les sources du
kernel ; rien que ça.

Donc pour ce faire :

arreter X

    /etc/init.d/gdm3 stop

lancer

    ./NVIDIA-Linux-x86_64-304.64.run

A l'invite il peut vous dire que vous utilisez un GCC 4.7 et que le
module était prévu pour compiler avec GCC 4.6 vous lui dites donc "non"
et ça passera.

La compilation se passe les doigts dans le nez !  
L'installeur vous demandera s'il peut vous exectuer

    nvidia-xconfig

pour pondre le fichier /etc/X11/xorg.conf  
Dites lui oui !

finissez par un petit

    modprobe nvidia

lancer gdm3

    /etc/init.d/gdm3 start

Et là comme par enchantement on retrouve un environnement graphique
paisible.  
Par paisible j'entends que l'installation précédente allait très bien
mais que le ventilo du proc de la CG tournait comme un débile à qui l'on
aurait demander de faire du traitement vidéo... Alors qu'une fois le
module NVIDIA chargé tout redevenait clamos.

Voilou !

Edit 16/5 : un truc qui m'a quand même fortement déplu avec ces mises à
jour. (j'en ai fait 3), il n'y a aucun avertissement sur le non support
du driver NVIDIA lors de l'upgrade. On est dans le noir si le driver ne
passe pas ... et pour retrouver ses billes, "interroger" la "toile" ; si
on n'est pas familier de links ou w3m c'est la mort

