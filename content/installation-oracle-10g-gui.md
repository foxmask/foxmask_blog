Title: Installation Oracle 10G en mode spéléo
Date: 2014-10-09 10:24
Author: foxmask
Category: Techno
Tags: oracle
Slug: installation-oracle-10g-gui
Status: published

Bon, j'avais un wiki, au temps jadis, que j'avais basardé parce que je
m'étais dit "Oracle 10 n'est plus supporté, je n'aurai plus à me faire
suer pour l'installer" ... Et c'est toujours dans ces cas de figure
qu'on se maudit quand le moment poindre le bout du nez.

Voilà donc un billet qui part en spéléo vous narrez quelques trucs qui
depuis le temps sont surement déjà acquises (j'ose espérer ;)

Donc pour installer Oracle 10g, je vous souhaite d'avoir les archives
dans un coin car ça n'est plus dispo chez Oracle via la manager qui va
bien.

Après les avoir décompressées, temps il est de lancer l'installeur :

```shell
cd database
./runInstaller
```

La plupart du temps on n'installe pas Oracle sur une workstation ou sur
un serveur disposant d'un écran et d'un clavier. Or l'installeur Oracle
utilise "OUI" (Oracle Universal Installer), qui lance une GUI !

Donc avant même de lancer cet installeur, on est bon pour :

1.  installer la machinerie pour compiler
2.  installer des lib X11
3.  configurer le forwarding X11

### 1- la machinerie pour compiler

```shell
yum install binutils gcc glibc glibc-headers glibc-kernheaders glibc-devel
compat-libstdc++ cpp compat-gcc make compat-db compat-gcc-c++ 
compat-libstdc++-devel openmotif openmotif21
setarch pdksh libaio libaio-devel 
libXt.i686 libXt-devel.x86_64 libXt-devel.i686
libXtst.i686 libXtst-devel.i686 libXtst-devel.x86_64 
```

### 2- installer des lib X11

ceci vous evitera de rencontrer ce genre d'erreur :

```shell
java.lang.UnsatisfiedLinkError: /tmp/OraInstall../jre/1.4.2/lib/i386/libawt.so: 
libXtst.so.6: cannot open shared object file: No such file or directory
```

### 3- configurer le forwarding X11

pour faire du X11 forwarding, tout le monde sait qu'on fait

```shell
ssh -X login@server
```

mais si on regarde de plus près, ça ne suffit souvent pas :

```shell
ssh -v -X login@server
...
debug1: Remote: No xauth program; cannot forward with spoofing.
X11 forwarding request failed on channel 0
```

comme l'avant dernière ligne l'indique, il n'y a pas xauth de dispo,
donc let's go

```shell
yum install xauth
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.quelquesmots.fr
 * extras: centos.mirror.fr.planethoster.net
 * updates: centos.crazyfrogs.org
base                                                                                                                                                     | 1.1 kB     00:00     
extras                                                                                                                                                   | 2.1 kB     00:00     
updates                                                                                                                                                  | 1.9 kB     00:00     
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package xorg-x11-xauth.i386 1:1.0.1-2.1 set to be updated
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================================================================================================================
 Package                                         Arch                                  Version                                      Repository                             Size
================================================================================================================================================================================
Installing:
 xorg-x11-xauth                                  i386                                  1:1.0.1-2.1                                  base                                   31 k

Transaction Summary
================================================================================================================================================================================
Install       1 Package(s)
Upgrade       0 Package(s)

Total download size: 31 k
Is this ok [y/N]: Y
Downloading Packages:
xorg-x11-xauth-1.0.1-2.1.i386.rpm                                                                                                                        |  31 kB     00:00     
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
  Installing     : xorg-x11-xauth                                                                                                                                           1/1 

Installed:
  xorg-x11-xauth.i386 1:1.0.1-2.1                                                                                                                                               

Complete!
```

Ensuite il se peut que ca ne suffise toujours pas, il faut donc editer
le fichier <code< etc ssh sshd_config< code>  
pour mettre ces parametres :

```ini
X11Forwarding yes
X11UseLocalhost no
```

puis relancer sshd.

Testons à présent

```shell
ssh -v -X oracle@server
debug1: Requesting X11 forwarding with authentication spoofing.
debug1: Sending environment.
debug1: Sending env LANG = fr_FR.utf8
Last login: Thu Oct  9 09:40:29 2014 from 
/usr/bin/xauth:  creating new authority file /u01/app/oracle/.Xauthority
[oracle@server ~]$ xclock
debug1: client_input_channel_open: ctype x11 rchan 2 win 65536 max 16384
debug1: client_request_x11: request from 127.0.0.1 41557
debug1: channel 1: new [x11]
debug1: confirm x11
debug1: channel 1: FORCE input drain
```

ouais vous la voyez pas sur cette page l'horloge, faut pas pousser non
plus ;)

Si ça ne marchait toujours pas chez vous, vérifiez bien que
X11Forwarding est activé sur le serveur :

```shell
grep X11Forwarding /etc/ssh/sshd_config
#X11Forwarding no
X11Forwarding yes
```

Maintenant zont n'est prêt pour lancer l'installeur.

```shell
cd /u01/app/oracle/binaires/database/
./runInstaller -ignoreSysPrereqs
```

et le GUI démarre, zavez plus qu'à vous faire plaisir.

le `-ignoreSysPrereqs` indique à Oracle de me lâcher la grappe sur les
prérequis système, notamment sur l'OS qui n'est pas RedHat.

### Et c'est pas fini ©

Je n'ai volontairement pas abordé les prérequis techniques sur les
sémaphores et tout le bataclan, le net en regorge, ce billet est un
nième noeud à mon mouchoir pour pouvoir lancer le GUI :P

Une solution existe pour lancer l'installer sans le GUI avec l'option
`-silent` et avec un fichier de *réponses*
(`-reponseFile /full/path/to/responsefile.rsp`) contenant déjà tout le
paramétrage qui va bien. Mais souvent les fichiers de réponse ne sont
pas à jour. Ne serait-ce que la structure du fichier d'une version
mineure à l'autre de Oracle. Je l'ai juste citée en cas de besoin ;)

