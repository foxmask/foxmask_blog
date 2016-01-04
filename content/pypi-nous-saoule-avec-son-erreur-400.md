Title: pypi nous saoule avec son erreur 400
Date: 2015-04-19 22:45
Author: foxmask
Category: Techno
Tags: python
Slug: pypi-nous-saoule-avec-son-erreur-400
Status: published

Bon alors un truc bien pénible avec PYPI ; l'erreur 400

```shell
Upload failed (400): This filename has previously been used, you should use a different version.
```

Je pense qu'ils n'ont pas réfléchi à l'impact très néfaste.  
Je maintiens tout juste 8 modules python ; dont 7 dépendent de
django-th.  
Si je me goure d'une virgule dans ma doc et renvoie la même version je
suis blackboulé et dois faire une version n+1

J'ai bien évidemment supprimer la version qui était concernée par ma
coquille mais ca ne suffit pas, j'ai du coup supprimé le projet entier
pour le renvoyer ; RIEN Y FAIT !

Or :

-   cette manière de faire est récente, car lors de mes publications de
    novembre, je n'ai pas eu ce problème.
-   imposer cette façon de gérer m'impose de reprendre 8 modules, de
    changer la version de chacun ... POUR RIEN !
-   Il n'y a eu AUCUNE COMMUNICATION sur le sujet de cette mesure...

Je n'ose pas imaginer ceux qui en gèrent bien plus que moi...

A quoi ca encourage à part se passer de pypi ?

