Title: Incontournables Pythonerie : Oh ho ho Géant Vert
Date: 2013-02-25 14:24
Author: foxmask
Category: Techno
Tags: python, relatorio
Slug: incontournables-pythonerie-oh-ho-ho-geant-vert
Status: published

Le Géant Vert en question est libreoffice ;-)

Ici un très simple billet pour vous montrer comment se faire un document
OpenOffice depuis un script Python en 5 lignes :P

Le script va se composer comme suit :

-   Récupération des données à publier dans le document
-   Récupération du document OpenOffice sur lequel va reposer notre
    génération finale
-   "Fusion" des points 1 & 2 ;)

Pour procéder à cette création, on aura besoin comme prérequis de
[Relatorio](https://code.google.com/p/python-relatorio/), un projet
python pour créer des doc ooo/pdf/html, à partir d'objets python.

Donc un petit

```shell
pip install relatorio
```

fera l'affaire pour disposer de l'armada ;)

1\) **Récupération des données à publier**

Ici je partirai d'un script Python renvoyant un dict, ni plus ni moins.

Le voici , il se nomme "maraicher.py":

```python
potager = dict(
            customer = 'Bonduelle',
            version = '1.12.09',
            previous_version = '1.12.08',
            middleware=[ { 'composant': 'Aluminium', 'version': '1.0.2' },
                         { 'composant': 'Fer', 'version': '1.1.2' } ,
                         { 'composant': 'Papier', 'version': '2.55.89' },
                ],
            core=[ { 'composant': 'Petits Pois', 'version': '1.12.13'},
                { 'composant': 'Carottes', 'version': '3.45.69'},
                { 'composant': 'Poireaux', 'version': '2.98.10'},
                { 'composant': 'Pommes de terre', 'version': '9.1'},
                ],

    )
```

2\) le **document OpenOffice** :

Ce dernier contient ce que vous avez
[ici](/static/pythoneries/Geant-Vert.odt "Document OpenOffice Geant Vert").
C'est en fait un tableau recensant des noms de produit avec leur
versions associées.  
[![geant vert : le template](/static/2013/02/geant-vert.png)](/static/2013/02/geant-vert.png)


3\) **Fusion**  
La fusion va consister à lire les données du dict et les injecter dans
le doc, tout cela se fait, like this (en 5lignes hein ;) :

```python
from relatorio.templates.opendocument import Template
from maraicher import potager
basic = Template(source=None, filepath='Geant-Vert.odt')
basic_generated = basic.generate(o=potager).render()
file('Geant-Vert1.odt', 'wb').write(basic_generated.getvalue())
```

le résultat est
[ici](/static/pythoneries/Geant-Vert1.odt "Document OpenOffice Geant Vert apres fusion")

[![geant-vert fusionné](/static/2013/02/geant-vert-fusion.png)](/static/2013/02/geant-vert-fusion.png)

Bon Appétit ;)

edit du 25/03/2015 : mise à jour du lien vers le projet relatorio
https://code.google.com/p/python-relatorio/

