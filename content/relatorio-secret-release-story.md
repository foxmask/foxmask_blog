Title: Relatorio et la Secret Release Story
Date: 2013-08-29 16:07
Author: foxmask
Category: Techno
Tags: python, relatorio
Slug: relatorio-secret-release-story
Status: published

Il y a 6 mois tout pile [je testais
relatorio](/post/2013/02/25/incontournables-pythonerie-oh-ho-ho-geant-vert/ "Incontournables Pythonerie : Oh ho ho Géant Vert")
avec succès sur un petit script pour un besoin précis et n'avait plus le
temps d'approfondir le sujet pour le boulot.

Les choses avançant (enfin), j'ai pu finir de faire le script python qui
me permet à présent de produire des documents openoffice automatiquement
à partir :

-   d'un modèle openoffice (comme on en ferait un pour word en utilisant
    la "fusion & publipostage" pour ceux à qui ça parle plus)
-   et d'une source de données au format XML provenant de
    [Autodeploy](http://buildprocess.sf.net "Autodeploy").

Autodeploy servant à manager pas moins de 160 environnements jEE pour
les installations et mises à jour.

Une fois les release produites, installées et testées il faut les livrer
aux clients. Et qui trouve-t-on au bout de la chaine pour tout cela ?
ouais ouais vous avez compris :)

Pendant longtemps déjà je me coltinais la création des livraisons aux
clients à la mimine (avec un mkdir -p des dossiers requis + wget des 'n'
archives dans chaque folder, vous voyez le patacaisse) jusqu'au moment
où la quantité de livraisons à effectuer dépassait 1j/homme et ai fini
par produire [Make
delivery](https://github.com/foxmask/autodeploy-make-delivery), un
script python parcourant le fichier XML d'Autodeploy.  
Ce dernier en extrait les tarball avec le nom du package et les colle
dans une arborescence de folders définie avant de tout compresser pour
l'envoyer au client.  
Temps passé **avant** make delivery : **1heure par livraison**  
Temps passé **depuis** make delivery : **15min par livraison** et je
suis large

Seulement dans le process de livraison, on fourni quand même une @\#\*!
de release note faite ... MAIN ! release note qu'on faisait vérifier par
le consultant afin de s'assurer que le contenu du document collait
parfaitement au livrable.  
Je vous laisse imaginer le temps perdu, les ratés potentiels, et la
suite chez le client qui installe tout le toutim.

A présent tout ça c'est FINI ! Bibi a fait l'(comic) script !

Le script "MakeDelivery" sera donc suivi par un second "MakeRelease"
pour la création de la doc, et aucune erreur de numéro de version ne
sera plus possible !

Grâce aux gars de la prod et du build process basé sur maven, on dispose
des numeros de version dans les urls de chaque package, d'où j'en
extrais le nom et la version que je refile dans un beau "dict()" lequel
"dict" est avalé par
[relatorio](http://code.google.com/p/python-relatorio/ "Page du projet relatorio")
qui pond le "document sésame" sans erreur possible !

Tout cela est tout beau mais attention quand même aux surprises de
dernières minutes. Comme je l'ai dit au début de ce billet j'avais
commencé mon script en février et mon

```python
pip install relatorio 
```

ne m'a pas chatouillé à l'époque.

Entre temps une release majeure debian est passée sur ma machine et
surtout une mise à jour relatorio !  
En reprenant donc le cours de mon installation je me refais un
virtualenv je lance sereinement le pip install précédent.

Une fois tout installé (enfin dirai-je) je fini mes devs sur mon script
make\_release.py et me dit "bon ce coup ci tout est prêt pour produire
enfin un doc Ooo" et au premier lancement *zboing* la fin des haricots !

```python
Traceback (most recent call last):
  File "run.py", line 172, in 
    main()
  File "run.py", line 166, in main
    generate_doc(customer_release)
  File "run.py", line 130, in generate_doc
    basic = Template(source=None, filepath='Foo_bar.odt')
  File "[...]/lib/python2.7/dist-packages/relatorio/templates/opendocument.py", line 245, in __init__
    encoding, lookup, allow_exec)
  File "[...]/lib/python2.7/dist-packages/genshi/template/markup.py", line 67, in __init__
    allow_exec=allow_exec)
  File "[...]/lib/python2.7/dist-packages/genshi/template/base.py", line 417, in __init__
    source = BytesIO(source)
TypeError: expected read buffer, NoneType found
```

Un truc aurait dû me mettre la puce à l'oreille, la flopée de modules
python supplémentaires à compiler/installer, me dis-je, incriminant
d'emblée relatorio et sa v 0.6.0 puisque même les exemples fournis sur
le wiki ne passaient pas.

Comme je me farcie pas mal de problèmes revêches quotidiennement, je
procède avec dichotomie afin de trouver qui de relatorio ou de genshi me
casse *vraiment* les pieds. Je laisse la 0.6.0 de relatorio et supprime
genshi 0.7.0 et mets une 0.6.0 à la place en me disant si cela ne passe
pas, au pire, je me ferai un nouveau virtualenv tout neuf avec un
relatorio 0.5.0.

je relance mon script et là ! ô joie, plus d'erreur et ma release note
est là toute belle !  
Gain de temps final ? : je ne vous en parle même pas ! plus de besoin
de faire 'n' validations "humaines" inutiles ! plus besoin de lancer
OpenOffice pour produire le document. Tout va être scripté mon bon
môsieur !

**edit**: la solution pour utiliser la dernière version de genshi est en
commentaire et tout rentre dans l'ordre ;)

