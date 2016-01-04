Title: extraire une portion d'une archive distante sans la télécharger
Date: 2014-03-27 14:46
Author: foxmask
Category: Techno
Tags: linux
Slug: extraire-une-portion-dune-archive-distante-sans-la-telecharger
Status: published

Bon c'est certes pas nouveau mais à force de la chercher, alors que je
m'en servais à un temps que les moins de 20 ans ne peuvent pas
connaitre, je la mets là, c'est pas pour emporter c'est pour manger tout
de suite.

Le truc ici va consister à être une partie d'une archive sans avoir à la
télécharger.

On fait comme ca :

```shell
wget -O - url |tar -xvzf - [dossier|path/vers/fichier]
```

je vous laisse jouer sur les options de tar mais l'idée est là ;)

genre ça fait quelques années lumières que je n'ai pas vu la tête d'une
archive du kernel linux de près, let's go dancing :

```shell
 wget -O - ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/linux-3.11-rc6.tar.gz|tar tvzf -
--2014-03-25 01:42:05--  ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/linux-3.11-rc6.tar.gz
           => «-»
Résolution de ftp.kernel.org (ftp.kernel.org)... 198.145.20.140, 149.20.4.69, 199.204.44.194
Connexion vers ftp.kernel.org (ftp.kernel.org)|198.145.20.140|:21...connecté.
Ouverture de session en anonymous...Session établie!
==> SYST ... complété.    ==> PWD ... complété.
==> TYPE I ... complété.  ==> CWD (1) /pub/linux/kernel/v3.x/testing ... complété.
==> SIZE linux-3.11-rc6.tar.gz ... 113162100
==> PASV ... complété.    ==> RETR linux-3.11-rc6.tar.gz ... complété.
Taille: 113162100 (108M) (non certifiée)

 0% [                                                                                                                                     ] 37 648       183K/s              drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/
-rw-rw-r-- root/root      1097 2013-08-18 23:36 linux-3.11-rc6/.gitignore
-rw-rw-r-- root/root      4465 2013-08-18 23:36 linux-3.11-rc6/.mailmap
-rw-rw-r-- root/root     18693 2013-08-18 23:36 linux-3.11-rc6/COPYING
-rw-rw-r-- root/root     95317 2013-08-18 23:36 linux-3.11-rc6/CREDITS
drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/
-rw-rw-r-- root/root       107 2013-08-18 23:36 linux-3.11-rc6/Documentation/.gitignore
-rw-rw-r-- root/root     16957 2013-08-18 23:36 linux-3.11-rc6/Documentation/00-INDEX
drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/
-rw-rw-r-- root/root      3284 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/README
drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/
-rw-rw-r-- root/root       248 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/proc-sys-vm-nr_pdflush_threads
-rw-rw-r-- root/root      1296 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/sysfs-bus-usb
-rw-rw-r-- root/root      1063 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/sysfs-class-rfkill
-rw-rw-r-- root/root      2820 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/sysfs-driver-hid-roccat-koneplus
-rw-rw-r-- root/root      3657 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/sysfs-driver-hid-roccat-kovaplus
-rw-rw-r-- root/root      3767 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/obsolete/sysfs-driver-hid-roccat-pyra
 0% [                                                                                                                                     ] 79 640       183K/s              drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/
-rw-rw-r-- root/root       471 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/devfs
-rw-rw-r-- root/root       664 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/dv1394
-rw-rw-r-- root/root       310 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/ip_queue
-rw-rw-r-- root/root       449 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/o2cb
-rw-rw-r-- root/root       663 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/raw1394
-rw-rw-r-- root/root       751 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/removed/video1394
drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/stable/
-rw-rw-r-- root/root      4140 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/stable/firewire-cdev
```

Vous pouvez faire varier les plaisirs avec un grep au bout evidement,
genre je ne veux que ce qui cause crypto :

```shell
 wget -O - ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/linux-3.11-rc6.tar.gz|tar tvzf - |grep crypto


--2014-03-25 01:50:56--  ftp://ftp.kernel.org/pub/linux/kernel/v3.x/testing/linux-3.11-rc6.tar.gz
           => «-»
Résolution de ftp.kernel.org (ftp.kernel.org)... 199.204.44.194, 198.145.20.140, 149.20.4.69
Connexion vers ftp.kernel.org (ftp.kernel.org)|199.204.44.194|:21...connecté.
Ouverture de session en anonymous...Session établie!
==> SYST ... complété.    ==> PWD ... complété.
==> TYPE I ... complété.  ==> CWD (1) /pub/linux/kernel/v3.x/testing ... complété.
==> SIZE linux-3.11-rc6.tar.gz ... 113162100
==> PASV ... complété.    ==> RETR linux-3.11-rc6.tar.gz ... complété.
Taille: 113162100 (108M) (non certifiée)

 0% [                                                                                                                                     ] 41 992       166K/s              -rw-rw-r-- root/root      1188 2013-08-18 23:36 linux-3.11-rc6/Documentation/ABI/testing/debugfs-pfo-nx-crypto
 1% [>                                                                                                                                    ] 1 369 808    828K/s              drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/crypto/
-rw-rw-r-- root/root      6569 2013-08-18 23:36 linux-3.11-rc6/Documentation/crypto/api-intro.txt
-rw-rw-r-- root/root     11244 2013-08-18 23:36 linux-3.11-rc6/Documentation/crypto/asymmetric-keys.txt
-rw-rw-r-- root/root      9347 2013-08-18 23:36 linux-3.11-rc6/Documentation/crypto/async-tx-api.txt
-rw-rw-r-- root/root     17200 2013-08-18 23:36 linux-3.11-rc6/Documentation/crypto/descore-readme.txt
drwxrwxr-x root/root         0 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/
-rw-rw-r-- root/root       399 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/fsl-imx-sahara.txt
-rw-rw-r-- root/root      2784 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/fsl-sec2.txt
-rw-rw-r-- root/root     14202 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/fsl-sec4.txt
-rw-rw-r-- root/root       544 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/mv_cesa.txt
-rw-rw-r-- root/root       789 2013-08-18 23:36 linux-3.11-rc6/Documentation/devicetree/bindings/crypto/picochip-spacc.txt
 2% [==>                                                                                                                                  ] 3 075 552   1,31M/s 
```

L'intérêt est de ne pas encombrer son HDD de saloperies "temporaires"
qui finissent toujours par durer.

Voilou, je n'ai plus à me demander "boudiou c'est comment que je faisais
dans l'ancien temps avec mes doigts"

