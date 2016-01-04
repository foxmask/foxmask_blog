Title: fabric ImportError: No module named main
Date: 2013-10-24 16:38
Author: foxmask
Category: Techno
Tags: fabric, python
Slug: fabric-importerror-no-module-named-main
Status: published

Voici peut-être une nouvelle série de billets sur Fabric cette fois ci
avec des retours d'xp des plus couillons au moins balot ;)  
Donc comme chaque nouveau sujet que je découvre je "partage" les
aneries de débutant, histoire de bien faire marrer la grand majorité des
pro du Python mais rassurer les autres débutants comme mézigues ;)

Ainsi donc, avec
[Fabric](http://fabric.org "Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks."),
me voilà à la découverte d'un nouveau monde.

Ce billet sera *rikiki pouce-pouce* puisque ne concernera qu'un problème
con comme là lune :

```python
ImportError: No module named main
```

Ce dernier se produit au lancement de fabric .. pratique ... à débuger
comme ça ... même avec la stacktrace plus bas ;)

J'ai installé un virtualenv qui a cette allure :

```shell
(install_release)foxmask@localhost:~/apps/install_release$ ls -l
total 52
drwxr-xr-x 3 foxmask foxmask  4096 oct.  24 16:15 autodeploy
drwxr-xr-x 2 foxmask foxmask  4096 oct.  24 16:02 bin
drwxr-xr-x 2 foxmask foxmask  4096 oct.  24 16:04 fabric
drwxr-xr-x 2 foxmask foxmask  4096 oct.  23 14:43 include
-rw-r--r-- 1 foxmask foxmask    93 oct.  24 16:17 __init__.py
-rw-r--r-- 1 foxmask foxmask   118 oct.  23 14:56 install_release.sublime-project
-rw-r--r-- 1 foxmask foxmask 19863 oct.  23 17:03 install_release.sublime-workspace
drwxr-xr-x 3 foxmask foxmask  4096 oct.  23 14:43 lib
drwxr-xr-x 2 foxmask foxmask  4096 oct.  23 14:43 local
```

en me rendant dans mon dossier fabric et en tapant une commande *fab
foobar*

je me mange systématiquement

```python
Traceback (most recent call last):
  File "/home/foxmask/apps/install_release/bin/fab", line 9, in 
    load_entry_point('Fabric==1.8.0', 'console_scripts', 'fab')()
  File "/home/foxmask/apps/install_release/local/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg/pkg_resources.py", line 337, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/home/foxmask/apps/install_release/local/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg/pkg_resources.py", line 2279, in load_entry_point
    return ep.load()
  File "/home/foxmask/apps/install_release/local/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg/pkg_resources.py", line 1989, in load
    entry = __import__(self.module_name, globals(),globals(), ['__name__'])

ImportError: No module named main
```

Mais en y regardant de plus près... ma structure de folders, qu'on voit
2 paragraphes plus haut, ne colle pas du tout ...

alors qu'ici

```shell
(install_release)foxmask@localhost:~/apps/install_release$ ls -l
total 44
drwxr-xr-x 2 foxmask foxmask  4096 oct.  24 16:02 bin
drwxr-xr-x 2 foxmask foxmask  4096 oct.  23 14:43 include
drwxr-xr-x 4 foxmask foxmask  4096 oct.  24 16:18 install_release
-rw-r--r-- 1 foxmask foxmask   118 oct.  23 14:56 install_release.sublime-project
-rw-r--r-- 1 foxmask foxmask 19863 oct.  23 17:03 install_release.sublime-workspace
drwxr-xr-x 3 foxmask foxmask  4096 oct.  23 14:43 lib
drwxr-xr-x 2 foxmask foxmask  4096 oct.  23 14:43 local
(install_release)foxmask@localhost:~/apps/install_release$ ls -l install_release
total 12
drwxr-xr-x 3 foxmask foxmask 4096 oct.  24 16:15 autodeploy
drwxr-xr-x 2 foxmask foxmask 4096 oct.  24 16:18 fabric
-rw-r--r-- 1 foxmask foxmask   93 oct.  24 16:17 __init__.py
```

elle convient bien mieux et fab est content avec son pitit message
"done" final qui me sied tout autant. :)

