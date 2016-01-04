Title: Incontournables Pythonerie : un pack de 12 s'il te plait !
Date: 2013-03-18 10:00
Author: foxmask
Category: Techno
Tags: python
Slug: incontournables-pythonerie-pack-de-12
Status: published

Avec ce billet nous allons voir comment produire un package comme on en
voit partout dans le monde opensource (ou pas d'ailleurs) pour livrer
une "suite logicielle" à ses clients/utilisateurs.

**Brève présentation du script :**

Ce script extrait d'un fichier XML (produit par
[Autodeploy](http://buildprocess.sourceforge.net/autodeploy.html "autodeploy"))
les targz installés sur les environnements.  
Puis lit un fichier de configuration pour décider dans quel répertoire
va être télécharger chaque archive. C'est tout ! On mappe ni plus ni
moins un targz dans un dossier.

**Prérequis à la lecture de cet article**  
la lecture des mes billets précédents, vous donnera l'aperçu de ce qui
va suivre, puisque chacun d'eux est une partie du script complet qui
suivra comme je vous l'ai présenté depuis ces derniers jours, notamment
:

-   récupération des arguments entrés sur la ligne de commande soit
    [avec
    optparse](/post/2013/02/25/incontournables-pythonerie-die-arg)
    ou
    [argpase](/post/2013/03/13/incontournables-pythonerie-parse-parse-parsera-la-derniere-la-derniere/ "Incontournables Pythonerie : parse parse parsera la dernière la dernière")
-   [la lecture de fichier
    XML](/post/2013/02/18/de-php-a-python-x-aime-l/ "de PHP à Python : X aime L")
-   [la lecture de fichier de
    configuration](/post/2013/03/04/de-php-a-python-minie-petite-souris)
-   [la création de fichier de
    journalisation](/post/2013/03/11/incontournable-pythonerie-bigbrother-is-logging-you)

La *nouveauté* dans cet article est le pseudo "wget" à la sauce Python
pour récupérer les archives

Tout ceci ressemble bien au déroulement d'un script, [ça tombe bien le
voici](https://github.com/foxmask/autodeploy-make-delivery/blob/master/make_delivery.py)
:)

Pour utiliser ce script, on tape

```shell
python make_delivery -r RELEASE -e ENV -c CONFIG
```

le script traitera ceux ci comme suit :

```python

    usage = "%prog -e environment name -r release name. \nfor example : \npython make_delivery -e envname -r 20130101"
    parser = OptionParser(usage)
    parser.add_option("-e", "--env", dest="environment",
                      help="the environment name to use to build the delivery", metavar="ENV")
    parser.add_option("-r", "--rel", dest="release",
                      help="the release name of this delivery (used to name the final package like release-RELEASE-yyyymmdd)", metavar="RELEASE")
    parser.add_option("-c", "--conf", dest="configfile",
                    help="the path where the config file is located. This file should contain the name of the environment from which to download the archives. By Default the script will search in ./env_dirs.conf", default="./env_dirs.conf", metavar="CONFIG")
    parser.add_option("-l", "--log", dest="configlogfile",
help="the path where the config file for the loggging is located. By Default the script will search in ~/MakeDelivery/logging.conf", default=os.path.expanduser('~/MakeDelivery/logging.conf'), metavar="LOGGING_CONFIG")
    (options, args) = parser.parse_args()
    if options.environment == None or options.release == None:
        parser.error("options -e and -r are mandatory")
    else:
        [...]
        #lets concat release name + date to have a name to use for logfile and directory
        release_name = release_name_main ( options.release )
        [...]
        release_name_dir = release_name_create( release_name )
```

Dès lors make\_delivery va faire quelques vérifications d'existence du
dossier que j'escompte créé (pour ne pas écrire par dessus pusique je
conserve un historique de toutes les livraisons faites au client).

```python
def release_name_create(release_name_dir):
    if os.path.isdir(release_name_dir):
        logger.critical("Directory %s already exists. You should change the release number ( -r parameter ) " , release_name_dir)
        exit ( 1 )
    else:
        logger.info("Creation of %s" , release_name_dir)
        os.makedirs(release_name_dir)
        return release_name_dir
```

Puis make\_delivery appelle le [module
get\_envs](https://github.com/foxmask/autodeploy-make-delivery/blob/master/get_env.py)
(parsant le fichier XML) pour obtenir les noms des applications de mon
environnement et en extraire les URL de chacune

```python
from get_env import get_apps
[...]
#get the data from the get_env class which read the ConfigWrapper file from autodeploy
environment_datas = get_apps(options.environment)
```

Puis make\_delivery lit le fichier de configuration décrivant comment
structurer ma livraison en indiquant le nom de chaque application avec
son dossier de destination.

```ini
[myenv]
#directory to add to the delivery whatever happens
doc: fake

[myenv_apps]
myapp1: app
myapp2: app
myapp3: null

[myenv_software]
myapp4: app
myapp5: path/to/target
myapp6: null #do nothing for this app
myapp7: .
```

Enfin le transfert de fichier se produit et affiche une progress bar
histoire de voir où on en est.

```python
def make_release(environment_name, release_name_dir, environment_datas, configfile):
  for component in environment_datas:
    
    logger.info("Environment =>>> %s Components: %s : Begin " , environment_name , component )
    
    archives = environment_datas[component]
    
    for archive_name in archives:
    os.chdir(curdir)
    destination_directory = config.get(environment_name+"_"+component,archive_name)
    if destination_directory == 'null':
        continue
    #check if the directory exists
    #if yes ; chdir to it
    if os.path.isdir(destination_directory):
        os.chdir(destination_directory)
    #otherwise create it then chdir
    else:
        os.makedirs(destination_directory)
        os.chdir(destination_directory)
                
    #get the url of the archive
    url = archives[archive_name]
    #get the filename part of the URL to download
    file_name = url.split('/')[-1]
    #download the file
    try:
        logger.info("Download %s - url %s" , archive_name,url)
        u = urllib2.urlopen(url)
    except:
        logger.error("Error: %s %s %s" , sys.exc_info()[1],archive_name,url)
        pass
            
    f = open(file_name, 'wb')
    meta = u.info()
    #get the Content Length
    file_size = int(meta.getheaders("Content-Length")[0])
    #display the prgress on the screen
    logger.info("Downloading: %s Bytes: %s" , file_name, file_size)
    
    file_size_dl = 0
    block_sz = 8192
    while True:
        #read the file getting from the url
        buffer = u.read(block_sz)
                
        if not buffer:
        break
    
        file_size_dl += len(buffer)
        f.write(buffer)
        #progressbar
        status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    
    f.close()
    logger.info("Environment =>>> %s Components: %s : End " , environment_name , component )
```

Evidement, dans la foulée tout est loggé,

```python
#set the name of the config logging file from the command line
logging.config.fileConfig(options.configlogfile,disable_existing_loggers=False)
[...]
            
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

#write the logfile in the current working dir
fh = logging.FileHandler('./'+release_name+'.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
fh.setFormatter(formatter)
logger.addHandler(fh) 
```

ainsi je n'ai plus qu'à regarder dans mon fichier
release-YYYYMMDD-name.log si j'ai des erreurs (genre une 404 au hasard
;)

Une fois lancée, la commande affiche ceci :

```log
2013-02-22 10:34:44,398 - make_delivery - INFO - Creation of release-201041.41-20130222
2013-02-22 10:34:44,439 - make_delivery - INFO - Creation of the release 201041.41 from the environment customer1-testing
2013-02-22 10:34:44,439 - make_delivery - INFO - Reading config file /root/MakeDelivery/env_dirs.conf 
2013-02-22 10:34:44,470 - get_env - INFO - Read the Autodeploy config file http://autodeploy.domain.com/ConfigurationWrapper
2013-02-22 10:34:45,059 - make_delivery - INFO - Environment =>>> customer1-testing Components: apps : Begin 
2013-02-22 10:34:45,104 - make_delivery - INFO - Download myapp1 - url  http://maven.domain.com/deliveries/myapp1/releases/myapp_2.19.23_weblogic.tar.gz
2013-02-22 10:34:45,169 - make_delivery - INFO - Downloading: myapp1.19.23_weblogic.tar.gz Bytes: 29585377
2013-02-22 10:34:46,572 - make_delivery - INFO - Download myapp2 - url  http://maven.domain.com/deliveries/myapp2/releases/myapp2_2010.r1.2.44.42_core_weblogic.tar.gz
2013-02-22 10:34:46,652 - make_delivery - INFO - Downloading: myapp2_2010.r1.2.44.42_core_weblogic.tar.gz Bytes: 67769731
2013-02-22 10:34:49,681 - make_delivery - INFO - Download framework - url  http://maven.domain.com/maven2/internal/services/framework/framework/1.16.29/framework-1.16.29-delivery.tar.gz
2013-02-22 10:34:49,733 - make_delivery - INFO - Downloading: framework-1.16.29-delivery.tar.gz Bytes: 11556974
2013-02-22 10:34:50,231 - make_delivery - INFO - Download myapp3 - url  http://maven.domain.com/deliveries/myapp3/releases/myapp3_2010.r1.1.37.42_weblogic.tar.gz
2013-02-22 10:34:50,303 - make_delivery - INFO - Downloading: myapp3_2010.r1.1.37.42_weblogic.tar.gz Bytes: 51400921
2013-02-22 10:34:52,224 - make_delivery - INFO - Download portal - url  http://maven.domain.com/maven2/internal/services/portal/portal/1.10.18/portal-1.10.18-delivery.tar.gz
2013-02-22 10:34:52,276 - make_delivery - INFO - Downloading: portal-1.10.18-delivery.tar.gz Bytes: 16350871
2013-02-22 10:34:52,969 - make_delivery - INFO - Download myapp4 - url  http://repo.domain.com/deliveries/myapp4/releases/myapp4_2010.r1.1.31.38_weblogic.tar.gz
2013-02-22 10:34:53,061 - make_delivery - INFO - Downloading: myapp4_2010.r1.1.31.38_weblogic.tar.gz Bytes: 60468113
2013-02-22 10:34:55,450 - make_delivery - INFO - Environment =>>> customer1-testing Components: apps : End 
2013-02-22 10:34:55,450 - make_delivery - INFO - Environment =>>> customer1-testing Components: software : Begin 
2013-02-22 10:34:56,677 - make_delivery - INFO - Download database - url  http://maven.domain.com/maven2/internal/database/2010.r1.3.23.41/database-2010.r1.3.23.41.tar.gz
2013-02-22 10:34:56,727 - make_delivery - INFO - Downloading: database-2010.r1.3.23.41.tar.gz Bytes: 4902673
2013-02-22 10:35:11,832 - make_delivery - INFO - Download database2 - url  http://maven.domain.com/maven2/internal/database2/database2/1.48.12/database2-1.48.12-delivery.tar.gz
2013-02-22 10:35:11,868 - make_delivery - INFO - Downloading: database2-1.48.12-delivery.tar.gz Bytes: 10995334
2013-02-22 10:35:12,321 - make_delivery - INFO - Environment =>>> customer1-testing Components: software : End 
2013-02-22 10:35:12,321 - root - INFO - Environment =>>> customer1-testing download successfull completed
```

On m'a cité il y a quelques temps l'usage de la lib
"[requests](http://docs.python-requests.org/en/latest/)" plutôt que
urllib2 car plus souple et facile de mise en oeuvre notamment pour gérer
l'auth. Ici je n'ai nul besoin d'auth c'est un accès réseau sur
l'intranet ;)

Si vous voulez zieuter de plus près les sources de ce script, ou plus
simplement en avoir une vue d'ensemble, [il se trouve ici sur
github](https://github.com/foxmask/autodeploy-make-delivery)

Etant loin d'être un pro dans le domaine c'est modestement que j'ai
tenté l'exercice de vous montrer étape par étape, comment "ça marche"
chez moi.

Ce script marche parfaitement en prod, et me permet d'économiser un
temps monstreux :

-   plus besoin de faire les mkdir
-   plus besoin de faire les wget des presque 60 archives que
    constituent une "livraison" à mes clients
-   le script ne prend que 3 minutes à produire ma livraison pour le
    plus "gros" client.  
    Avant ce script il me fallait en passer par mkdir + wget avec
    risque d'erreurs potentielles ... =\> 1heure

J'ai dans le pipe, la création d'une RELEASE NOTE listant au client les
éléments fournis, dans un doc PDF, document note que je ponds
manuellement aujourd'hui : un tableau des versions avec instructions
d'installation =\> re une heure de perdue ... alors qu'apres un test
d'une soluce python ça me prendrait 1min :)

Voilou :

N'hésitez pas à me faire un retour, si j'ai pu vous donner envie de vous
mettre à python (si vous veniez de php comme bibi), si vous avez trouvé
ça trop "weak"/trop juste, trop chiant, ou juste "pas mal", je suis prêt
à tout entendre ;)

