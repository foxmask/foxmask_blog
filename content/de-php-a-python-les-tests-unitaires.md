Title: de PHP à Python : les tests unitaires
Date: 2013-02-12 10:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, python
Slug: de-php-a-python-les-tests-unitaires
Status: published

Nouvel épisode de la série [de PHP à
Python](/post/2013/01/14/de-php-a-python-tous-ensemble/ "de PHP à Python : tous ensemble").

Cette fois ci nous allons nous pencher sur l'incontournable outil du dev
voulant s'assurer la qualité de son code et de sa non régression : le
test unitaire.

![Tests Unitaires](http://blog.pagesd.info/public/ContactManagement/unit-testing.png)](http://blog.pagesd.info/public/ContactManagement/unit-testing.png)

J'aborderai succinctement comment on s'y prend en PHP pour ensuite vous
montrer l'équivalent Python et finirai par d'autres moyens dont dispose
Python dans son arsenal.

**de PHP ...**  
Alors d'avance désolé, mais je ne vais pas aborder
[Atoum](https://github.com/atoum "Atoum l'autre pays du test unitaire;)"),
quand bien même cela ne me déplairait pas :) Le but étant de montrer
comment en PHP on fait un test unitaire et retrouver une smilitude voire
carrement des ressemblances avec Python. Atoum n'existant pas dans une
version Pythonesque, ca sera donc PHPUnit puisque de ce coté là, un
pendant Python existe ;)

Donc [PHPUnit](https://fr.wikipedia.org/wiki/PHPUnit) est bien connu des
développeurs PHP et est donc un framework de tests unitaires dérivé de
JUnit (issue du monde Java)

Voici donc un **script
[test.php](https://raw.github.com/foxmask/de_php_a_python/les_tests_unitaires/test.php "télécharger les sources")**
contenant ce qui suit :

```php
cal = new Calc();
    }
    public function testMoyenne() {
        $this->assertEquals($this->cal->moyenne(array(1,2,3)),2);
        $this->assertEquals($this->cal->moyenne(array(2,4,6)),4);
    }

        public function testDivision() {    
        $cal = new Calc();
        $this->assertEquals($this->cal->division(10,5),2);
        
    }
}
?>
```

**[calculs.php](https://raw.github.com/foxmask/de_php_a_python/les_tests_unitaires/calculs.php "télécharger les sources")**
quant à lui contient :

```php

J'ai volontairement éluder la question de la division par zéro, on va le voir plus tard.
le resultat du test donne ceci :

phpunit test.php 
PHPUnit 3.4.14 by Sebastian Bergmann.
..

Time: 0 seconds, Memory: 6.50Mb

OK (2 tests, 3 assertions)
```

Et "voilà" :)

**.... à Python**

*partie 1 : unittest*

Coté du fameux reptile, il s'agit de
"[unittest](http://docs.python.org/3/library/unittest.html)" et est
également un framework de tests unitaires, dérivé du même JUnit - donc
on peut déjà se frotter les mains, l'acquis sur PHPUnit pour passer à
unittest devrait être le plus smoothy possible :)

Petite définition en passant d'unittest, toute droit sortie de la doc :

> The Python unit testing framework, sometimes referred to as “PyUnit,”
> is a Python language version of JUnit, by Kent Beck and Erich Gamma.
> JUnit is, in turn, a Java version of Kent’s Smalltalk testing
> framework. Each is the de facto standard unit testing framework for
> its respective language.

voici
**[test.py](https://raw.github.com/foxmask/de_php_a_python/les_tests_unitaires/test.py "télécharger les sources")**

```python
import unittest

from calculs import moyenne
from calculs import division

class CalculsTest(unittest.TestCase):   

    def test_moyenne(self):
        self.assertEquals(moyenne(1, 2, 3), 2)
        self.assertEquals(moyenne(2, 4, 6), 4)
    
    def test_division(self):
        self.assertEquals(division(10, 5), 2)

if __name__ == '__main__':
    unittest.main()
```

et
**[calculs.py](https://raw.github.com/foxmask/de_php_a_python/les_tests_unitaires/calculs.py "télécharger les sources")**

```python
def moyenne(*args):
    length = len(args)
    sum = 0
    for num in args:
        sum += num
    return float(sum) / float(length)
        
    
def division(a, b):
    return a / b
```

ce qui donne un fois lancé :

```shell
python test.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Quant à la division par Zéro volontairement omise voici en Python
comment on la gère et la teste :

```python
[...]
class CalculsTest(unittest.TestCase):   
[...]
    def test_division(self):
        self.assertEquals(division(10, 5), 2)
        self.assertRaises(ZeroDivisionError, division, 10, 0)
```

Pour PHPUnit, on n'a semble-t-il toujours rien en magasin qui permette
de tester quelle méthode lève bien l'exception attendue, alors qu'[Atoum
oui](http://docs.atoum.org/en/chapter2.html#exception) ;)

une note finale, sur cette partie, pour rendre à césar le code Python
ici est entièrement extrait du livre de Tarek Ziadé "Python, Petit guide
à l'usage du développeur agile"

*Partie 2 : doctest*  
A présent que nous avons vu les TU *unittest*, Python possède une
seconde méthode de tests :
[doctest](http://docs.python.org/3/library/doctest.html).

Comment fonctionne-t-elle ?

Le module doctest, au lancement de la commande python, va scruter votre
code source à la recherche de texte ressemblant à un session python et
une fois trouvé, exécutera justement la session python.

Exemple :
[mynameis.py](https://raw.github.com/foxmask/de_php_a_python/les_tests_unitaires/mynameis.py "télécharger les sources")

```python
"""
>>> my_name_is("foxmask")
'foxmask'
"""
def my_name_is(string):
    return string

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

pour tester on fera :

```shell
$ python mynameis.py
$
```

rien s'affiche, donc pas d'erreur - bon voyons le mode verbose quand
même puisqu'on est curieux :

```shell
python mynameis.py  -v
Trying:
    my_name_is("foxmask")
Expecting:
    'foxmask'
ok
1 items had no tests:
    __main__.my_name_is
1 items passed all tests:
   1 tests in __main__
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
```

Vous pourriez vous demander pourquoi faire 2 outils pour la même chose
finalement ?  
Doctest permet également de produire de la doc et les docstring comme
on les appelle permettent cela tout autant que de tester la non
régression de votre code qui aurait pu varié.

D'aucuns diront (l'un d'eux se reconnaitra ;) que l'on n'a pas écrit le
code du test avant le code lui-même, mais l'inverse, et que donc doctest
vérifie le résultat de son exécution. Ce n'est pas faux mais ça fait
quand même son boulot ;)

Il existe enfin une dernière méthode dite *DDD* : le Développement
Dirigé par la Documentation. Je ne l'ai pas encore abordée et ne
pourrait vous en dire plus en détails, juste qu'elle existe.

nota : [les sources de l'article sont sur
github](https://github.com/foxmask/de_php_a_python/tree/les_tests_unitaires);)

