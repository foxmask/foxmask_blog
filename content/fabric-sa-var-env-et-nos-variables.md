Title: Fabric, sa var 'env' et nos variables dynamiques !
Date: 2017-07-06 20:00
Author: foxmask
Category: Techno
Tags: python, Fabric
Slug: fabric-sa-var-env-nos-variables-dynamiques
Status: published


Fabric est un sérieux concurrent face à ansible, quoiqu'on en pense.

# Intro : 

J'ai eu à faire à [ansible](https://www.ansible.com/) pendant plus d'un an pour automatiser des installations d'applications java sur tous les types de serveur d'applications du marché.
Mais comme à mon habitude, je n'utilise pas des outils de DevOps pour ce qu'ils ont été conçus dès le départ, à savoir, répéter la même operation sur plusieurs hosts à la fois.
Non, j'ai vu dans ansible, la possibilité d'automatiser toujours la même opération sur UN serveur et UN seul à la fois. 
En effet, les environnements jEE en entreprise sont du genre "production", "test", "developpement", et évidement, on ne va pas s'amuser à deployer la version de dev automatiquement en test et en prod.
Donc on a 3 environnements par client, chacun vivant sa vie, comme chacun peut l'imaginer. Les corrections de bug de prod dans un coin, les évol en cours sur l'env de test etc...
Du coup on voit bien que l'industrialisation "classique" des DevOps, consistant à installer 'n' fois un service sur 'n' serveurs, ne colle pas du tout au "métier".

# Ansible at first 

Avec ansible tout se passait pour le mieux, mais arriva un moment où, les serveurs unix devenaient retord et ansible n'accrochait plus ces derniers correctement. 
Plus de retour des tâches habituellement exécutées, tantôt stuck, tantôt plantées, mais trop souvent, restées dans le flou avec une question récurrente : "mais où ca en est ?"
Alors sont en cause les serveurs eux mêmes puisque surchargés et RAM faible, mais à ce moment là je m'attendais à un minumum de reaction de ansible pour quand même "revenir" au serveur déclencheur du playbook et s'arrêter proprement.

Donc las de cette situation, j'ai réécrit tous mon playbook et roles ansible en 5 modules python avec fabric en lieu et place.

# Fabric : 

avec ansible, il est possible de fournir un fichier JSON contenant des extra-vars. Très pratique pour moi, pour fournir à ansible, dynamiquement, le nom du serveur et les URL des applications java à recuperer pour les deplooyer ensuite.

avec [fabric](http://docs.fabfile.org/en/1.13/index.html), je fis un petit wrapper qui me permet de passer du JSON en un fichier settings à la django dynamiquement. Par contre, j'oubliais que comme 'n' users pouvaient utiliser mon appli Django pour déclencher les installations, tout allaient écrire dans le même fichier settings ... 
Donc en creusant comme avoir aussi avec Fabric un fichier d'extra-vars, je n'ai rien trouvé de meiux que de peupler la variable env de Fabric avec ma propre sauce.
Vous pourriez objecter que c'est une grosse connerie parce que je vais me mélanger les crayons avec les variables de Fabric, mais que néni, mes variables sont toutes en MAJUSCULE, ce qui n'est pas la cas de Fabric.

Donc **env.user** et **env.password** ne seront pas écrasées par mes **env.ENV_USER** et **env.PASSWORD** par exemple.

Donc pour obtenir une fonctiionnalité équivalente de extra-var de Ansible avec Fabric, on spécifiera sur la ligne de commande l'option "-c" pour que Fabric aille chercher le fichier RC, qui lui, contiendra le même contenu que le fichier settings sus-mentionné.

Ainsi 'n' users ne se marcheront plus sur les pieds.

__Dernière subtilité donnée dans la doc__ :

les fichiers RC sont lus comme suit :

```python
CLE_A=valeur
```

où valeur sera retournée sous la valeur : 'valeur'

si valeur est un path ca donnera '/mon/path/'
ce qui est la chianli quand on fait un os.path.join(env.CLE_A, 'sous_dossier')  puisqu'on obtiendra comme valeur : '/mon/path/'/sous_dossier

de même pour mon **env.ENV_USER** qui a pour valeur 'foxmask' ; quand je fais un **sudo(cmd, user=env.ENV_USER)** j'ai droit à un manignifique __"sudo user 'foxmask' n'existe pas"__

de même pour un dict 

```python
CLE_B=[{'truc_machin': 'bidule']
```

sera retourné sous une la forme d'une string
    
du coup on le voit on se fait bien enfumer

Pour régler son compte à ce comportement, reste à se faire une petite méthode pour épurer les valeurs de ses propres variables, avec un coup de 

```python
env.MAVARIABLE = env.MAVARIABLE.replace("'", '')
```

là où c'est nécéssaire et appeler ladite méthode dans les modules où on utilise "env" :P

Et pour la cas du dict, il faudra passer par le module "[ast](https://docs.python.org/3/library/ast.html?highlight=ast#module-ast)" pour revenir à un "dict" nomal, like this 

```python
cle_b = ast.literal_eval(env.CLE_B)
```

et on pourra retourner faire joujou avec son dict comme d'hab

## [Fabric and Django integration](http://docs.fabfile.org/en/1.13/api/contrib/django.html)

Un moment j'ai cru voir une lueur d'espoir avec cette contribution qui permettrait d'accéder à "ses affaires" made in Django, depuis Fabric, genre au pif les données du modèle que j'injecte en JSON à la volée et récupère dans **env.MES_VARIABLES_A_LA_NOIX** mais, j'ai vite déchanté avec un erreur on ne peut plus bateau :

```python
ModuleNotFoundError: No module named 'monmodule'
```


# Conclusion :

Voila voilo pour une billet fait rapidos sur des utilisations completements détournées du but premier :)


