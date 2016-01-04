Title: de PHP à Python : Minie petite souris
Date: 2013-03-04 10:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, python
Slug: de-php-a-python-minie-petite-souris
Status: published

Nouvel opus de la série de [de PHP à
Python](/post/2013/01/14/de-php-a-python-tous-ensemble/ "de PHP à Python : tous ensemble").

Aujourd'hui, Comment parcourir un fichier de configuration ini ?

Alors en intro, un truc bien cool pour tout à chacun : les fichiers ini
se lisent aussi bien avec Python que PHP.

Zavez une appli avec un bon (gros) fichier de config au format ini ; pas
de problème, vous allez voir ce que vous allez voir ;)

Pour illustrer ce billet j'ai pris un fichier de config de mon forum
[HaveFnuBB](http://havefnubb.foxmask.info "HaveFnuBB! Forum PHP Libre et Open Source | Free Open Source PHP Forum")
écrit en PHP [que
voici](https://github.com/havefnubb/havefnubb/blob/master/havefnubb/var/config/defaultconfig.ini.php.dist "defaultconfig.ini.dist de HaveFnuBB")

Le bout de code PHP lisant mon fichier de config permet de connaitre les
Réponses HTML possible, le code est le suivant :  
**de PHP ...**

```php

Ceci affichera les valeurs de mes variables définies dans ma section sus mentionnée

array(3) {
  ["minifyCSS"]=>
  string(1) "1"
  ["minifyJS"]=>
  string(0) ""
  ["minifyCheckCacheFiletime"]=>
  string(0) ""
}
```

**... à Python**  
Pour le script python cela donnera

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.getcwd()+'/havefnubb/var/config/defaultconfig.ini.php.dist')
print config.items('jResponseHtml')
```

pour obtenir en résultat :

```python
[('minifyjs', 'off'), ('minifycss', 'on'), ('minifycheckcachefiletime', 'off')]
```

Pour l'oeil aguerri, vous aurez remarqué que 1 est devenu on et "" est
devenu off pour python.

Le module
[ConfigParser](http://docs.python.org/2/library/configparser.html) ne se
contente pas que de vous afficher le contenu d'une section (fort
heureusement).  
Avec celui-ci vous avez un accès direct à tous les paramètres avec une
instruction *get* comme ceci :

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.getcwd()+'/havefnubb/var/config/defaultconfig.ini.php.dist')
print config.get('jResponseHtml','minifyjs')
```

vous affichera le "off" vu plus haut.

Outre l'accès direct, vous pouvez également pondre un fichier de config
à la volée en commençant par ajouter la section puis les variables
distinctes comme ceci :

```python
import ConfigParser

config = ConfigParser.RawConfigParser()

config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'wb') as configfile:
    config.write(configfile)
```

Produira un fichier **example.cfg**:

```ini
[Section1]
an_int=15
a_bool=true
a_float=3.1415
baz=fun
bar=Python
foo=%(bar)s is %(baz)s!
```

ici %(bar) et %(baz) seront remplacées par les valeurs de leur variable
définie juste au dessus

Coté PHP on n'a rien d'équivalent... sauf au sein de(s) framework(s) PHP
comme Jelix et sa méthode
**[jIniFileModifier('fichier')-\>getValue('variable','section')](https://github.com/havefnubb/havefnubb/blob/master/havefnubb/migration/wizard/pages/migrate/migrate.page.php#L355)**

*La prochaine partie traitera du traitement de la journalisation (les
logs)*

