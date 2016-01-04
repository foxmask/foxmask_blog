Title: Debian Network Manager et Eth0 non gérée
Date: 2014-06-03 09:54
Author: foxmask
Category: Techno
Tags: debian, linux
Slug: debian-network-manager-et-eth0-non-geree
Status: published

Quand on est une faignasse qui n'a pas envie de se plonger dans les
arcanes des fichiers de config pour gérer l'accès réseau et qu'on n'a
pas envie de faire ça sur sa workstation, on a un truc qui répond au
besoin avec le
[NetworkManager](https://wiki.debian.org/fr/NetworkManager) disponible
sous gnome.

En général ce dernier est installé mais ne permet pas de configurer sa
carte réseau depuis gnome.

On a généralement ceci :

![Réseau non géré](/static/2014/06/lan_ko.png)](/static/2014/06/lan_ko.png)


Du coup on est dans l'incapacité de gérer l'interface réseau de son
choix ...

En cherchant très très loin [dans la
doc](https://wiki.debian.org/fr/NetworkManager#Les_r.2BAOk-seaux_filaires_ne_sont_pas_g.2BAOk-r.2BAOk-s)
on trouve une ligne de configuration à switcher de valeur.  
On editera donc le fichier **/etc/NetworkManager/NetworkManager.conf**
dans lequel on changera le *false* en *true*

```ini
[ifupdown]
managed=true
```

Ensuite on relance :

```shell
# /etc/init.d/network-manager restart
[ ok ] Stopping network connection manager: NetworkManager.
[ ok ] Starting network connection manager: NetworkManager.
```

Et on obtient enfin ceci :  
[![Réseau géré](/static/2014/06/lan_ok.png)](/static/2014/06/lan_ok.png)

Ce qui nous permet à présent d'ouvrir la config de l'interface elle-même !

Un dernier tips en passant, si vous tripotez votre config réseau via
l'interface graphique, mettez de coté le fichier **/etc/resolv.conf**,
afin de ne pas perdre votre résolution DNS au cas où vous vous
tromperiez dans votre conf réseau. Dès que vous appliquez vos
paramètres, le fichier **/etc/resolv.conf** est **dynamiquement
regénéré**.

Dans un prochain billet, la config d'un accès avec OpenVPN (où
j'aborderai de nouveau ces subtilités) par exemple si ça vous botte.

