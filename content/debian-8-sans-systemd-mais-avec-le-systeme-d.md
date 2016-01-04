Title: Debian 8 sans systemD mais avec le système D !
Date: 2015-05-16 14:18
Author: foxmask
Category: Techno
Tags: debian, xcfe4
Slug: debian-8-sans-systemd-mais-avec-le-systeme-d
Status: published

Debian 8 [installé après un upgrade
foiré](/post/2015/05/15/debian-update-wheezy-a-jessie-quand-votre-grub-fait-boom/),
me voici sur XFCE4 ;)

[après avoir shooté systemd](http://without-systemd.org/), on redecouvre
les joies de la ligne de commandes pour certaines choses aussi QQ que se
connecter en VPN :)

```shell
aptitude install openvpn
```

suivi d'un coup de

```shell
sudo openvpn foobar.ovpn
Sat May 16 14:06:56 2015 OpenVPN 2.3.4 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [EPOLL] [PKCS11] [MH] [IPv6] built on Dec  1 2014
Sat May 16 14:06:56 2015 library versions: OpenSSL 1.0.1k 8 Jan 2015, LZO 2.08
Enter Auth Username:
Enter Auth Password:
Sat May 16 14:07:05 2015 UDPv4 link local: [undef]
Sat May 16 14:07:05 2015 UDPv4 link remote: [AF_INET]aaa.bbb.ccc.ddd:eee
Sat May 16 14:07:05 2015 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
Sat May 16 14:07:06 2015 [VPN] Peer Connection Initiated with [AF_INET]aaa.bbb.ccc.ddd:eee
Sat May 16 14:07:09 2015 TUN/TAP device tun0 opened
Sat May 16 14:07:09 2015 do_ifconfig, tt->ipv6=0, tt->did_ifconfig_ipv6_setup=0
Sat May 16 14:07:09 2015 /sbin/ip link set dev tun0 up mtu 1500
Sat May 16 14:07:09 2015 /sbin/ip addr add dev tun0 local fff.ggg.hhh.iii peer fff.ggg.hhh.iii
Sat May 16 14:07:09 2015 Initialization Sequence Completed
```

Un coup sur http://whatismyipaddress.com/ et on peut vérifier qu'on est
bien ailleurs :P

Un truc sympa avec XFCE4, les applications par défaut "Navigateur Web"
et "Client de messagerie" sont liées à vos propres outils tel FireFox ou
Thunderbird même s'ils sont dans votre \$HOME/thunderbird
\$HOME/firefox. En quoi c'est sympa ? ben pas besoin de définir des
shortcuts à la con ... comme avec Gnome 3 :P

Par ailleurs quand on défini un nouveau lanceur, taper le début du nom
du programme et il vous trouvera tout ce qui est dans \$HOME, genre
SublimeText pour ma part.

XCFE4 c'est ZE système D(ébrouille|émerde)

je reviendrai sur ce billet vous livrer le reste de quelques trucs
sympas

