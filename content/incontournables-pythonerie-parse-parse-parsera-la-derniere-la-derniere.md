Title: Incontournables Pythonerie : parse parse parsera la dernière la dernière 
Date: 2013-03-13 15:04
Author: foxmask
Category: Techno
Tags: python
Slug: incontournables-pythonerie-parse-parse-parsera-la-derniere-la-derniere
Status: published

Le sujet du jour concernera le traitement des paramètres en lignes de
commandes, mais au lieu de mon [précédant billet sur le
sujet](/post/2013/02/25/incontournables-pythonerie-die-arg/ "Incontournables Pythonerie : Die Arg"),
qui traitait de
[OptParse](http://docs.python.org/2/library/optparse.html "Python doc Optparse"),
celui ci traitera de
[argparse](http://docs.python.org/2/library/argparse.html "Python doc Argparse")
et des différences que j'ai constaté pour passer de l'un à l'autre, et
[qui ne sont pas dans la doc de
"migration"](http://docs.python.org/2/library/argparse.html#upgrading-optparse-code)

Pour traiter un cas concret j'ai produit un lib python pour récupérer
des infos d'un site en ligne telles que une timeline, la liste épisodes
d'une série tv, la liste des séries tv ressemblant à une autre etc... ça
c'est pour la lib, elle fonctionne ;)

Pour la tester j'ai pondu un script qui fait l'appel à toutes les
méthodes de la classe de ma lib. Il y a pas moins d'une quarantaine de
méthodes.  
Pourquoi je vous dis ça ? parce que ça m'a fait faire une quarantaine
de traitement d'arguments ;) Ah ba quand il faut il faut ;)

**Optparse**

Avec optparse, j'ai donc décidé de partir du postulat : faire des
"groupes" : un par methode de ma classe avec les options qui matcheront
les paramètres attendues par chaque méthode (classique quoi). Cela
donnait ceci (je ne vous mets pas tout rassurez vous ;) :

```python
def main():
    parser = OptionParser()

    group0 = OptionGroup(parser, "*** Search series")
    group0.add_option("--title", dest="title", type="string",
                      help="make a search by title")
    parser.add_option_group(group0)

    # group the options for handling Display of series parameters
    group1 = OptionGroup(parser, "*** Details of series")
    group1.add_option("--display", dest="display", action="store",
                     help="the name of the given serie")
    parser.add_option_group(group1)

    # group the options for handling Episodes parameters
    group2 = OptionGroup(parser, "*** Episodes",
                        "use --name  (--season ) (--episode )  
(--summary) to filter episodes you want to search")
    group2.add_option("--name", dest="name", action="store",
                     help="the name of the given serie")

    group2.add_option("--episode", dest="episode", action="store",
                     help="the number of the episode (optional)")

    group2.add_option("--season", dest="season", action="store",
                     help="the number of the season (optional)")

    group2.add_option("--summary", dest="summary", action="store_true",
                     help="boolean set to false by default,   
to only get the summary of the episode (optional)")

    parser.add_option_group(group2)
[...]
    (options, args) = parser.parse_args()
[...]
```

Ensuite pour avoir l'aide on tape

```python
python go.py -h
```

qui affiche

```shell
Usage: go.py [options]

Options:
  -h, --help            show this help message and exit

  *** Search series:
    --title=TITLE       make a search by title

  *** Details of series:
    --display=DISPLAY   the name of the given serie

  *** Episodes:
    use --name  (--season ) (--episode ) (--summary) to
    filter episodes you want to search

    --name=NAME         the name of the given serie
    --episode=EPISODE   the number of the episode (optional)
    --season=SEASON     the number of the season (optional)
    --summary           boolean set to false by default,
                        to only get the summary of the episode (optional)
```

Ok c'est tout beau et cool et ça marche (en plus ;-)

Bon à présent les limitations de optparse (outre le fait qu'il est
déprécié car plus maintenu) :

**les paramètres obligatoires**:

optparse permet de rendre des paramètres obligatoires via un
required=True, mais le soucis c'est que les groupes ne sont pas
exclusifs et que dans le "options" qui est ici :

```python
 (options, args) = parser.parse_args()
```

"options" contient TOUS les paramètres de TOUS les groupes. Du coup si
on fait un required=True sur

```python
    group0.add_option("--title", dest="title", type="string",
                      help="make a search by title",required=True)
```

quand je taperai

```python
python go.py --display --name dexter
```

il me sortira que j'ai oublié de renseigner le paramètre TITLE.... que
je n'ai pas besoin pour l'utilisation de --display ...

Ça ça m'a dérangé car du coup j'ai dû déporter l'aspect "obligation de
renseigner un paramètre" plus tard dans mon code.

**paramètres en conflit**  
optparse ne permet pas d'utiliser 2 fois le même nom de paramètre pour
deux groupes distincts, il pète une vraie exception et rien à faire pour
contourner. Du coup la convention de nommage des variables (pour les
rendre unique) devient vite pénible pour conserver un semblant
d'homogénéité entre les noms des méthodes de la classe de ma lib et les
noms des actions mises en place dans mon script.

**aide trop verbeuse**  
Comme dit plus tôt j'ai pres de 40 groupes, du coup l'aide en devient
carrément illisible au premier coup d'oeil.

Si si je vous promets, imaginer ça

```shell
Usage: go.py [options]

Options:
  -h, --help            show this help message and exit

  *** Search series:
    --title=TITLE       make a search by title

  *** Details of series:
    --display=DISPLAY   the name of the given serie

  *** Episodes:
    use --name  (--season ) (--episode ) (--summary) to
    filter episodes you want to search

    --name=NAME         the name of the given serie
    --episode=EPISODE   the number of the episode (optional)
    --season=SEASON     the number of the season (optional)
    --summary           boolean set to false by default,
                        to only get the summary of the episode (optional)
```

... multiplié par 10 ...

Donc fort de ces constats je me suis dit "bon hé ho ; si ça me saoule
déjà rien qu'à moi personnellement moi même ; je ne serai pas le seul ;
voyons argparse"

**Argparse**  
Pour démarrer sans trop perdre de temps j'ai donc suivi la doc
d'upgrade mentionnée plus haut pour passer de optparse à argparse.

Ça a vite fonctionné et j'étais plutôt content ;)

**paramètres en conflits** : **résolu**  
Mais comme je suis toujours insatisfait, je suis reparti sur mon envie
de mettre les mêmes noms de variables à mes actions qu'à celle des
paramètres de mes méthodes de classe de ma lib.

en clair je voulais pour ça :

```python
    def shows_episodes(self, url, season=None, episode=None, summary=False,
                       hide_notes=False, token=None):
[...]
    def shows_characters(self, url, summary=False, the_id=None):
[...]
```

faire un truc du genre :

```python
python go.py shows_episodes --url ... --season ... --episode ... 
python go.py shows_characters --url ... --summary ...
```

Pour y parvenir argparse a une option de gestion des conflits
**conflict\_handler** qu'on passe à *'resolve'*

Ainsi pourvu, taper les paramètres sera beaucoup facile à retenir ou
tout du moins plus simple à taper que

```python
python go.py --shows_episodes --shows_episodes_url ... --shows_episodes_season ... --shows_episodes_episode
python go.py --shows_characters --shows_characters_url ... --shows_characters_summary ... 
```

vous voyez le genre de balles dans la tete qu'on pouvait se tirer avec
optparse pour avoir des var "unique" (sans conflit ;)

**aide trop verbeuse** : **résolu**  
De même l'aide cette fois-ci s'est retrouvée raccourcie drastiquement.

avant on avait

```shell
Usage: go.py [options]

Options:
  -h, --help            show this help message and exit

  *** Search series:
    --title=TITLE       make a search by title

  *** Details of series:
    --display=DISPLAY   the name of the given serie

  *** Episodes:
    use --name  (--season ) (--episode ) (--summary) to
    filter episodes you want to search

    --name=NAME         the name of the given serie
    --episode=EPISODE   the number of the episode (optional)
    --season=SEASON     the number of the season (optional)
    --summary           boolean set to false by default,
                        to only get the summary of the episode (optional)
```

à présent ca donne :

```shell
Usage: go.py [options]

Options:
  -h, --help            show this help message and exit

  shows_search - Search series: use shows_series make a search by title
  shows_displays - Details of series: use display=DISPLAY   the name of the given serie
  shows_episodes - Episodes: use shows_episode  (--season ) (--episode )
                  (--summary) to filter episodes you want to search
```

La différence entre les 2 ? On n'affiche plus ici les options de chaque
commande ! Mais ensuite si on veut l'aide complète de l'action
shows\_search on tapera un :

```shell
python go.py show_search --help
```

qui donnera l'aide escomptée

```shell
usage: go [options] shows_search [-h] --title TITLE

positional arguments:
  shows_search   Search series: use --shows_search --title 

optional arguments:
  -h, --help     show this help message and exit
  --title TITLE  make a search by title
```

C'est plus clair plus concis et on est tout joie ;)

Tout ceci est obtenu avec une particularité propre à argparse qui est la
création d'un sub-parser. Oui un subparser.

Avant on avait la totalité des actions (sous la main avec optparse)
comme montré dans le premier snipset

A présent avec subparser ca donne ceci :

```python
    parser = argparse.ArgumentParser(prog="go",
                                     usage='%(prog)s [options]',
                                     description='BetaSeries API Management',
                                     conflict_handler='resolve',
                                     add_help=True)

    subparsers = parser.add_subparsers(help='sub-command help')

    group0 = subparsers.add_parser('shows_search', help='Search series:   
use --shows_search --title ')
    group0.add_argument("shows_search", action="store_true",
                    help='Search series: use --shows_search --title ')
    group0.add_argument("--title", action="store", required=True,
                        help="make a search by title")

    group1 = subparsers.add_parser("shows_display",
            help="Details of series: use --shows_display --url ")
    group1.add_argument("shows_display", action="store_true",
                    help="Details of series : use --shows_display --url ")
    group1.add_argument("--url", action="store", required=True,
                     help="the url/name of the given serie")

    group2 = subparsers.add_parser("shows_episodes", help="Show Episodes: use   
--shows_episodes --url  (--season ) (--episode )  
(--summary) to filter episodes you want to search")
    group2.add_argument("shows_episodes", action="store_true", help="Episodes:  
--shows_episodes --url  (--season ) (--episode )  
(--summary) to filter episodes you want to search")
    group2.add_argument("--url", action="store", required=True,
                     help="the url of the given serie")
    group2.add_argument("--episode", action="store",
                     help="the number of the episode (optional)")
    group2.add_argument("--season", action="store",
                     help="the number of the season (optional)")
    group2.add_argument("--summary", action="store_true",
                     help="boolean set to false by default,   
to only get the summary of the episode (optional)")
[...]
    args = parser.parse_args()
    if len(sys.argv) > 1:
        do_action(args)
    else:
        parser.error("enter -help to see the options you can use")
```

Une petite explication sur le parm help s'impose dans l'utilisation que
j'en ai faite.

-   Quand on tape **python go.py --help** l'aide affichée n'est autre
    que le texte (help="..") qui se trouve sur ma ligne **groupX =
    subparser.add\_parser()**
-   Quand on tape **python go.py shows\_search --help** l'aide affichée
    est celle sur la ligne add\_argument("show\_search",help="..")
    puisque cette fois ci je veux l'aide de la commande elle même.

La différence c'est que la premiere sert pour afficher l'aide de toutes
les commandes, la seconde pour l'aide de la commande elle seule.

Donc, personnellement je mets la même chose sinon je n'ai pas d'aide
affichée suffisement explicite.  
On pourrait se dire que argparse va réafficher quand même l'aide déjà
fournie pour ici **groupX = subparser.add\_parser()**, mais non :

voici la difference

**sans le texte d'aide**

```shell
usage: go [options] shows_search [-h] --title TITLE

positional arguments:
  shows_search

optional arguments:
  -h, --help     show this help message and exit
```

**avec le texte d'aide**

```shell
usage: go [options] shows_search [-h] --title TITLE

positional arguments:
  shows_search   Search series: use --shows_search --title 

optional arguments:
  -h, --help     show this help message and exit
  --title TITLE  make a search by title
```

Autre différence majeure entre optparse et argparse :

**Récuperer les infos saisies avec optparse**

on faisait à la tout fin de la definition des groupes (pour mon cas)

```python
(options, args) = parser.parse_args()
```

puis dans sa fonction on testait les paramètres :

```python
if options.title:
#traitement
elif options.name:
#traitement 
```

**Récuperer les infos saisies avec argparse**

```python
args = parser.parse_args()
```

Ici args est une liste nommée Namespace qui contient uniquement les
paramètres disponibles via le subparser concerné, exemple un print de
args donnerait ceci :

```python
python go_new.py shows_episodes --url dexter
Namespace(episode=None, season=None, shows_episodes=True, summary=False, url='dexter')
```

Ensuite donc dans sa fonction on teste si la commande est dispo dans
options :

```python
f hasattr(options, 'shows_characters'):
#traitement 
elif hasattr(options, 'shows_episodes'):
#traitement
```

On doit utiliser if hasattr(options, 'shows\_episodes'): à la place de
if options.shows\_episodes sinon python produira systématiquement une
erreur, puisque l'info sur options.shows\_episodes n'est pas disponible
quand on traitera de .... shows\_characters... et inversement.

voili voilo.

Pour voir mes scripts complets avec optparse et argparse ; [ils sont
tous deux disponibles sur github au beau milieu d'un
projet](https://github.com/foxmask/pythonseries/) ;)

Si vous avez des remarques &/ou corrections, lâchez vous ;)

[Si vous avez envie d'article sur un sujet particulier, "il y a un"
billet "pour cela"
(c)](/post/2013/02/15/incontournables-pythonerie/ "Incontournables Pythonerie")
et je me fais fort de (tenter) d'y répondre ;)

