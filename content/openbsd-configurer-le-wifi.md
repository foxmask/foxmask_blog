Title: OpenBSD : configurer le wifi
Date: 2015-05-08 13:55
Author: foxmask
Category: Techno
Tags: bsd
Slug: openbsd-configurer-le-wifi
Status: published

Hey !

Comme à mon habitude, je mets là mes déboires/résolutions de problèmes
de noob, pour les prochains noob passant par là ...

**Etat des lieux**  
Découvrant OpenBSD, mis sur un laptop depuis 1 semaine, le besoin
premier : accèder au net via le wifi.

Par defaut j'avais pu configurer l'interface ethernet, mais se trimbaler
le fil rj45 ...  
Donc bon...

**La config de départ**  
sur BSD il s'avere que la partie gerant la config réseau se trouve
comme chacun le sait (sauf moi depuis 5min :) dans
/etc/hostname.<interface>

Donc ayant déjà /etc/hostname.bge0 contenant la seule ligne dhcp, je
l'ai copié en /etc/hostname.iwi0, qui est mon interface wifi.

Ensuite il faut faire :

```shell
ifconfig iwi0 down
ifconfig iwi0 nwid "Livebox-xxxx" wpakey "xxxxxxxxx"
ifconfig iwi0 up
dhclient iwi0
```

et voilà :)

