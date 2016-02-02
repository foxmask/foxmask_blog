Title: Revue Technique de la semaine du 02/02/2016
Date: 2016-02-02 01:00
Author: foxmask
Category: Techno
Tags: Django, python, devops, ansible, meetup, pycharm
Slug: revue-technique-de-la-semaine-du-02022016
Status: published

Ca vous manquait aussi un billet du renard masqué hein ?
Bon qu'est-ce que je vais bien pouvoir vous racontrer ? 


### Evernote de mieux en pire ?

Je résumerai bien ce qui arrive a Evernote par "Qui trop étreint, mal embrasse" tant ce qui se passe le reflète.
L'an passé on apprenait qu'Evernote se séparait d'une partie de ses equipes d'ingénierie, après que certains associés fondateurs aient tirés leur révérence, au point qu'on evoquait sa fin, ce qui m'a du coup fait prendre conscience, comme pour google, "nom di diou si ca ferme demain que fais je de mon contenu?", ou "Le syndrôme des services gratos Google qui vous font perdre vos données à vous même rien à vous".

Pour ma part j'ai rapidement repris le dessus puisque je peux facilement renvoyer tout ce que j'ai chez, eux ailleurs, via mon projet [TriggerHappy](http://blog.trigger-happy.eu).

Mais revenons à nos moutons, après ce premier évènement, suit un second depuis hier, Evernote annonce cesser son activité de [vente de produits hype](http://www.theverge.com/2016/2/1/10890562/evernote-market-shut-down-moleskine-notebook-2016) et quand même cher pour ce que c'est. Donc fini les carnets moleskine, portefeuille et scanner, qui ne seront plus vendus que par leur partenaire. Evernote se recentrant (enfin?) sur le software.

Ce qui m'a toujours paru bizarre c'est leur blog où il tente de "louer", via des personnes exterieures à l'entreprise, la reussite de l'utilisation de l'outil, qui leur a changé la vie, qui les a rendu plus productifs etc. Comme s'ils avaient besoins de témoignages pour s'en convaincre eux mêmes. Ca me fait trop penser aux vieilles "pub témoignages" moisies "Weight&Watchers" où pour vous convaincre, il faut vous le dire...

Pour ma part j'adore l'outil qui, techniquement, est incontournable (le moteur de recherche offline + l'OCR notamment + le plugin firefox de capture d'article) mais la comm marketing autour est une misère.

Donc pour l'heure, tant que le bateau ne chavire pas, je ne bougerai rien, sinon j'irai m'oriente vers une alternative libre déjà existante mais pour l'heure sans API permettant d'ajouter des données autrement que manuellement. Celle ci se nommera [paperwork](https://github.com/twostairs/paperwork) ou [laverna](https://github.com/Laverna/laverna)

### Django 

#### 1.9.2 security fix and 1.8.9 bug fix

[A vos mises à jour](https://www.djangoproject.com/weblog/2016/feb/01/releases-192-and-189/) si vous êtes sur la 1.9.x !
Pour la 1.8.9 rien à craindre, il s'agit que d'une release concernant peu de corrections de bugs.

#### Extensions or not to be

Il y a quelques jours j'évoquais un besoin sur les forms django (je ne sais plus lequel :P) avec [SpoutBe](https://twitter.com/spoutnik) qui me disait que [django crispy](https://github.com/maraujop/django-crispy-forms/) répondait à mon besoin. Mais je lui avais répondu que j'étais très réticent à utiliser des "projets satellites" parce que le jour où plus maintenus, le code produit (n')évolue (plus que) difficilement. Donc tant que c'est pas "core" je n'y toucherai pas. Il n'y a que les cas où des projets satellites "naissent" du core que je les emploie, comme par exemple [django-formwizard](https://pypi.python.org/pypi/django-formwizard).

Et vous, comment gérez vous l'ajout de fonctionnalités offertes par de tels projets pour Django ? Vous fiez vous à la "vivacité" du projet pour le choisir et vous dire que c'est un gage d'évolution ?


### Meetup - c'est reparti !

Des meetup (DevOps, Paris.py) ont repris mais j'ai pas l'envie là tout de suite, pourtant j'ai l'occasion d'y aller en bonne compagnie, mais non là non, j'ai encore un coup de "mood" là , ca attendra !

* [Paris DevOps, aujourd'hui](http://www.meetup.com/fr-FR/Paris-Devops-Meetup/)
* [Paris.Py, le 4 février](http://www.meetup.com/Paris-py-Python-Django-friends/)


### Arround the world

Quelques bons billets à se mettre sous la dent :

* [Evolution de Python](http://sametmax.com/evolution-de-python/) par Sam & Max
* [Free Software activities](http://anarc.at/blog/2016-01-31-free-software-activities-january-2016/) par Anarc
* [News de Crossbar](http://sametmax.com/nouvelle-release-de-crossbar-historique-des-events-et-crypto/) par Sam & Max
* [PyCharm 5.0.4](http://feedproxy.google.com/~r/Pycharm/~3/YWRWdinNGw4/)
* [Le Pypi nouveau est sur les rails](http://pyfound.blogspot.fr/2016/01/postscript-to-warehouse-post.html) par la PSF


### A Tester / A Lire

* [Ansible 2](http://www.ansible.com/blog/ansible-2.0-launch), à tester avant de switcher de 1.9, car ca pète pas mal de choses qui focntionnaient avant ou passent en dépréciées comme les inclusions de playbook avec un tag ... ca ca me reste en travers ...

ceci n'est plus possible :

```yml

   include: /path/to/foo/bar tag=foobar
   include: /path/to/bar/foo tag=barfoo

```

du coup dans un main.yml, je ne peux plus conditionner l'inclusion (et donc l'execution de ce qui est inclus), merci !

* [Github Reviewer](https://github.com/gabrielhora/github_reviewer)
* [bien démarrer DRF - Partie 5](http://makina-corpus.com/blog/metier/2016/bien-demarrer-avec-django-rest-framework-personnalisation-des-routeurs-partie-5) par Makina Corpus. ici j'ai pris le feuilleton en chemin, alors j'ai raccroché les vagons en m'envoyant les 4 premières parties ;)
* [IE 8,9,10, de l'histoire ancienne ?](http://mashable.com/2016/01/12/internet-explorer-8-9-10-dead/) j'aime quand c'est microsoft qui le dit :) 
* [Oracle met à mort le support de la java applet dans les browsers](http://www.v3.co.uk/v3-uk/news/2443810/oracle-signals-the-end-of-java-applet-support-for-browsers). Les boites qui sont encore avec du IE < 10 et avec des applet java (au pif Oracle Forms) ont du mouron à se faire ...


### J'en fout pas une

Depuis quelques semaines je commit que dalle sur TriggerHappy, je "papillone", je teste des trucs, je regarde des nouveaux langages, je glande, je joue, je procrastine, je fais de la bouffe ([genre](http://www.recettes-bretonnes.fr/gateaux-bretons/quatre-quarts-pommes.html)), la vie quoi ...


