Title: de PHP à Python : Gangnam Style
Date: 2013-02-04 10:00
Author: foxmask
Category: Techno
Tags: ApacheMySqlPHP, python
Slug: gangam-style
Status: published

"Gangnam Style" kézako : Bon en fait j'étais parti vous parler
sérieusement avec un titre *de PSR-1 à PEP8* mais ca manquait de fun ;-)

Donc le sujet du jour de la série "[de PHP à
Python](/post/2013/01/14/de-php-a-python-tous-ensemble/ "de PHP à Python : tous ensemble")",
comme le laisse supposer (ceux qui connaissent) ces 2 'codes' PSR-1 &
PEP8 : les règles de coding dans chacun des 2 langages.  
Je me suis dit qu'après tout, on ne pouvait pas aborder le passage à
python sans en passer par les règles de "rédaction", donc voici.

**de PHP ...**

Pour PHP la définition de la
[PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md)
est toute récente, et comme le rappelle
[mageekguy](http://blog.mageekbox.net/?post/2012/06/19/%C3%80-propos-de-PSR-0%2C-PSR-1-et-PSR-2),
celle ci est somme toute très subjective car cela n'empêchera personne
de coder comme il a toujours fait, et cette règle peut déranger les
habitudes de tout à chacun (moi le premier :) exemple de code :

```php

Pourquoi diable pour les fonctions les accolades sont à la ligne suivante et pas sur celle du if ?
Perso, je les ai toujours TOUTES mises sur la même ligne, une habitude prise avec PERL :)
... à Python 
La PEP8 quant à elle n'a que 12 ans ...
Les accolades n'existent pas on met des ":" sur la même ligne que l'instruction et on indent de 4 espaces.
Voici à quoi cela ressemble et on en discute après :


#Use 4 spaces per indentation level.
foo = long_function_name(var_one, var_two, var_three, var_four)

def long_function_name(var_one, var_two, var_three, var_four):
    print(var_one)
```

on remarquera qu'en php on défini une fonction par le mot clé
"function", ici on utilisera "def"

Le Python n'étant pas rigide en tout point, parfois "la queue" (ligne de
code) est un peu longue donc on la "retrousse" comme suit :  

[![Un python qui se fait tout petit](/static/2013/01/Green-python-around-tree-1-300x225.jpg)](/static/2013/01/Green-python-around-tree-1.jpg)


```python
# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

C'est tout aussi lisible et l'indentation fait son office

Alors certes cela peut perturber le développeur PHP au début, mais si
comme moi vous aimez que ca soit au carré vous vous y ferez super vite.

La PEP8 définie également le nombre de lignes blanches entre 2 "def" ou
la taille maximum de caractères par ligne.

Une autre règle importante concerne les imports.

En PHP on n'ira pas écrire

```php
use Customer, Order
```

mais bien

```php
use Customer
use Order
```

En Python on n'écrira pas non plus

```python
import customer, order
```

mais bien 2 imports distincts

```python
import customer
import order
```

on retiendra que si la PEP8 n'est pas respectée, en exécutant votre
script python vous aurez droit à une belle erreur ;)

PHP a coté est largement plus laxiste !

Par exemple j'avais pris pour habitude d(e volontairement) écrire ce
genre de tru,c pour bien le repérer visuellement plus tard, et le
retirer quand j'avais fini de débogger :

```php
function bagnole_spec($voiture) {
var_dump($voiture);
   if ( in_array($voiture,'nb_portes')) {
       echo $voiture['nb_portes'];
   }
}
```

En python, aucun atermoiement n'est possible, on ne peut pas faire du
code crade même temporairement, ça doit pas dépasser. L'ordre de facto
on s'y fait, après tout le deboggage a sa place, autant ne pas le
négliger :)

**Conclusion :**  
Bon évidement la PSR-1 ne se contente pas que de cela de même que la
PEP8 ne se borne pas à ces limitations/impositions de style.

Se conformer aux règles a du bon dès le départ, bon sauf quand ça fait
plus de 10 piges qu'on crache du code et qu'on vous dit qu'il faut
changer ;)

De toute façon avec des IDE modernes vous aurez tout loisir que ce
dernier vérifie que votre code colle aux exigences du langage.  
Par exemple avec Python et [Aptana](http://www.aptana.com/) vous pouvez
ajouter les lib qui permettent à l'IDE de valider que votre code n'est
pas écrit de travers, l'une d'elle est
[pylint](http://www.logilab.org/857), ça donne cela :

[![PEP8 avec Pylint dans Aptana](/static/2013/01/pep8.png)](/static/2013/01/pep8.png)

Comme on voit là sur la ligne *return render*, j'ai bien le droit de me
faire plaisir par quelques retours à la ligne alignés sur la parenthèse
ouvrante, quant à la ligne *logger.debug* on la voit beaucoup trop
longue. Là python ne poussera pas le bouchon à nous invalider le code
pour "si peu".

Pour en revenir à "Gangnam Style": avec les accolades à tirelarigot on a
vraiment l'impression d'avoir une posture de 'code' sur un canasson
(quand on code pas comme un bourrin ;) et coté Python, d'aucuns diront
qu'ils sont des poneys zailés ;)

