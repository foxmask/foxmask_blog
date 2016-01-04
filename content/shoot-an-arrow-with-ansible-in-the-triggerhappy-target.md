Title: Shoot an Arrow with Ansible in the TriggerHappy target
Date: 2015-08-24 10:57
Author: foxmask
Category: Techno
Tags: ansible, Django, python, TriggerHappy
Slug: shoot-an-arrow-with-ansible-in-the-triggerhappy-target
Status: published

Create a module for participating to TriggerHappy is now so simple that
I cant imagine to make a new one without this new little module named
"Trigger Happy Ansible"

What does it do ?

Well, as anyone can imagine, when you start a django project you enter,

```shell
python manage.py startproject 
```

when you start a new app you enter :

```shell
python manage.py startapp
```

thus you will have a new empty module with a lot a "empty" files.

To speed up the creation of a Trigger Happy module, first I made a
simple module
[django-th-dummy](https://github.com/foxmask/django-th-dummy) that
provides a module ready to use , but that need to be customized to be
used.

So I went a little far away and now you can just enter

```shell
ansible-playbook -i hosts site.yml
```

and that's all !

a new TriggerHappy module is ready to be installed in the middle of all
the others ones.

Under the hood, what has been done ?

You need to install ansible, then setup the site.yml file to change all
the variables that fit your needs and once the playbook is played, a new
folder will be created with everything needed by TriggerHappy

Here is the
[site.yml](https://github.com/foxmask/django-th-ansible/blob/master/site.yml)
file.

The lines to be changed are those ones :

```yaml
  vars:
    # to directory tree and class/module/name purpose
    module_name: johndoe
    service_name: johndoe
    class_name: Johndoe

    # for setup.py purpose
    author: John Doe
    author_email: john@doe.com
    description: this is a module that is fun
    details: when fun is higher than anything
    url: https://github.com/foxmask/django-th-johndoe
    download_url: https://github.com/foxmask/django-th-johndoe/archive/trigger-happy-johndoe-

    # for dependencies purpose
    external_api: foobar
    external_api_class: Foobar
    external_api_version: 1.2.3
```

as you can see, I separated variables by usage domain

And here is the output of the running ansible playbook

```shell
ansible-playbook -i hosts site.yml

    PLAY [home-sweet-home] ******************************************************** 

    GATHERING FACTS *************************************************************** 
    ok: [localhost]

    TASK: [dummy | create folder of the module name] ****************************** 
    changed: [localhost]

    TASK: [dummy | create tests folder of the module name] ************************ 
    changed: [localhost]

    TASK: [dummy | travis.yml] **************************************************** 
    changed: [localhost]

    TASK: [dummy | gitignore] ***************************************************** 
    changed: [localhost]

    TASK: [dummy | copy of th_dummy/__init__.py] ********************************** 
    changed: [localhost]

    TASK: [dummy | copy of th_dummy/tests/__init__.py] **************************** 
    changed: [localhost]

    TASK: [dummy | copy of LICENSE] *********************************************** 
    changed: [localhost]

    TASK: [dummy | copy of MANIFEST.in] ******************************************* 
    changed: [localhost]

    TASK: [dummy | copy of setup.py] ********************************************** 
    changed: [localhost]

    TASK: [dummy | copy of README.rst] ******************************************** 
    changed: [localhost]

    TASK: [dummy | copy of requirements.txt] ************************************** 
    changed: [localhost]

    TASK: [dummy | copy of my_dummy.py to my_{{ module_name }}.py] *************** 
    changed: [localhost]

    TASK: [dummy | copy of model.py] ********************************************** 
    changed: [localhost]

    TASK: [dummy | copy of forms.py] ********************************************** 
    changed: [localhost]

    TASK: [dummy | copy of test.py] *********************************************** 
    changed: [localhost]

    TASK: [dummy | copy of the templates] ***************************************** 
    changed: [localhost]

    PLAY RECAP ******************************************************************** 
    localhost                  : ok=17   changed=16   unreachable=0    failed=0   

    (triggerhappy-bootstrap)foxmask@zorro:~/Django-VirtualEnv/django-th-ansible$ ls -ltR django-th-johndoe/
    django-th-johndoe/:
    total 24
    drwxr-xr-x 4 foxmask foxmask 4096 août  23 16:28 th_johndoe
    -rw-r--r-- 1 foxmask foxmask   14 août  23 16:28 requirements.txt
    -rw-r--r-- 1 foxmask foxmask 1368 août  23 16:28 README.rst
    -rw-r--r-- 1 foxmask foxmask 1186 août  23 16:28 setup.py
    -rw-r--r-- 1 foxmask foxmask  194 août  23 16:28 MANIFEST.in
    -rw-r--r-- 1 foxmask foxmask 1484 août  23 16:28 LICENSE

    django-th-johndoe/th_johndoe:
    total 28
    drwxr-xr-x 2 foxmask foxmask 4096 août  23 16:28 tests
    -rw-r--r-- 1 foxmask foxmask  471 août  23 16:28 forms.py
    -rw-r--r-- 1 foxmask foxmask  614 août  23 16:28 models.py
    -rw-r--r-- 1 foxmask foxmask 6424 août  23 16:28 my_johndoe.py
    -rw-r--r-- 1 foxmask foxmask   81 août  23 16:28 __init__.py
    drwxr-xr-x 3 foxmask foxmask 4096 août  23 16:28 templates

    django-th-johndoe/th_johndoe/tests:
    total 4
    -rw-r--r-- 1 foxmask foxmask 3725 août  23 16:28 test.py
    -rw-r--r-- 1 foxmask foxmask    0 août  23 16:28 __init__.py

    django-th-johndoe/th_johndoe/templates:
    total 4
    drwxr-xr-x 2 foxmask foxmask 4096 août  23 16:28 th_johndoe

    django-th-johndoe/th_johndoe/templates/th_johndoe:
    total 20
    -rw-r--r-- 1 foxmask foxmask 1277 août  23 16:28 edit_provider.html
    -rw-r--r-- 1 foxmask foxmask 1277 août  23 16:28 edit_consumer.html
    -rw-r--r-- 1 foxmask foxmask 1513 août  23 16:28 wz-3-form.html
    -rw-r--r-- 1 foxmask foxmask 1513 août  23 16:28 wz-1-form.html
    -rw-r--r-- 1 foxmask foxmask  382 août  23 16:28 callback.html
```
