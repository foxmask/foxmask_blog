Title: Incontournables Pythonerie : ImportError: No module named 'xxx' dans un virtualenv
Date: 2013-11-05 16:22
Author: foxmask
Category: Techno
Tags: python, pythonerie
Slug: incontournables-pythonerie-importerror-no-module-named-dans-un-virtualenv
Status: published

Ça pourrait s'intituler "C'est l'histoire d'un mec... qu'est su' l'pont
de l'Alma pi qui regarde dans l'eau et qui dit \*j'ai fait tomber mes
lunettes dans la Loire\*"

Une histoire d'un biglotron quoi.

Donc voilà .

On se fait un script python qui marche au quart de poil et pour le
coller sur un serveur en prod on se dit que quand même si on l'intégrait
dans un virtualenv ça serait 'ach'ment mieux à gérer.

je m'en vais donc me faire ce virtualenv tout QQ

```python
foxmask@localhost:~/virtualenv/apps/$ virtualenv toto
New python executable in toto/bin/python
Installing distribute.............................................................................................................................................................................................done.
Installing pip...............done.

foxmask@localhost:~/virtualenv/apps/$ cd $_
foxmask@localhost:~/virtualenv/apps/toto$ 
(toto)foxmask@localhost:~/virtualenv/apps/toto$ source bin/activate
(toto)foxmask@localhost:~/virtualenv/apps/toto$ mkdir tata
(toto)foxmask@localhost:~/virtualenv/apps/toto$ cd $_
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ cp ~/monscriptdelamort.py .
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ cp ~/requirements.txt .
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ cat requirements.txt 
Genshi==0.7
distribute==0.6.24
lxml==3.2.3
relatorio==0.6.0
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ pip install -r requirements.txt
```

je vous passe la compilation de lxml ...

```python
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ pip freeze --local
Genshi==0.7
distribute==0.6.24
lxml==3.2.3
relatorio==0.6.0
```

et là où ça devient intéressant c'est quand je lance
monscriptdelamort.py  
et qu'il me sort la superbe erreur :

```python
    from relatorio.templates.opendocument import Template
ImportError: No module named relatorio.templates.opendocument
```

or comme on le voit au dessus il est bien là ce module  
de même que

```python
(toto)foxmask@localhost:~/virtualenv/apps/toto/tata$ python
>>> import relatorio.templates.opendocument
>>> print (relatorio.templates.opendocument)

>>> 
```

ça t'en bouche un coin public hein ?

Au bout d'un long moment à tourner en rond autour de la poubelle de la
machine à café en panne (elle aussi)  
je rouvre mon script et vois la lumière sur la ligne 1 :

```python
#!/usr/bin/python
```

hé oué public t'as tout compris .  
Comme dis au début ; j'ai fait le script avant de l'intégrer dans un
virtualenv donc quand je le lancais, j'appelais le binaire python
outside of ze Virtualenv ...

A bientôt pour une nouvelle bourde "inside".

