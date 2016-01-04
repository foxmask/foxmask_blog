Title: de PHP à Python : X aime L
Date: 2013-02-18 10:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, python
Slug: de-php-a-python-x-aime-l
Status: published

Nouvel opus de la série de [de PHP à
Python](/post/2013/01/14/de-php-a-python-tous-ensemble/ "de PHP à Python : tous ensemble").

Aujourd'hui, Comment parcourir un fichier XML ?

Bon en plus je vais pousser le bouchon à utiliser XPath ;) tant qu'à
lire un fichier, autant que ça soit "intelligent" et pas juste lire pour
lire (quoi je me répète répète;)

La *matière première* commune à ces 2 scripts sera ce fichier XML allégé
pour l'occasion mais issu directement de
[autodeploy](http://buildprocess.sourceforge.net/) un outil ( opensource
devrai-je le préciser ? ) que j'utilise au quotidien pour faire des
déploiements d'applications les doigts dans le nez ;)


En prod je n'ai *que* 200 environnements, avec en moyenne près de 10
targz chacun, je vous laisse imaginez le poids du trucs (pres de 10Mo
grosso merdo;) Vivendi qui s'en sert en gere 10x plus ;)

Ici je n'en extrairai que le nom de l'application/software et l'URL

**de PHP ...**  
la version PHP donne ceci avec un coup de DOMXPath :

```php
Load('ConfigurationWrapper');
$xpath  = new DOMXPath($doc);

$app = find_archive($xpath,$envName,'/applicationservers/applicationserver/applications/application');

$soft = find_archive($xpath,$envName,'/softwares/software');

function find_archive(DOMXPath $xpath, $envName, $queryPath) {
    $query = '//environments/environment[@name="'.$envName.'"]'.$queryPath;
    $entries = $xpath->query($query);
    foreach ($entries as $entry) {
        echo $entry->getAttribute('name')  . ' ' . $entry->getAttribute('uri') ."\n";
    }
}
```

affichera :

```shell
app1 http://maven.intranet.mycompany.com/repository/my-app1.tar.gz
app2 http://maven.intranet.mycompany.com/repository/my-app2.tar.gz
My Oracle Upgrade http://maven.intranet.mycompany.com/repository/my-oracle-upgrade.tar.gz
```

**... à Python**  
Le même process en Python avec cette fois ci le [module
LXML](http://lxml.de/tutorial.html) donne ceci :

```python
# -*- coding: utf-8 -*-
from lxml import etree
from lxml.etree import Element  

autodeploy_filename = 'ConfigurationWrapper'
env = 'my-environmentA'

def find_archive(env_name,tree,xpath):

    my_nodes = tree.xpath('//environments/environment[@name="'+env_name+'"]'+xpath);

    for node in my_nodes:
        if len(node.get('uri',None)) > 0:
            print "{name} {uri}".format(name=node.get('name',None),uri= node.get('uri',None))

tree = etree.parse(autodeploy_filename)

#get the name of the applications
find_archive(env,tree,'/applicationservers/applicationserver/applications/application')

#get the name of the Software
find_archive(env,tree,'/softwares/software');
```

affichera :

```shell
app1 http://maven.intranet.mycompany.com/repository/my-app1.tar.gz
app2 http://maven.intranet.mycompany.com/repository/my-app2.tar.gz
My Oracle Upgrade http://maven.intranet.mycompany.com/repository/my-oracle-upgrade.tar.gz
```

Actuellement sur l'intranet j'ai une appli en
[Jelix](http://www.jelix.org), qui parcourt le XML (dans un cache) et
affiche tout le toutim aux end-user (consultants) pour leur permettre de
trouver ce qui est installé sur les environnements jEE ainsi que les
adresses des bases etc...

Quand les consultants veulent que je livre un client avec une release
donnée, alors, à l'autre bout de la chaine j'ai un script Python *home
made*, qui parcourt le même flux et me pond un livrable à partir d'un
fichier de configuration qui me décrit l'arbo cible et dépose chaque
targz dans cette dernière.

D'ailleurs un billet est à venir sur la lecture de fichier de config en
PHP/Python, une histoire de *petite souris* mais je n'en dirais pas plus
;)

