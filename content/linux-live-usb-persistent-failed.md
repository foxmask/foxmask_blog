Title: Linux Live USB Persistent : failed
Date: 2011-11-05 17:01
Author: foxmask
Category: Techno
Tags: linux
Slug: linux-live-usb-persistent-failed
Status: published

Suite à [cette
mésaventure](/post/2011/10/22/linux-sur-laptop-sans-disque-dur/ "Laptop sous linux sans dique dur"),
j'ai fait les frais d'une clé USB 32Go, et de 2 soirées d'affilées à la
recherche d'images ISO qui soit exploitable sur le (vieux) portable
recyclé pour ma fille.

Mon "cahier des charges" étant :

1.  Hardware
    1.  RAM utilisable 512Mo
    2.  Wifi sur une clef USB à prendre en charge

2.  Linux en Français (avec Gnome 2 pas 3 tant qu'à faire puisque vieux
    PC)
3.  le mode persistant pour stocker quelques photos de copines :P

Fort de tout cela j'ai pu essayer plusieurs outils :

1.  [Linux Live USB](http://www.linuxliveusb.com/) fourni un outil
    permettant de choisir quel périphérique utiliser, de télécharger une
    ISO, l'installer et spécifier la taille max dédié au mode
    persistant.
    1.  Mon premier choix s'était bien sûr porté sur
        [Debian](http://debian.org "GNU/Linux Debian") (utilisateur de
        debian depuis la potatoe ceci explique cela:), mais les **ISO
        debian 6.0.1** requis par l'outil ne sont pas les bonnes...
    2.  Ensuite j'ai pu m'orienter sur
        **[Ubuntu](http://ubuntu.com "Ubuntu") 11.10**, et tenter en
        vain de booter sur le portable... En vain car j'avais pas fait
        attention que j'avais déjà du mal à booter une **10.10** avant
        le crash du disque dur ...
    3.  J'ai donc repris un **10.10** mais hélas mille fois hélas, à
        part le splash screen avec les petits points qui passent du
        blanc au marron, je n'arrive jamais à passer cet écran. Pourtant
        avec un **live CD Ubuntu 10.10**, ca passe ...
    4.  Devant cet échec j'ai installé les doigts dans le nez, une
        **slackware** :
        [Slax](http://slax.org "Slax, your pocket operating système") de
        son nom! Slax fourni KDE mais est totalement en anglais (or je
        vous rappelle que c'est pour ma fille de 10ans, l'anglais
        technique c'est un poil trop tôt:) ... et ne prend pas en charge
        ma clef usb pour le wifi (à ba oui on cumule les obstacles)
    5.  J'ai bien évidement tenté d'installer le projet Linux Live USB
        Debian mais à part une liste de packages à installer, rien
        n'explique comment le faire...

2.  Ensuite pour quand même tenter d'installer une Debian (oui têtu un
    jour têtu toujours) j'ai utilisé [Cet
    outil](http://www.pendrivelinux.com/liveusb-install-live-usb-creator/)
    qui m'a permis de mettre une 6.0.3 tout aussi facilement que la
    slackware, et booter, tout nickel jusqu'au deux derniers obstacles :
    la clé usb pour le wifi, non reconnue et Gnome full English ! Shit !
    J'ai eu beau récupéré le driver (non-free:p) pour l'installer, de
    réseau wifi la Debian ne vit, ni ne voulu prendre en compte avec les
    infos que je lui avais fourni.

Après tout cela je suis dépité, ok Ubuntu avant le crash disque
reconnaissait ma clé usb et fonctionnait tant bien que mal, mais depuis
toutes ces années je n'avais jamais vu de distribution ne pas me donner
satisfaction. Sauf qu'à présent, l'idée de "redonner un second souffle à
un PC" avec un linux salvateur/sauveur devient de plus en plus
hypothétique. Si ubuntu avait envi de faire comme windows en devenant de
plus en plus gourmand, c'est gagné !

Maintenant où j'en suis ?

là :

"Papa quand est-ce que je peux utiliser mon ordinateur ?"

PS : maintenant je suis calé pour monter une distrib' en mode persistant
et ... redimensionner la partie non allouée au delà des 4Go :D

Si quelqu'un connait une distribution linux avec un gnome 2 en français
qui soit exploitable avec moins de 512Mo ... et avec prise en charge du
driver usb [ZD1211](http://sourceforge.net/projects/zd1211/) ca serait
le grand pied !

