Title: Quand Fabric refuse de bosser
Date: 2018-01-23 16:45
Author: foxmask
Category: Techno
Tags: python, Fabric,
Slug: quand-fabric-refuse-bosser
Status: published


Un comportement completement fou se produit pour moi avec Fabric, il n'execute absolument pas une `command` (run ici) en se faisant jetter par le serveur où il devrait executer celle ci...



Je pose ça là vite fait pour qui rencontrerait le problème à son tour

J'ai un script, le plus con du monde qui execute la commande id sur le serveur de mon choix, comme suit :

```python
# coding: utf-8
from fabric.api import env, local, run, settings
from fabric.colors import blue, yellow

env.user = 'root'
env.password = 'root'

def the_log(f):
    def new_f(server):
        msg = "[{0}] {1}".format(server, f.__doc__)
        print(blue(msg))
        f(server)

    return new_f


@the_log
def main(server):
    """This is my main function that will triggers anything"""

    with settings(warn_only=True):

        output = local("id")
        print(yellow(output))

        output = run("id",
                     shell=True,
                     combine_stderr=True)
        print(blue(output))
```

Quand ce script tourne il fait :

```bash
[foxmask:~/DjangoVirtualEnv/monitoring/monitoring] [monitoring] $ fab main:server=server1 -H server1
[server1] Executing task 'main'
[server1] This is my main function that will triggers anything
[localhost] local: id
uid=1000(foxmask) gid=1000(foxmask) groupes=1000(foxmask),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),100(users),103(scanner),112(netdev)

[server1] run: id


```

on voit le resultat des 2 commandes... la seconde ne fonctionne pas et pourtant un ssh passe lui

```bash
ssh root@server1 id
uid=0(root) gid=0(root) groupes=0(root)
```

après avoir écrèmé la toile à la recherche de config SSH que j'aurai raté, je testé le meme script sur un serveur. 
Et la entre serveurs tout passe.
La difference avec ma station, OpenSSH 7.1 vs OpenSSH 5.3
Donc me dis que c'est quand même gonflé qu'une diff d'openssh me mette dedans
Je mets à jour OpenSSH sur la Redhat mais j'arrive tout juste à la 5.3.13.

Je mets du PDB partout pour voir qu'est-ce qui n'irait pas.
Et je tombe sur cette page [http://www.fabfile.org/troubleshooting.html?highlight=ssh](http://www.fabfile.org/troubleshooting.html?highlight=ssh)

Où je fais un bon copier coller du code sous le paragraphe "Enable Paramiko-level debug logging"
Et là à l'execution ca donne :

```bash

[foxmask:~/DjangoVirtualEnv/monitoring/monitoring] [monitoring] $ fab -f main main:server=server1 -H server1 -p pass1
[server1] Executing task 'main'
[server1] This is my main function that will triggers anything
[localhost] local: id
uid=1000(foxmask) gid=1000(foxmask) groupes=1000(foxmask),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),100(users),103(scanner),112(netdev)

[server1] run: id
DEBUG:paramiko.transport:starting thread (client mode): 0x66aed748
DEBUG:paramiko.transport:Local version/idstring: SSH-2.0-paramiko_2.4.0
DEBUG:paramiko.transport:Remote version/idstring: SSH-2.0-OpenSSH_5.3
INFO:paramiko.transport:Connected (version 2.0, client OpenSSH_5.3)
DEBUG:paramiko.transport:kex algos:['diffie-hellman-group-exchange-sha256', 'diffie-hellman-group-exchange-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1'] server key:['ssh-rsa', 'ssh-dss'] client encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] server encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] client mac:['hmac-md5', 'hmac-sha1', 'umac-64@openssh.com', 'hmac-sha2-256', 'hmac-sha2-512', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] server mac:['hmac-md5', 'hmac-sha1', 'umac-64@openssh.com', 'hmac-sha2-256', 'hmac-sha2-512', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] client compress:['none', 'zlib@openssh.com'] server compress:['none', 'zlib@openssh.com'] client lang:[''] server lang:[''] kex follows?False
DEBUG:paramiko.transport:Kex agreed: diffie-hellman-group-exchange-sha256
DEBUG:paramiko.transport:HostKey agreed: ssh-rsa
DEBUG:paramiko.transport:Cipher agreed: aes128-ctr
DEBUG:paramiko.transport:MAC agreed: hmac-sha2-256
DEBUG:paramiko.transport:Compression agreed: none
DEBUG:paramiko.transport:Got server p (2048 bits)
DEBUG:paramiko.transport:kex engine KexGexSHA256 specified hash_algo <built-in function openssl_sha256>
DEBUG:paramiko.transport:Switch to new keys ...
DEBUG:paramiko.transport:Trying discovered key b'8fbb1c6beb76bcc6767eccfcbef3730e' in /home/foxmask/.ssh/id_rsa
DEBUG:paramiko.transport:userauth is OK
INFO:paramiko.transport:Authentication (publickey) failed.

```
du coup me v'la frais avec un paramiko qui met son caca en trouvant bien que l'userauth est ok mais pas la publickey. Ca te ferait mal de me laisser passer puisque tu as vu que le user/pass etait ok ?

Etape suivante, trouver comment forcer [SSH à utiliser le mot de passe et basta](https://serverfault.com/questions/283722/authentication-order-with-ssh) ... 

Je n'ai pas encore mis la main sur une solution , je mettrai à jour si j'en trouve une d'ici là :)


@Tchao :)
