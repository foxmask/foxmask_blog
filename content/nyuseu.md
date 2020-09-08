Title: 뉴스 - Nyuseu - News 
Date: 2020-09-08 18:00
Author: foxmask
Category: Techno
Tags: Django, python
Slug: nyuseu-news 
Status: published

# 뉴스 - Nyuseu - News

Waza ?

Un billet sur le/la COVID19 ?

Nan

Un billet sur les vacances ? 

Nan

Sam revient ? 

NAn !

J'ai changé de boulot ?

Nannnnnnnnnnnn !

J'abandonne le coréen ? 

Naaan !

Bé alors quoi ?

Bon ben, j'ai refait un truc inutile !

Un nouveau projet me permettant de lire des flux de données dans mon navigateur.

Dans le même genre gratuit, mais pas opensource, vous avez Feedly, Inoreader, dans le genre opensource vous avez Wallabag.

Alors pourquoi celui là ? 

Ben j'avais du temps à perdre :P entre 2 pages de 한국 et quelques écoutes de [podcast](http://world.kbs.co.kr/service/contents_list.htm?lang=f&menu_cate=learnkorean)

Puis Wallabag c'est en PHP :P 

Du coup j'ai fait le bidule en Python3.8 / Django3.1 et Bootsrap4, tranquillou. Ni plus ni moins.

![](https://raw.githubusercontent.com/foxmask/nyuseu/master/nyuseu/doc/screenshot.png)

C'est "con comme la lune" ;)

On peut importer des fichiers OPML pour demarrer sur des flux qu'on choie.

```bash
python manage.py opml_load ~/Download/feedly-e2343e92-9e71-4345-b045-cef7e1736cd2-2020-05-14.opml 
Nyuseu Server - 뉴스 - Feeds Reader Server - Starlette powered
Humor Le blog d'un odieux connard
Dev Vue.js News
Dev Real Python
Dev PyCharm Blog
Dev Python Insider
Dev The Django weblog
Dev Ned Batchelder's blog
Dev Pythonic News: Latest
Dev Caktus Blog
Dev The Official Vue News
Android Les Numériques
Android Frandroid
Dys Fédération Française des DYS
Gaming NoFrag
Gaming Gameblog
Gaming Gamekult - Jeux vidéo PC et consoles: tout l'univers des joueurs
Gaming PlayStation.Blog
Gaming jeuxvideo.com - PlayStation 4
Nyuseu Server - 뉴스 - Feeds Loaded
```



Après le moteur se charge dans une crontab de vous rapatrier les données et les mettre dans la base.

Si on n'a pas envie de demarrer le serveur on peut toujours utiliser la console pour lire les flux :P 

```bash
python manage.py nyuseu
```

Liste des articles

![Articles List](https://github.com/foxmask/nyuseu/raw/master/nyuseu/doc/nyuseu_articles_list.png)

```bash
python manage.py nyuseu -id 1158
```

un article

![An Article](https://github.com/foxmask/nyuseu/raw/master/nyuseu/doc/nyuseu_an_article.png)

Cela reste somme toute, tout à fait lisible :P

PS: pour le nom vous l'aurez devinez, ` 뉴스  ` se prononce `niousseu`  (en français) qui veut dire ` News` not in French :P

[Les sources sont par ici](https://github.com/foxmask/nyuseu)