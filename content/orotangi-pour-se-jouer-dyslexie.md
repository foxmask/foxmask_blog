Title: Orotangi, pour se jouer de la dyslexie
Date: 2017-04-25 16:00
Author: foxmask
Category: Techno
Slug: orotangi-pour-se-jouer-dyslexie
Status: published

# intro

Je me suis lancé dans un nouveau projet, de prises de notes à la Evernote, qui sera loin de couvrir tout cette dernière offre mais pour l'heure ce n'est pas le but.

Un sujet qui me tient à coeur ici, c'est qu'il me faut absolument la gestion de la police de caractères OpenDyslexic. En effet, "n°2" est concerné et c'est vraiement un plaie à gérer pour sa scolarité. J'ai le pot d'avoir un collège qui a un protocol pour les dyslexiques, et là c''est génial, mais il faut pousser plus loin. 
Par ailleurs il existe des associations pour dyslexiques dont [Ordyslexie](https://www.ordyslexie.fr/page/42731-accueil) qui recycle des ordinateurs pour les reconditionner et fournir aux adhérents, moyennant un certain budget, "un cartable numerique" où l'élève dyslexique, fini par être plus rapide que son camarade non dyslexique. Seulement pour obtenir ce "cartable" il y a des démarches medicales et l'achat du "cartable", dont le coût s'envole grâce à la licence Microsoft OneNote...

Du coup face, à ça, alors que Bill Gates (l'homme le plus riche du monde?) a monté une fondation (sans aucun rapport:), il aurait au moins pu laisser courir sur la licence de OnteNote...,  je me suis lancé dans ce projet aux antipodes de ce que je fais habituellement.


# Le "bidule" (projet) inclura donc :

Une prise de note facilité avec un éditeur "tout pret" avec l'utilisation de la police OpenDyslexic (ou non selon ce que chacun voudra)
Du Text To Speech / Speech To Text, que le texte mis dans l'editeur soit lu au gamin (en surlignant mot à mot si possible), ou que le gamin parle et que ca enregistre ce qu'il dit dans une note.
Les Dyslexiques n'étant pas tous identiques, chacun adaptera l'outil selon ce qui lui rendra service. Par exemple la police OpenDyslexic, pour certains d'entre eux n'est pas agréable, donc ils pourront retourner à une police "classique".
Plus tard j'aimerai bien, comme ce que fait Ordyslexie, scanner des doc pour écrire directement dedans :) ou qu'après le scan, l'appli enregistre le texte dans une note pour que le TextToSpeech fasse la lecture du contenu.

# la Dyslexie et des "génies"

Enfin à celles et ceux qui penseraient que les dyslexiques ne sont pas des lumières (vous en connaissez forcement 2, les plus célèbres qui soit) et que "c'est rien, c'est passager" . Il n'en est rien :

Voici quelques témoignages sur [Ted](https://ted.com) :

* [Overcoming Dyslexia, Finding Passion](https://www.youtube.com/watch?v=ugFIHHom1NU)
* [The True Gifts of a Dyslexic Mind](https://www.youtube.com/watch?v=_dPyzFFcG7A)


# Free at last we are free at last

Comme à mon habitude, ce projet est libre et je ne serai pas contre un peu d'aide si vous vous y connaissez un peu avec :

* [Django Rest Framework](http://www.django-rest-framework.org/)
* [VueJS](https://vuejs.org)
* l'UX adapté aux dyslexiques  (même si vous n'y connaissez rien en dyslexie mais en UX je prends quand même ; de nombreux sites expliquent ce qu'on ne doit pas faire dans une page pour eux)

Et comme "qui peut le plus peu le moins", ce projet devrait être utilisable pour tout le monde (par le biais de préférences / paramètrages)


# Checkpoint

[Les sources sont là](https://github.com/orotangi)

En l'état actuel le projet permet d'ajouter des notes, d'importer des notes Evernote, de les afficher avec un éditeur Markdown (mais je pense le retirer parce que je ne m'imagine pas un enfant taper du markdown plus facilement que surligner le texte et sélectionner la mise en forme qui va bien, ou à défaut de le retirer, permettre par un paramètrage, d'utiliser l'editeur Markdown ou CKEditor/TinyMCE par exemple)

Quand le projet sera mûr pour une première version, je ne pourrai que vous proposer de l'installer chez vous, je ne pourrai pas l'héberger comme ce que je fais pour un autre projet.
Mais aucune crainte à avoir, la documentation sera là pour vous y aider :)

# End

Cela sera mon 2nd projet qui vous permettra une nouvelle fois, de prendre le contrôle de vos données en les sortant des compagnies qui vous font payer pour ce service, Evernote s'étant illustrée en novembre dernier en s'occtroyant le prvilège de lire nos notes (avant de se raviser après que de nombreux clients aient manifesté leur mécontentement) ...  ca sera la reponse du berger à la bergère du même coup :)

