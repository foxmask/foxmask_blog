Title: Tuto linux : trouver le process qui a ouvert un port
Date: 2015-08-05 10:45
Author: foxmask
Category: Techno
Tags: linux
Slug: tuto-linux-trouver-le-process-qui-a-ouvert-un-port
Status: published

A qui ca n'est pas arrivé de voir un process se planter parce que "port
already bound" ...

Comment repérer le process qui a ouvert le port dont on a besoin ?

imaginons les ports 8009 et 8080

on commence par un

```shell
$ netstat -an|grep 8009
tcp        0      0 0.0.0.0:8009                0.0.0.0:*                   LISTEN      
tcp        0      0 127.0.0.1:8009              127.0.0.1:15561             ESTABLISHED 
tcp        0      0 127.0.0.1:15477             127.0.0.1:8009              ESTABLISHED 

$ netstat -an|grep 8080
tcp        0      0 0.0.0.0:8080                0.0.0.0:*                   LISTEN      
tcp        0      0 127.0.0.1:8080              127.0.0.1:60159             ESTABLISHED 
tcp        0      0 127.0.0.1:58230             127.0.0.1:8080              TIME_WAIT   
```

pour s'assurer que ces ports soient bien ouverts, histoire de voir qu'on
a bien les yeux en face des trous

Ensuite je vais pour utiliser **lsof** :

```shell
$ lsof -i |grep 8009 

httpd     20944     apache   14u  IPv4 48859942      0t0  TCP localhost:15588->localhost:8009 (ESTABLISHED)
httpd     20945     apache   14u  IPv4 48858055      0t0  TCP localhost:15478->localhost:8009 (ESTABLISHED)
java      23193      jboss  283u  IPv4 48833112      0t0  TCP *:8009 (LISTEN)
java      23193      jboss  830u  IPv4 48858029      0t0  TCP localhost:8009->localhost:15473 (ESTABLISHED)
java      23193      jboss  833u  IPv4 48858251      0t0  TCP localhost:8009->localhost:15487 (ESTABLISHED)
```

Parfait je vois qui m'enquiquine sur ce port j'ai le pid 23193 :P

puis la meme pour le port 8080

```shell
$ lsof -i|grep 8080
$ 
```

mais là, rien ne s'affiche, wtf ?

c'est parce que lsof -i affiche les process ayant ouvert des ports dont
les services sont "connus" de `/etc/services`

donc d'abord il faut faire un

```shell
$ grep 8080 /etc/services 

webcache        8080/tcp        http-alt        # WWW caching service
webcache        8080/udp        http-alt        # WWW caching service
```

pour localiser le NOM dudit service lié au port 8008, puis on conclut
par

```shell
$ lsof -i |grep webcache
java      23193      jboss  284u  IPv4 48833113      0t0  TCP *:webcache (LISTEN)
```

et voilà j'ai trouvé mes coupables ;)

