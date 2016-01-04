Title: Ansible : les variables définies à la volée
Date: 2015-08-11 10:45
Author: foxmask
Category: Techno
Tags: ansible, python
Slug: ansible-les-variables-definies-a-la-volee
Status: published

**Ansible : comment définir des variables à la volée dans son playbook**

Imaginons que j'ai besoin de définir des variables au fur et à mesure
que le processus avance

Cas concret déployer des WAR issues d'une "nightly build" depuis des
repo maven :

je demarre par une tâche allant à la pêche aux SNAPSHOT

```yaml
- name: Find last snapshot
  command: ssh {{ server_repo }} ls -d {{ maven_repository }}/standard/{{ branch }}.*-SNAPSHOT | sort
  register: snapshot
```

ici *register* va me permettre d'utiliser "snapshot" par la suite.
Disons *command* m'a permit de trouver FOOBAR-1.2.3-SNAPSHOT

```yaml
- name: let's define "war_path"
  command: echo {{ path }}{{ snapshot.stdout | basename }}.war
  when: snapshot
  register: war_path
```

ici 2 choses et une astuce :

1\) j'utilise de nouveau *register* pour pouvoir télécharger le war plus
tard
2) j'utilise *when* ce qui permet de ne faire la *command* que quand la
tasks ***snapshot*** est *register*ed
3) l'astuce : utiliser *command* comme si on avait fait un simple
export FOO=BAR, et sur la ligne de *command* on utilise
*snapshot.stdout* parce qu'on a *register* *snapshot* précédement qui
n'est qu'une chaine et pas une liste.
Ce qui, avec les filtres "basename" et la concaténation avec ".war ",
me donne grosso modo comme résultat un tout QQ :

```shell
  echo /un/jolie/path/FOOBAR-1.2.3-SNAPSHOT.war
```

tâche suivante :

```yaml
- name: war_path download from server_repo
  command: scp -pr {{ server_repo }}:{{ war_path.stdout }} /temp
  when: war_path
```

ici un simple scp, on remarquera *war\_path* qui est la tasks *register*
juste au dessus et le *when* qui utilise *war\_path*

```yaml
- name: war_path check is here
  stat: path=/temp/{{ war_path.stdout | basename}}
  register: war_path_exists
```

ici vérification que le transfert a eu lieu

```yaml
- name: war_path fail to download
  fail: file /temp/{{ war_path.stdout | basename}} does not exists
  when: war_path_exists.stat.exists == False
```

ici on peut vérifier que ça a foiré, on se contente d'un message
d'erreur mais on aurait pu faire péter un mail au service IT :P

```yaml

- name: war_path Extract
  command: chdir={{ home }}/{{ target }}-tomcat/webapps/{{ foobar }} {{ java_home }}/bin/jar xf /temp/{{ war_path.stdout | basename }}
  when: war_path
```

et on acheve par la décompression du war

je vous fais grâce du restart tomcat :)

Pour finir, [un petit gist qui fait joujou avec uniquement des variables
à base de echo :)](https://gist.github.com/foxmask/b3c958169933e044f7b0)

