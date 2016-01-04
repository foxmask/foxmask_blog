Title: Python pip freeze by noob
Date: 2012-09-10 21:57
Author: foxmask
Category: Techno
Tags: Django
Slug: python-pip-freeze
Status: published

Dans la série je découvre les joies de python, voici un très court
billet sur l'utilisation de pip [à la suite de ce très instructif billet
de Sam et Max](http://sametmax.com/votre-python-aime-les-pip/) où on
apprend qu'on peut produire son propre fichier requirements.txt
recensant les modules utilisés pour son
[virtualenv](http://pypi.python.org/pypi/virtualenv). Le but de la
manoeuvre étant d'éviter de se coltiner les réinstallations à
l'identique sur des virtualenv / serveurs distincts.

Donc tout content de mettre en pratique je me lance la commande comme
suit :  

` foxmask@foxmask:~$ cd Django-VirtualEnv/django-huanui foxmask@foxmask:~/Django-VirtualEnv/django-huanui$ pip freeze --local > requirements.txt`  
ce qui me donne comme requirements.txt :  

` Axiom==0.6.0 BeautifulSoup==3.1.0.1 Brlapi==0.5.5 ClientForm==0.2.10 Coherence==0.6.6.2 Epsilon==0.6.0 GnuPGInterface==0.3.2 Louie==1.1 Mako==0.3.4 MarkupSafe==0.9.2 MySQL-python==1.2.2 Nevow==0.10.0 PAM==0.4.2 PIL==1.1.7 PyOpenGL==3.0.1b2 Twisted-Conch==10.1.0 Twisted-Core==10.1.0 Twisted-Web==10.1.0 apt-xapian-index==0.41 chardet==2.0.1 configobj==4.7.2 cups==1.0 distribute==0.6.14 feedparser==4.1 gdata==2.0.8 gnome-app-install==0.4.7-nmu1 httplib2==0.6.0 louis==2.0.0 mechanize==0.1.11 mercurial==1.6.4 numpy==1.4.1 pep8==0.5.0 pexpect==2.3 pyOpenSSL==0.10 pyasn1==0.0.11a pycrypto==2.1.0 pyserial==2.3 pysqlite==2.6.0 python-apt==0.7.100.1-squeeze1 python-debian==0.1.18-squeeze1 pyxdg==0.19 rdflib==2.4.2 reportbug==4.12.6 rope==0.9.2 tagpy==0.94.7 uTidylib==0.2 unattended-upgrades==0.1 virtualenv==1.4.9 wsgiref==0.1.2 zope.interface==3.5.3`  
Oula mais ça me va pas cette ribambelle de modules, but wtf ?

Bon ben comme les pros du pot l'ont déjà vu ; faute de débutant
flagrante.

Quand on se créé un virtualenv on n'utilise les scripts qui sont dans ce
dernier, donc dans mon cas ici :  
`~/Django-VirtualEnv/django-huanui/bin/`

donc on la refait :  

` foxmask@foxmask:~/Django-VirtualEnv/django-huanui$ ./bin/pip freeze --local > requirements.txt`  
et cette fois ci on respire, la "pollution" environnementale s'est
dissipée :  

` foxmask@foxmask:~/Django-VirtualEnv/django-huanui$ cat requirements.txt Django==1.4.1 distribute==0.6.10 django-debug-toolbar==0.9.4 django-profiles==0.2 django-registration==0.8 django-relationships==0.3.2`  
nota: si on ne colle pas le --local on "ramasse" tous les modules
précédents

edit : vu ce weekend à [PyConFr](http://www.pycon.fr/ "PynConFr") grâce
à [@Dzen](http://twitter.com/dzen) ;) pour ne plus se prendre le chou
avec  
` ./bin/pip`  
ou autre  
`../bin/bin/pip blabla `  
dans le dossier de son virtualenv on tape betement  
`source bin/activate`  
et les variables d'environnement feront leur boulot pour que tout soit
relatif à votre environnement virtuel \_\_avant\_\_ celui de la machine
courante

