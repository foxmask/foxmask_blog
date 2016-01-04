Title: SQL Full Table Scan vs Index - The Usual Suspects
Date: 2013-11-15 17:49
Author: foxmask
Category: Techno
Tags: oracle
Slug: sql-full-table-scan-vs-index
Status: published

Hello,  
Voici un condensé sur ma semaine de formation au Tuning Oracle ;)  
Un condensé de conneries à proscrire pour avoir un RDBMS qui marche
mieux du point de vue du dev, tout du moins, parce que je n'irai pas
saouler le dev avec des noms barbares sur la ram et tout le bataclan :)

Ainsi voici une liste de requêtes SQL à éviter à tout prix au risque de
vous retrouver à faire faire des full scan sur vos "petites" tables.  
**Requête moisie n°1**

```sql
SELECT * FROM salarie WHERE salaire*12 > 6000
```

ici on voudrait les salariés ayant un salaire mensuel supérieur à 60000
par an.  
Or, quand bien même salaire serait un index, Oracle partirait bel et
bien en Full Scan. La preuve avec l'exécution du "plan d'exécution" aka
"explain plan" qui vous le sortira la preuve par neuf ;)

Pour que cette requête fasse son effet avec l'index il faut l'écrire
ainsi :

```sql
SELECT * FROM salarie WHERE salaire > 60000/12
```

**Requête moisie n°2**  
Un autre exemple avec celle-ci

```sql
SELECT * FROM table WHERE upper(name) = 'FOXMASK'
```

les fonctions sur les index partent en full scan systématiquement.  
Si vous tenez à faire cela, il faut explicitement pondre un "function
index" avec, lui aussi upper(name) dessus.

```sql
CREATE INDEX func_upper ON TABLE(UPPER(name));
```

**Requête moisie n°3 sur index non discriminant**  
Autre cas de figure avec des index inutiles :

Les tables avec des données dans une colonne insuffisamment
discriminante provoquera un full scan car le moteur du RDBMS considérera
moins coûteux le full scan que l'index qui n'est pas assez
discriminant.  
Par exemple une colonne "sexe" pour une table "profil".

Encore une fois si vous tenez à cet index, il faudra alors le définir
différemment : en [BITMAP](https://en.wikipedia.org/wiki/Bitmap_index)
et là ça "déchirera" :)

**Cadeau Bonusque**  
en cadeau bonusque pour ceux ce que ca nain téreeserrait, 2 trucs :

1\) Cas d'une requête entre grosses tables :  
postulat : j'ai 2 tables une A, de quelques millions de lignes, une B
de quelque milliers de lignes

```sql
SELECT * FROM A, B where A.id=B.id AND B.status = 1
```

Là, la requête c'est de la bonne daube puisqu'on se farcie l'inner join
pour chaque ID de B et A .  
Or l'ordre dans la clause where compte. Donc pour limiter le coût de la
requête il faudrait la faire comme suit :

```sql
SELECT * FROM A, B where B.status = 1 AND A.id=B.id
```

Évidemment, le moteur du RDBMS devrait trouver le plan d'exécution le
plus adapté mais des fois ce n'est pas le cas, et il faut en passer par
des HINT.

2\) Cas des requêtes retournant les mêmes résultats mais identifiées
différentes : comment est-ce possible ?  
Ceci :

```sql
SELECT * FROM A, B WHERE A.id=B.id AND B.status = 1
```

et Cela (nota j'ai dû shooter la coloration syntaxique qui corrigeait
tout seul ma prose ;)

```text
select * from A, B where A.id=B.id and B.status = 1
```

donneront le même résultat c'est sûr mais consommera de la mémoire 2
fois au lieu d'une car elles ne sont pas écrites de la même façon... le
même cas de figure arrivera avec des espaces en trop entre les
verbes/instructions/tables/colonnes. Ok, ça sera le même résultat mais
l'optimisation pour le moteur du RDBMS au lieu de chopper la requête
dans le cache, ira en coller une de plus dans le cache. Donc le coût
peut s'avérer monstrueux si chacun code comme il le veut dans son coin
sa requête SQL.

**Conclusion** : alors oui j'ai parlé de Oracle mais coté PostGreSQL et
vraie RDBMS opensource, il y a fort à parier que de tels comportements
se produisent au détriment de l'application bien sûr.

