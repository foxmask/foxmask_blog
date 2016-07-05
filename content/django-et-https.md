Title: Django et HTTPS
Date: 2016-07-03 22:00
Author: foxmask
Category: Techno
Tags: Django, HTTPS
Slug: django-et-https
Status: published


Un rapide billet pour poser ici un retour de prise de tête :)


Avec la venue de [LetsEncrypt](https://letsencrypt.org/), il va fleurer bon les sites en HTTPS de ci de là.

Par contre une fois mis en place en prod, coté dev il arrive qu'on fasse un hack vite fait pour pas passer 3 plombes sur sa conf nginx comme ça :


```bash

export HTTPS=on
./manage.py runserver

```

et roule ma poule !


Bon en prod par contre on ne va pas s'amuser à ca quand on a un NGINX en frontal du Gunicorn par exemple.

Et si on laisse en etat, au final tout accès à request.scheme vous retournera dans les dents un casse-burette 'http'.

Donc en suivant [la doc](https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER) on modifie son settings en rajoutant 

```python

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

```

mais ça ne suffit toujours pas. Nginx renverra encore et toujours du HTTP...

donc à sa conf toute QQ 

```ini

location / {
        add_header           Front-End-Https    on;
        add_header Cache-Control "public, must-revalidate";
        add_header Strict-Transport-Security "max-age=2592000; includeSubdomains";
        proxy_pass http://127.0.0.1:8080; # Pass to Gunicorn
        proxy_next_upstream error timeout invalid_header;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Host $host;
    }


```

on rajoutera 



```ini

proxy_set_header        X-Forwarded-Proto $scheme;

```

pour obtenir : 

```ini

location / {
        add_header           Front-End-Https    on;
        add_header Cache-Control "public, must-revalidate";
        add_header Strict-Transport-Security "max-age=2592000; includeSubdomains";
        proxy_pass http://127.0.0.1:8080; # Pass to Gunicorn
        proxy_next_upstream error timeout invalid_header;
        proxy_set_header        Host            $host;
        proxy_set_header        X-Real-IP       $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Host $host;
        proxy_set_header        X-Forwarded-Proto $scheme;
    }


```


Et là au joie, on obtiendra bien un request.scheme vallant 'https'.


