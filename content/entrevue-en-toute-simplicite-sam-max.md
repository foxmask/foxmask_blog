Title: Entrevue en toute simplicité - Sam et Max
Date: 2015-08-31 10:45
Author: foxmask
Category: Techno
Tags: python
Slug: entrevue-en-toute-simplicite-sam-max
Status: published

Ce billet aura une "autre saveur" puisque, alors que je m'étais refusé à
le faire, me disant que tout le monde les connaissait, j'ai fini par
franchir le pas. Donc voici une entrevue avec [Sam ET
Max](http://sametmax.com/)

Bonjour Sam et Max,

**Pouvez vous vous présenter en quelques mots ?**

**Sam** Ca va être dur sans tomber dans les généralités vu le côté
anonyme du  
blog. Disons que je suis un homme de moins de 40 ans, de plus de 20
ans, informaticien freelance avec une forte affinité pour le voyage et
la pédagogie. Enfin, ça dit pas grand chose, je pense que si les gens
voyaient à quoi ressemblait ma vie, beaucoup serait surpris.  
Il y a énormément de choses qu'on se garde de dire sur le blog. Mais
franchement, ce n'est pas très important. Y a assez de status facebook
inutiles pour pas que je vous raconte en plus ma marque de pomme
préférée.

**Max** : tombé dans la marmite informatique tout petit, j'ai commencé à
faire des petits progs en BASIC sur MO5, rien d'extraordinaire jusqu'aux
années 2000, avec la fameuse bulle internet (iBazar, Aucland, etc) le
net a commencé à prendre une place dans ma vie, je programmais déjà en
PHP et je sortais mes premiers sites de divertissement pour adultes.  
Comme ça ne rapportait pas grand chose, en parallèle je bossais dans
des boites comme webdesigner la plupart du temps. Ensuite j'ai monté ma
boite (affiliation sur du contenu adulte payant) et c'est là que j'ai
rencontré Sam (il faisait un stage dans les bureaux d'à côté). Le reste
vous le saurez en parcourant le blog ;)

**Comment êtes vous venus à python et que faisiez vous avant de faire du
python, depuis quand faites vous du python ?**

**Sam** Mon premier ordi avec une disquette 5 pouces et un bouton turbo
pour booster le proc à 8Mhz. Pas Ghz. Mhz. Mais j'ai programmé très
tard, ayant commencé ma formation en tant qu'ergonome puis rédacteur sur
une webzine d'info connu. Du coup j'ai vraiment attaqué la programmation
avec Basic et PHP3, que j'ai laissé tombé pour Python 2.4.

Un jour je me suis juste dit "PHP c'est vraiment pourri" et j'ai cherché
quelque chose de sympas. Je suis tombé sur un post de forum "Ruby VS
Python" (déjà à l'époque...). Les gars de Ruby vendaient le côté 'stylé'
du langage. Les gars de Python vendaient le coté 'lisibilité'. Je
préfère le pratique à l'esthétique, du coup j'ai choisit Python et j'ai
téléchargé le bouquin de Swinnen.

**Max** c'est la faute de Sam, j'avais besoin de refaire des sites en
PHP qui foiraient, il est arrivé avec sa science et voulait tout
reprendre à zéro, comme il détestait PHP je lui ai fait confiance et on
a tout passé en Django / python. Je ne le regrette pas.

**A quels projets opensource participez vous ?**

**Sam** On peut jeter à coup d'oeil aux repos pour ça
(<https://github.com/sametmax?tab=repositories>). Mais ca dépend de la
période de l'année. En ce moment surtout
[path.py](https://pypi.python.org/pypi/path.py) qui a gagné l'attribut
app\_dirs et la commutativité du /. Il y a aussi tout ce qui ne se voit
pas : rapport de bugs, aide sur les forums, etc.

**Max** Moi très peu, j'étais sur les débuts de
[0bin](https://github.com/sametmax/0bin) et je crois que c'est tout, pas
trop le temps faut dire.

**Utilisez vous
[Crossbar](http://crossbar.io/)/[Autobahn](http://autobahn.ws/python/)
en prod aujourd'hui ? Sur quel type de projet ? Petit/Gros ? Avec une
stack qui déchire/à toute épreuve ?**

**Sam** Absolument pas. A mon avis j'aurais un truc en prod utilisant
crossbar en 2016 à cause d'un projet dans les cartons, mais ça implique
développer une surcouche autour. Crossbar mérite vraiment une
abstraction.

Je vends la techno clairement comme quelque chose en construction. Le
jour où j'aurais un truc en prod, je ferai bien entendu un article
dessus.

**Max** Moi non j'y crois pas à ce truc :) Mais bon j'attends que Sam me
fasse une super démo de son utilité en PROD !!!!

**Quelle(s) lib tierce(s) a/ont votre préférence ?**

**Sam** Au final on en revient toujours aux mêmes modules :

-   codecs
-   collections
-   csv
-   datetime
-   functools
-   hashlib
-   itertools
-   json
-   pprint
-   random
-   re
-   subprocess
-   sys
-   threading
-   uuid

Ce sont les essentiels de Python. Avant il y en avait plus, mais
beaucoup sont remplacés par des libs tierces parties.

La stack que j'utilise le plus est encore et toujours l'écosystème
autour de Django. La raison est simple : il permet de faire le job pour
90% des missions. Je l'ai testé dans des conditions de merde en Asie et
en Afrique, je l'ai utilisé par des trucs cleans et des trucs à
l'arrache, et ça passe. On peut faire des petits sites, des gros sites,
et ça va marcher.

C'est quelque chose d'extraordinaire avec Python : on a un socle de
base, mais après, on a cette polyvalence du langage qui fait que dès
qu'on a un besoin, il y aura quelque chose pour le faire. Jusqu'ici, je
ne me suis jamais retrouvé avec un truc où je me suis dis "j'aurais pas
du prendre python". Par contre j'ai déjà identifié des projets où je me
suis dit "ce sera mieux de ne pas prendre Python". Le blog par exemple.

Est-ce que j'utiliserais toujours Django dans le futur. Probablement
pas. La raison pour laquelle j'emmerde tout le monde avec crossbar en ce
moment, c'est parce que je pense qu'on peut créer quelque chose de mieux
avec cette techno. Mieux que ce qui existe en Python, mais surtout mieux
que ce qui existe dans tous les autres langages.

De toute façon si on ne le fait pas, Python disparaîtra du monde de la
programmation Web et JS bouffera tout d'ici 10 ans du simple fait de son
avantage compétitif injuste : le marché captif des browsers. Donc même
si demain JS n'apporte rien sur la table, à effort égal, il gagnera. Et
JS apporte quelque chose sur la table avec des projets innovant comme
Meteor. Pour cette raison, il faut faire mieux que les outils JS actuels
si on veut rester pertinent en Web backend dans la prochaine décennie.

**Max** Requests, beautifullSoup, scrapy. Mais en général je me bats
avec Sam pour utiliser le moins de libs possible, ça foire toujours à un
moment donné (updates, rétrocompatibilité).  
Quand on se retrouve avec 50 libs et qu'on met son Django à jour par
exemple, on prie énormément et on prend son Prozac avant, ça foire à
99%.

**Que faites vous aujourd’hui et quel avenir/quels projets envisagez
vous ?**

**Sam** Aujourd'hui c'est beaucoup de formation et de dev, pas mal de taff autour du blog, et une avancée lente sur les projets en parallèle.
Je crois qu'un de nos problèmes c'est qu'on a des vies trop confortables : on a réussi à dégager plus de revenus en travaillant moins que la
moyenne, on vit dans des locaux souvent très chouettes, et on fait beaucoup d'activités de loisir.
Du coup on rogne sur les projets. C'est la décadence :)

**Max** Moi je gère toujours mes sites à fort trafic, avec Sam on
aimerait bien finir un projet qu'on a commencé ensemble (parmis tant
d'autres) qui semble prometteur mais j'en dit pas plus :p  
J'ai toujours 3 / 4 idées de projets sous le coude, cette année je vais
essayer de voir avec Sam pour en réaliser plusieurs ensemble, car on se
marre bien.

**Depuis le début de l'année vous avez ouverts des services tels
[indexerror.net](http://indexerror.net) et récemment un subreddit
[sam&max](https://www.reddit.com/r/sametmax/), vous avez d'autres idées
sous le sabot ?**

**Sam** Oui, mais on ne va pas faire une annonce ici pour éviter le côté
vaporware.  
On sait jamais, les journées sont courtes et la todo liste est longue.  
L'argent est aussi un problème. Aujourd'hui le blog et ses dérivés me
prennent 15% de mon temps de travail. Mais me rapporte 0 euros depuis 3
ans.  
Du coup si on veut continuer il va falloir qu'un des projets rapporte
des sous (on est pas consuméristes, mais on est très dépensiers), mais
sans affecter les autres projets ou détruire la bonne ambiance qu'il y a
dans la communauté. C'est très difficile à faire, la plupart des gens
échouent et transforment leur succès en supermarché, et c'est pour ça
qu'on ne se presse pas. Mais du coup le nombre d'articles à un peu
diminué, avec en contrepartie une présence sur les autres plate-formes
un peu plus forte. Je ne sais pas si c'est une bonne ou une mauvaise
chose.

Un truc qu'on peut dire, c'est que j'ai en tête un nouveau jeu avec lot
sur le blog comme on avait fait les années précédentes. Comme d'hab se
sera gratuit et le lot sera payé de notre poche. Mais la réa est
vraiment beaucoup plus importante, donc ça va pas arriver demain.

Il faut se souvenir que le S&M est une activité, qui bien quelle nous
prenne beaucoup de temps, reste en marge de nos vies.

**Max** Là on va freiner je pense de ce côté, car il faut penser à nous,
il y a le Multiboards customisable qu'il faut sortir (on a bien foiré sa
prod l'autre jour c'était marrant) et ça ira pour le moment.  
IndexError a été sorti en 1 jour (car c'est un script gratoche) et il
tourne tout seul, mais il bénéficie de la communauté S&M qui est
vraiment super alors c'est pas vraiment du taf mais il a son petit
succès et ça motive quand même pas mal pour envisager un nouveau projet
similaire, mais pas pour le moment.

<strong>En plus de l'aspect très technique et didactique, le ton décalé
du blog a séduit beaucoup de monde, "votre" communauté à grandi, et il
me semble qu'une certaine interaction s'est créée avec celle ci via les
services cités ci dessus.

Sans déconner, Comment gérez vous cette "notoriété" où vous êtes cités
tantôt dans un billet d'un blog tantôt dans une conf Python, tantôt
interpelés sur twitter ou irc ? C'est le mojo baby ?! ;)</strong>

**Sam** L'anonymat aide beaucoup. Notre entourage n'a aucune idée de
notre notoriété (même ceux/celles qui savent se font une idée vague), et
quand je vais à un event on parle souvent de nous à côté de l'un d'entre
nous.  
Mais comme on a une espèce de légende créée autour de nous, les gens
s'attendent à quelque chose de spécial. Du coup quand on arrive à
l'arrache par la porte de derrière, personne ne nous remarque.  
Ca fait garder les pieds sur terre, mais ça aide à une chose : avoir
confiance en son jugement. Notre profession souffre énormément du
syndrome de l'imposteur, et la validation des pairs aide à
l'outrepasser.

Il y a un autre point à prendre en compte : Max et moi sommes prêts à
voir tout disparaitre du jour au lendemain. Le blog ferme, plus personne
n'entend parler de nous, tous nos business se pètent la gueule. Pas
qu'on le souhaite, mais on y est préparé. Du coup on profite, mais pas
avec autant d'attachement au résultat qu'on pourrait imaginer. On a déjà
pas mal eu de "hard reset" avérés ou évités de justesse dans nos vies,
et ça forge le caractère.

**Max** On le doit beaucoup à Sam, il explique super bien les choses,
c'est inné chez lui. Pour le côté cul je pense que c'est mon job
principal qui a déteint dessus :)  
Et il me semble qu'au début on voulait se démarquer un peu alors on
s'est dit pourquoi ne pas parler de cas concrets de foirages de code par
rapport à nos sites. Et comme les sites c'était du cul ben les premiers
tutos de code portaient sur du filtrage de commentaires de cul, de
l'encodage de vidéos avec ffmpeg et python, etc.

**Dans le couple sam&max : Comment sont répartis vos rôles ? L'un gère
l'Infra, l'autre le code par exemple ? Dans vos projets communs qui fait
le choix de la stack ?**

**Sam** Max s'occupe de la maintenance et du design, moi du code et de
l'archi.  
Le reste, c'est de la co-décision. Mais on ne travaille pas tout le
temps ensemble. En fait, depuis que le blog a été créé, on a déjà vécu
plusieurs fois ensemble, puis changé de pays plusieurs fois travaillant,
à des milliers de bornes de distance, parfois sur des projets qui n'ont
rien à voir. Parfois on ne se donne pas de nouvelles pendant des
semaines. C'est pour ça que c'est amusant quand les gens croient savoir
où on est. Le où change très souvent.

**Max** Moi je suis l'admin système parce que je suis le seul à pouvoir
rester plus de 48h sur un bug, Sam craque au bout d'une heure.  
Côté code, on code tous les deux mais moi c'est franchement dégueulasse
alors il repasse souvent derrière pour lisser tout ça.  
Pour le choix de la Stack c'est Sam qui lance les propositions mais il
veut toujours utiliser les dernières versions alpha.beta.planta, moi je
suis très réfractaire aux nouvelles techno exotiques car la doc est
toujours naze et ça plante sans qu'on sache pourquoi, ceci dit Sam a
fini par s'en apercevoir sur nos projets et petit à petit j'arrive à le
convaincre d'utiliser des technos plus vieilles mais plus robustes (je
rappelle que je suis seul sur pas mal de projets en permanence et qu'on
est que deux sur l'ensemble pour gérer du python, php, sql, postgres,
ffmpeg, une 12aine de serveurs, celery, de l'upload, nginx, lua, jquery,
redis, varnish, munin, bash, bottle, etc, etc ) alors les nouvelles
technos avec 30 pages de doc incomplète qui bug de partout à mettre en
prod et à rajouter à cette stack, bof bof.  
Pour l'ergonomie de nos projets on aime bien en discuter ensemble, on
finit en général par tomber d'accord.

**En dehors du \#NSFW, et du code, comment se passe une journée loin du
clavier pour sam & max ? Une vie de patachon, de fetard ? Ou simplement
des "monsieur tout le monde" ?**

**Sam** Croyez-le ou non on est très sport (sports en plein air, salle
de muscu...) et jeu (LOL, Dota, JDR, plateau, console).  
Perso je suis vieux jeu et je lis beaucoup, mais regarde beaucoup de
films/séries modernes, alors que Max est du genre à regarder en boucle
des vieux classiques et à pouvoir citer chaque virgule de South Park.

Max est le fêtard, et pendant ses beuveries et nuits blanches, moi je
marathonne Got. Il soulève 90kg en développer-coucher, mais je lui mets
la misère en footing. On ne ressemble pas du tout à l'idée que la
plupart des lecteurs se font de nous dans les comments.

Les plus gros points communs qu'on ait sont les voyages et la bouffe. On
voyage tout le temps. D'où notre habitude à mélanger des sujets qui
n'ont rien à voir. C'est le monde qui est comme ça : un bordel mouvant
dans lequel il faut trouver un moyen de passer une belle journée. Et on
se fait tous les restos sur la route.

Après, le blog semble indiquer qu'on passe énormément de temps
uniquement ensemble, mais nous avons chacun une vie entière complètement
distincte, des réseaux sociaux très séparés.

**Max** J'ai deux passions dans la vie, les putes et la bouffe, le reste
c'est superflue :) Donc quand je code pas je suis avec les biatches ou
sinon à faire des bouffes (ouais je cuisine).

**Une conclusion ?**

**Sam** La première fois que nous nous sommes rencontrés, on n'a pas pu
se blairer. Comme quoi...

**Max** A poil les putes!

Merci pour votre participation à tous 2!

* * * * *

***(re)Lire une Entrevue précédente***

-   [Debnet](/post/2015/08/03/entrevue-en-toute-simplicite-debnet/)
-   [Ashgan](/post/2015/07/27/entrevue-en-toute-simplicite-ashgan/)
-   [Spout](/post/2015/07/20/entrevue-en-toute-simplicite-spout/)

