Title: Ansible undefined variable : les yeux en face des trous
Date: 2022-05-06 07:24:15.561953+00:00
Author: FoxMaSk 

tags: ansible

Status: published





# Ansible undefined variable : les yeux en face des trous

[Ansible undefined variable : les yeux en face des trous](None)

Un petit post vite fait, sur un playbook qui deploie des war pour tomcat
, avec une surprise au bout 


```bash
foxmask@home:~/deploy$ ll
total 24
-rw-rw-r-- 1 foxmask foxmask   22 May  4 09:31 hosts.ini
drwxrwxr-x 4 foxmask foxmask   46 May  4 11:01 hosts_vars
-rw-rw-r-- 1 foxmask foxmask 6629 May  4 15:05 playbook.yml
-rw-rw-r-- 1 foxmask foxmask  849 May  4 15:05 README.md
drwxrwxr-x 4 foxmask foxmask   35 May  3 15:36 roles
```


```bash
$ ansible-playbook --check -i hosts.ini playbook.yml --extra-vars &#39;delivery_folder=delivery_20220506&#39;

PLAY [all] ******************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************************************************************
ok: [serverA]

TASK [backup : create lsq backup 202205060710] ******************************************************************************************************************************************************************************************
fatal: [serverA]: FAILED! =&gt; {&#34;msg&#34;: &#34;The conditional check &#39;wars&#39; failed. The error was: error while evaluating conditional (wars): {{ lsq.wars }}: &#39;lsq&#39; is undefined\n\nThe error appears to be in &#39;/home/foxmask/deploy/roles/backup/tasks/main.yml&#39;: line 12, column 3, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n\n- name: \&#34;create {{ what }} backup {{ today }}\&#34;\n  ^ here\nWe could be wrong, but this one looks like it might be an issue with\nmissing quotes. Always quote template expression brackets when they\nstart a value. For instance:\n\n    with_items:\n      - {{ foo }}\n\nShould be written as:\n\n    with_items:\n      - \&#34;{{ foo }}\&#34;\n&#34;}


PLAY RECAP ******************************************************************************************************************************************************************************************************************************
serverA             : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
```

Pourtant en vérifiant dans hosts_vars/serverA/vars.yml on trouve bien la variable ourself 

```yaml
---

lsq:
  wars:
    - portal
	- admin

```

dans le playbook.yml on a 

```yaml
    # BACKUP
    - name: &#34;backup date&#34;
      ansible.builtin.command: date +%Y%m%d%H%M
      register: date
      check_mode: no
      tags:
        - backup
        - lsq


    - name: backup lsq
      include_role:
        name: backup
      vars:
        what: lsq
        wars: &#34;{{ lsq.wars }}&#34;
        tomcat_root: &#34;{{ tomcat_home }}&#34;
        today: &#34;{{ date.stdout }}&#34;
      tags:
        - backup
        - lsq

```

Donc rien d&#39;extraordinaire, définition d&#39;une variable pour récupérer la date du jour puis la tâche suivante appelle un rôle en passant en parm les variables définies dans `hosts_vars/serverA/vars.yml`


Pour arriver à mes fins et trouver la source du problème j&#39;ai donc décidé, bon gré mal gré, de définir les variables dans playbook.yml et là ca marchait !

Après une grosse digestion, et en nettoyant mes lunettes... j&#39;ai mis le doigt sur l&#39;origine du pb de ansible.


```bash
foxmask@home:~/deploy $ ll
total 24
-rw-rw-r-- 1 foxmask foxmask   22 May  4 09:31 hosts.ini
drwxrwxr-x 4 foxmask foxmask   46 May  4 11:01 hosts_vars        &lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; !!!!!!!!!!! le dossier doit s&#39;appeler host_vars ...
-rw-rw-r-- 1 foxmask foxmask 6629 May  4 15:05 playbook.yml
-rw-rw-r-- 1 foxmask foxmask  849 May  4 15:05 README.md
drwxrwxr-x 4 foxmask foxmask   35 May  3 15:36 roles
```

et tout rentre dans l&#39;ordre :)

```bash
$ ansible-playbook --check -i hosts.ini playbook.yml --extra-vars &#39;delivery_folder=delivery_20220506&#39;

TASK [Gathering Facts] ******************************************************************************************************************************************************************************************************************
ok: [serverA]

TASK [backup : create lsq backup 202205060710] ******************************************************************************************************************************************************************************************
ok: [serverA]

PLAY RECAP ******************************************************************************************************************************************************************************************************************************
serverA             : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

tjs ce fameux probleme de layer8 ;)