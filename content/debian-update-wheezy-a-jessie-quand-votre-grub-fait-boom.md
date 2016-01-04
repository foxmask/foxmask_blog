Title: Debian Update Wheezy à Jessie : quand votre grub fait boom
Date: 2015-05-15 22:28
Author: foxmask
Category: Techno
Tags: debian
Slug: debian-update-wheezy-a-jessie-quand-votre-grub-fait-boom
Status: published

La mise à jour de Debian Wheezy à Jessie s'est passé comme le titre vous
le laisse à penser, explosif.  
Au reboot, grub était vide... Le pied !

Etat des lieux avant avec Wheezy :

-   PC en dualboot Win7/Debian, chacun son HDD
-   le MBR est pris par le bootloader de Windows, là avant :P
-   Debian démarre sur le boot de son propre disque

Après l'installation, grub affichait simplement le prompt "grub\>", et
plus rien.  
Lors de l'installation j'ai refusé que GRUB se place sur le MBR sur 1°
disque parce que je ne voulais absolument pas que Windows disparaisse.

Actions entreprises pour tenter de retrouver le grub comme avant :

-   Résultat KO : J'ai donc mis à jour (quand meme) win32-loader qui
    permet de booter linux depuis windows
-   Résultat KO : J'ai réinstallé Debian uniquement sur la partition
    root sans toucher à /home
-   Résultat KO : depuis le menu "grub\>", la commande ls m'affiche ...
    le dossiers systeme de WINDOWS ! Trop beau !
-   Résultat KO : boot en mode rescue pour réparer grub en tapant
    update-grub

Action qui a empiré les choses :

-   boot en mode rescue pour réparer, et taper la commande :

    ```shell
    grub-install /dev/sda
    ```

    <p>
    qui a flingue le MBR de mon windows ... au lieu de le faire pointer
    sur /dev/sdb

J'ai rebooté et bien evidement, plus d'accès à windows dans le menu

Donc retour au mode rescue j'ai créé un fichier /etc/grub.d/42\_win
contenant :

```shell
menuentry "Windows 7" {
   insmod ntfs
   search --set=root --label WINDOWS_7 --hint hd0,msdos2
   ntldr /bootmgr
}
```

<p>
ce qui m'a permit de cette fois ci rajouter windows au menu de grub
apres un update-grub !

</pre>
Création du fichier de configuration GRUB…  
Found background image:
/usr/share/images/desktop-base/desktop-grub.png  
Image Linux trouvée : /boot/vmlinuz-3.16.0-4-amd64  
Image mémoire initiale trouvée : /boot/initrd.img-3.16.0-4-amd64  
Image Linux trouvée : /boot/vmlinuz-3.2.0-4-amd64  
Image mémoire initiale trouvée : /boot/initrd.img-3.2.0-4-amd64  
Windows 7 (loader) trouvé sur /dev/sda1  
Windows Recovery Environment (loader) trouvé sur /dev/sda4  
fait

</p>
La doc que j'ai pu suivre [Grub
Multiboot](http://www.gnu.org/software/grub/manual/html_node/Multi_002dboot-manual-config.html#Multi_002dboot-manual-config),
ainsi que
[GrubRecover](https://wiki.debian.org/GrubLegacyRecover?action=show&redirect=GrubRecover)

Encore une mise à jour comme on les aime...

edit @ 23h : HHAHAHAHAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
: firefox et sublimtext qui petent .... l'installation avec un kernel
32bits sur un proc 64bits Ahaaaaaaaaaaaaaaaaaaaaaa le mode rescue
ahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

