Title: Django Trigger Happy 0.11.0
Date: 2015-08-17 14:00
Author: foxmask
Category: Techno
Tags: Django, python, TriggerHappy
Slug: django-trigger-happy-0-11-0
Status: published

Bonjour,  
Voici venue une petite mise à jour de mon petit projet, de micro ESB,
permettant d'orchestrer la récupération de données et leur publication,
le tout en exploitant vos propres services internet (comme Twitter pour
n'en citer qu'un). Juste histoire d'être maître de vos données sans
devoir donner vos autorisations d'accès à n'importe qui.  
([un rappel complet dispo à partir d'un talk @ django
Paris](http://trigger-happy.eu/static/django-paris-novembre-2014/))

Au programme des réjouissances :

<ol>
<li>
**Nouveautés Fonctionnelles**

-   Il est à présent possible de **produire des flux RSS** à partir de
    données, récupérées par un autre service qu'on se sera installé.  
    [![Services
    Installés](/static/2015/08/service_installe.png)](/static/2015/08/service_installe.png)
    Par exemple à partir du service twitter. Classiquement on fait un
    trigger publiant sur twitter, tout ce qui provient d'un site par
    exemple, europe-echecs, pour suivre l'actu échiquéenne. À présent on
    peut faire l'inverse. Suivre un hashtag \#chess, par exemple, et
    tout ce qui sera publié sur ce sujet, finira par être généré dans un
    flux RSS par TriggerHappy. J'adresse un petit coucou aux amis
    esseulés de **[yahoo pipes](https://pipes.yahoo.com/pipes/)** pour
    qui j'ai fait ceci, avec un appel du pied de sam&max ;-)
    </p>
-   **Intégration d'un nouveau service** :
    **[Trello](http://coreight.com/content/utiliser-trello-comme-un-pro)**.
    Ce service permet de gérer des projets en créant des tableaux de
    bord et pour chaque tableau de bord des listes de cartes. Cartes de
    "trucs" à faire pour organiser son projet. Pour la petite histoire,
    lors de mes tests, j'ai suivi le hashtag \#django en créant un
    trigger qui devait publier dans Trello, mais comme mon code ne
    marchait mais immédiatement, le trigger a accumulé plus de 200
    tweets qui sont arrivés dans un tableau de bord dédié et je pouvais
    voir en live dans trello arrivés les tweets un par un :-). Ce qui
    ajoute un jouet de plus au trousseau de clés : Twitter, Evernote,
    RSS, Readability, Pocket, Trello
-   **Un moteur de recherche** (basé sur haystack & elasticsearch). Ça
    n'est pas forcément du luxe quand on fini par avoir un grand nombre
    de triggers, des questions existentielles surgissent "j'avais
    pourtant bien créé un trigger qui parlait de recettes de cuisine
    Bretonne" ;-)
-   Une fonction "**vacances**" qui désactive tous les triggers, pour se
    mettre au vert pour de bon pendant ses vacances ! Ensuite quand vous
    revenez de vacantes vous désactivez le mode "vacances" ce qui
    réactivera que les triggers actifs avant le départ.

</li>
<li>
**Améliorations Techniques**

-   Plus de python 2 nulle part. Ce qui m'a "forcé" à trouver des
    solutions d'authentification différentes de la librairie oauth2 pour
    les services tels readability et Evernote. Un mal pour un bien !
    [requests
    oauthlib](https://requests-oauthlib.readthedocs.org/en/latest/) est
    la solution comme chacun s'en doutera :-)
-   Django 1.8.x (naturellement)
-   Réorganisation des modules par services dans une seule application
    Plutôt que d'avoir un dépôt par module, j'ai fini par tout regrouper
    dans le dépôt trigger-happy. Actuellement c'est pratique pour
    releaser et pour les tests unitaires, mais mon petit doigt me dit
    qu'à un moment je m'en mordrai les doigts.
-   Gestion d'une limite du nombre de publications à destination d'un
    service. Exemple : je publie sur twitter plus de 30 sites que je
    suis. À un moment donné les news de chacun d'eux affluent tellement,
    que je publie trop vite des news sur twitter, ce qui a pour effet de
    bord, de "pourrir" la timeline de mes amis followers, qui au lieu
    d'avoir une timeline hétérogène finisse par me haïr de publier plus
    vite que Lucky Luke. À présent "ça", c'est fini. On défini une
    limite et quand elle est atteinte on publie le reste plus tard,
    tranquille pépère.

</li>
<li>
**Performances**

-   je suis un éternel insatisfait de ce que je produis, même quand je
    fini un truc je me dis que je peux largement encore mieux faire.
    Dans cette optique donc, j'ai articulé le code en le basant sur le
    "[framework
    cache](https://docs.djangoproject.com/en/1.8/topics/cache/)" de
    django qui permet d'utiliser le backend de son choix. Ainsi, toute
    récupération de données des services est déposé dans le cache. Puis
    au moment de publier les données, TriggerHappy va le chercher dans
    le cache. Avant cela, tout était synchrone. [A
    présent](/post/2015/06/19/supervisor-celery-django-orchestration/)[Celery](http://celery.readthedocs.org/)
    orchestre ces récupérations de données et leurs publications</a>.

</li>
<li>
**[Documentation](http://trigger-happy.readthedocs.org/)**

-   mise à jour en long en large et en travers. N'hésitez pas un instant
    à la parcourir
-   Pour mettre à jour depuis la version précédente [tout est ici, une
    migration qui m'a pris du temps à
    finaliser](http://trigger-happy.readthedocs.org/en/latest/migration.html)

</li>
<ul>
</ol>
Et demain ? [de nouveaux
services](https://github.com/foxmask/django-th/labels/module) sont
prévus, et [quelques idées](https://github.com/foxmask/django-th/issues)
:)

J'en ai aussi profité pour réorganiser les tickets/labels/milestones sur
github, histoire de facilement trouver ce qu'on cherche, afin de
faciliter les
[contributions](https://github.com/foxmask/django-th/blob/master/CONTRIBUTING.md).

**Merci !**  
merci [à quelques
intéressés](https://github.com/foxmask/django-th/stargazers), [à
quelques curieux](https://github.com/foxmask/django-th/watchers) et
enfin [aux
contributeurs](https://github.com/foxmask/django-th/graphs/contributors)
qui s'essayent sur la pointe des pieds ;)

liens :

-   [Trigger Happy](http://trigger-happy.eu) page d'accueil
-   [Trigger Happy](https://github.com/foxmask/django-th) GitHub
    repository

