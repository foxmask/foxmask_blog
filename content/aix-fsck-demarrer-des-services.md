Title: AIX fsck et demarrer des services
Date: 2016-01-13 23:00
Author: FoxMaSk
Category: Techno
Tags: AIX
Slug: aix-fsck-demarrer-des-services
Status: published

Sur AIX, lors d'un reboot (malencontreux?) il peut arriver que des folders soient vides (aïe bobo partout)

Bon du coup ca peut provenir du "simple" fait de "dirty" partitions qui ont besoin qu'on leur fasse faire un check 

```shell
fsck /opt/websphere
```

on repondra oui s'il vous demander de "FIX?"

et on pourra enfin faire le mount associé

```shell
# mount /opt/websphere
# ls /opt/websphere/
5.1               6.1               IHS

```

Dans la continuité du reboot, il peut arriver que des services ne se soient pas relancés donc :

```shell
# startsrc ftp
0513-124 The ftp subserver has been started.
```

et on respire !
