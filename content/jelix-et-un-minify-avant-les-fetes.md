Title: Jelix et un minify avant les fêtes
Date: 2012-12-21 23:58
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, Jelix
Slug: jelix-et-un-minify-avant-les-fetes
Status: published

Hey !!!

Ca faisait une éternité que je ne m'étais pas arrêté sur Jelix et
proposé un billet sur le sujet ;)

Bon au menu de ce soir un truc très court mais utile si on ne veut pas
se bourrer de dolipranes à en avance sur les fêtes ;)

Donc voici :

**Minify**

Comme tout jelixien le sait, on peut "minifier" ses scripts CSS & JS.  
Tout se passe bien tant qu'on veut pas jouer au malin (comme moi ;p).

J'installe une version 1.5-dev toute fraîche pour [me farcir une évol'
toute con mais avec maints
ramifications](http://developer.jelix.org/ticket/1043).

Du coup là après m'être farci jConfigCompiler, je suis sur
jelix\_minify.php et là, après avoir configuré jelix pour minifier mes
CSS, je me mange un message d'erreur trop lourd pour une avant veille de
réveillon :

**ERROR 400 BAD REQUEST**

Ma qué passa ? tout cassé la machina ?

Je plonge dans le code de jelix\_minify et ne vois rien qui cloche sur
mon évol', donc commence à mettre dans un bateau firebug et firephp pour
voir lequel des 2 sera le premier à ne pas tomber à l'eau.

Manque de pot, ils se sont tous 2 noyés, j'ai dû me trouver la solution
tout seul (comme d'hab' quand c'est trop compliqué, tout le monde se
débine :P ).  
**  
Alors !! T'accouche ?**

je vous vois trépigner "mais qu'il est long pour la cracher sa valda"...
mais nan allez encore 2min de patience.

Quand on se démarre un projet flambant neuf avec jelix, on obtient la
belle page toute bleue ressemblant à [celle ci](http://huanui.org). Mais
avant d'être bleue, elle est toute blanche parce qu'on n'a pas ajouté
dans son dossier www le path vers lib/jelix-www contenant les CSS de
base de Jelix. Donc comme tout à chacun, devant ma page blanche (avec du
texte mais sans couleur, s'entend) je me fais un pur lien symbolique :

```shell
ln -s ../../lib/jelix-www jelix
```

je recharge ma page et hop la voilà toute belle vêtue de bleu.

Ensuite arrive ma config minify je recharge la page et hop ... toute
blanche ... avec comme HTTP réponse l'indigeste 400...

Comme on commence à l'entrevoir c'est mon lien symbolique qui le défrise
l'ami Jelix\_Minify.

J'ai donc fini par sucrer le lien symbolique et le remplacer par une
copie du dossier lui même.

En rechargeant ma page ce coup ci tout était bleu (sans éléPHPant :D )
et sans plus l'erreur 400.

[![éléPHPant Minifiant](/static/2012/12/2012-12-22-00.13.39-300x225.jpg)](/post/2012/12/21/jelix-et-un-minify-avant-les-fetes/2012-12-22-00-13-39/)


Sur ce passez un bon réveillon à tous ;)

