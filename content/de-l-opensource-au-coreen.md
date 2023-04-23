Title: de l&#39;opensource au coréen
Date: 2022-05-19 18:25:25.150774+00:00
Author: FoxMaSk 
Tags: opensource
Category: link
Status: published



# de l&#39;opensource au coréen

[de l&#39;opensource au coréen](None)

Un truc qui plombe grandement nos projets opensources, pour la majorité d&#39;entre nous qui les gérons solo, outre que personne n&#39;a envie de contribuer, c&#39;est la pérennité des lib, ou (de la version) du langage utilisé(e), qui nous pousse sans cesse à &#34;rester&#34; à jour avec ses dépendances.



Sauf que, à un moment, seul devant sa feuille, se farcir des update de framework/lib, quand on considère que son projet est stable comme il est, ça devient très pénible.



Du coup on se retrouve par la force des choses, à planter là son projet malgré nous, ne plus le mettre à jour et le rendre inutilisable dès lors qu&#39;une des lib en dépendance aura changé son API.



Par exemple, un projet que j&#39;avais réalisé, permettait de faire communiquer des données provenant d&#39;une bonne grosse poignée de lib tierce comme Evernote Twitter mastodon wallabag, slack, mattermost et j&#39;en passe



Quand tout cela marchait de concert c&#39;était génial.

Mais dès qu&#39;il fallait suivre les évolutions de chacune d&#39;elle + les dépréciations de Django + les versions de python qui évoluaient à leur tour + la base de données + la distribution de linux (qui supportait une autre version de python) + l&#39;OS lui-même ...

Mais on connait tous les effets/méfaits de la course aux corrections de bug, failles de secu, &#34;ameliorations&#34;, que cela engendrent pour nos (petits) projets.



Alors qu&#39;avec une Django 2.2 et un python 3.6, tout marchait. 



Ces modif et améliorations font certes partie du quotidien de la vie d&#39;un projet, et quand on est plusieurs, on s&#39;en sort à peu près.



Du coup, à part une solution dégeu: se faire des images docker qui permettraient de &#34;cryogéniser&#34; nos projets avec tout le package des dépendances, je ne vois pas trop comment ne pas faire arakiri à ses projets.



J&#39;ai lu sur twitter un post interessant (pour une fois hein;) et tout à fait pertinent (desole je ne l&#39;ai pas retrouvé). Ce n&#39;est pas parce qu&#39;un projet n&#39;évolue pas qu&#39;il est soit abandonné, soit moisi, soit ne marche pas/plus. C&#39;est juste qu&#39;il est mature comme il est et qu&#39;on en est content tel quel (auteur comme utilisateur).



Peut-être la solution ultime est de pondre un projet sans aucune dépendance, autre que celle du langage de programmation utilisé ?

J&#39;ai croisé peu de projets n&#39;ayant que le langage pour dependance (et même aucune base de données) : 

En PHP : &#34;Shaarli&#34;. 

En JS : Je n&#39;ai pas creusé 0bin mais ca doit pas en être loin non plus.

En Python je n&#39;ai pas trouvé de projet complet (qui ne soit pas une lib ou un framework) avec quasi aucune dependance



Pour ma part, les derniers produits sont avec python/django ou starlette/sqlite/feedparser



Sinon on peut faire encore mieux, comme bibi et se mettre au 



co ré en ! 



à part un peu de sous (avec un CPF;) et de temps (qu&#39;on retrouve en lachant &#34;l&#39;ingrat opensource&#34;), comme dependances,  c&#39;est tout !