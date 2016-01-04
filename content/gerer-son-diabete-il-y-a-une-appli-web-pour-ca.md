Title: Gérer son Diabète, il y a une appli web pour ça
Date: 2014-06-29 21:27
Author: foxmask
Category: Techno
Tags: dj-diabetes, Django, python
Slug: gerer-son-diabete-il-y-a-une-appli-web-pour-ca
Status: published

En ce weekend de merde (pourri pluvieux) et envie de faire l'ermite, je
me suis occupé en rendant un service sur une migration WordPress, et ai
produit une application pour gérer son quotidien de diabétique.  
Non que je ne le sois, mais je m'ennuyais et ai demandé à un pote : "si
tu avais du temps, quelles applications développerais tu ?"

Les réponses furent :

1.  un client IRC web avec des fonctions que je tairais pour l'heure,
2.  une application pour enregistrer des métriques du quotidien de
    diabétiques

A partir du MCD qu'il m'a fourni j'ai produis
"[dj-diabetes](https://github.com/foxmask/dj-diabetes)" avec
[Django](https://www.djangoproject.com/) et
[bootstrap3](http://getbootstrap.com/) .

Le but étant de savoir, pour le pote, à quel moment il est le "mieux".  
Que ça soit après un exercice, après ou avant un repas etc.

Avec ces informations, il peut voir le doc' avec des infos précises et
affiner le traitement.

En image ça donne ça

[![My Glucose Manager](/static/2014/06/glucose_manager-1024x771.png)](/static/2014/06/glucose_manager.png)

[![My Glucose Manager - Les Examens](/static/2014/06/glucose_manager_exams-1024x782.png)](/static/2014/06/glucose_manager_exams.png)


Aparté :  
Techniquement, aux amis poneys, j'ai dû m'éclater la tête contre les
[inlineformset\_factory](https://github.com/foxmask/dj-diabetes/blob/master/dj_diabetes/forms.py#L189)
dans des
[CBV](https://github.com/foxmask/dj-diabetes/blob/master/dj_diabetes/views.py#L617)
avec des ModelForm.

Je referai un billet sur les formset plus tard, là c'était juste pour
présenter l'appli elle même ;)

ps : l'appli est en constante évolution puisque tout fraiche. Si vous
l'utilisez/testez et trouvez des soucis [ouvrez un
ticket](https://github.com/foxmask/dj-diabetes/issues/new) afin que je
regarde ce qu'il en est.

