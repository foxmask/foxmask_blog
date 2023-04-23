Title: Ubuntu 20.04 LTS rollback
Date: 2022-05-18 18:51:02.825787+00:00
Author: FoxMaSk 

tags: ubuntu

Status: published





# Ubuntu 20.04 LTS rollback

[Ubuntu 20.04 LTS rollback](None)

# Suite et fin de ma mésaventure avec l&#39;upgrade de merde en 22.04.

Pour la faire courte j&#39;ai réinstallé la 20.04 LTS, et comme je suis parano, j&#39;avais des backups en veux-tu en voila, que j&#39;ai pu reprendre pour restorer $HOME et zoo

En détails kékicépassé ?

## Hangul 

Apres [mes déboires](https://shaarpy.foxmask.org/link/63dQvg/) lors de l&#39;upgrade en 22.04 et la découverte de la perte de du [Hangul](https://fr.wikipedia.org/wiki/Hangeul)... j&#39;ai remué ciel et terre pour trouver une solution, tant sur irc #ubuntu-kr (où on m&#39;a dit &#34;ouais ubuntu c&#39;est de pire en pire depuis la 18.04, j&#39;ai remis une gentoo sur le laptop&#34;) qu&#39;auprès d&#39;un des mainteneurs du packet ibus-hangul pour ubuntu (qui m&#39;a joyeusement envoyé chier avec un &#34;j&#39;utilise ubuntu 20.04&#34;)

## Ouais Land !

J&#39;ai découvert que passer Wayland serait le saint graal et comme le driver de ma carte graphique NVIDIA datait de la 18.04 je me suis resolu à passer à la derniere version puisque le carte etait dans le lot des cartes supportées.

Grand mal m&#39;en a pris, au reboot, comme attendu (oui comme attendu car c&#39;etait un probleme très bien connu sur un forum de nvidia) le portable ne rebootait plus une fois la clé de cryptage fournie... \

## NVIDIA

Au final j&#39;ai rebooté en mode recovery, et fait un bon gros 

` ` ` shell
apt remove nvidia-* 
` ` ` 

et là tranquille et content je reboot \
et hop tout est de retour je souffle .... ou presque  \
je pars pour me remettre la version de la 18.04 du driver nvidia 

` ` ` shell
apt remove nvidia-*-390
` ` ` 

## RESEAU 

et là surprise, plus de reseau !

la goutte d&#39;eau mon vieux !


## USB RUFUS

&#34;hey fiston passe moi ton portable que je me fasse un clef boutable ...&#34;

et voilà j&#39;ai dl une image iso de la version desktop et avec [rufus](https://rufus.ie/fr/) ; coller ca sur une clé USB 8Go, changer l&#39;ordre de bootage dans le bios du portable et c&#39;était reparti, installation de base, et tout à la fin, j&#39;ai pluggé un disque externe ssd 1To, restorer à la bonne date (pour eviter de flinguer mon `$HOME` avec des fichiers de conf en 22.04 :P)