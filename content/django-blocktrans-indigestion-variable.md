Title: Django blocktrans et l'indigestion de variables
Date: 2012-10-15 11:00
Author: foxmask
Category: Techno
Tags: Django
Slug: django-blocktrans-indigestion-variable
Status: published

Dans mes tribulations (d'un Djangonaute en Poneyland) d'exploitation de
modules tiers comme [django
registration](http://docs.b-list.org/django-registration/0.8/), le
template permettant l'envoi de mail est très "free style", comprendre
qu'il est tellement explicite qu'on en perd son latin, du coup dans mes
"débuts" je me suis carrément pris la tête à dépiauter tout la pile
d'appels du "schmilblick".

**Ce qui ne marche pas**

Ainsi j'avais codé :

```python
{% url 'registration_activate' activation_key as registration_activate %}
{% blocktrans%}
Hello,
You wish to subscribe to the service provided by {{ site.name }}.

To confirm your subscription, go on the following page {{ site.domain }}{{ registration_activate }} to activate your account

Your subscription request will expire in  {{ expiration_days }} days if you dont confirm it.

--
2012 - {{ site.domain }}  
{% endblocktrans %}
```

et le mail partant, arrivait comme ceci

```html
Hello,
You wish to subscribe to the service provided by .

To confirm your subscription, go on the following page /accounts/activate/1ccfbb6800bde1b8549f8384cd88fa3d1c931fa3/ to activate your account

Your subscription request will expire in  7 days if you dont confirm it.

--
2012 -
```

Un beau mail ... pourri à souhait, mais que se passe-t-il ?

**WTF ?**  
je suis allé jusqu'à coller des **print** dans le fonction
**send\_activation\_email** du module **registration** mais l'objet site
était correctement peuplé. J'ai rechecké que mes propres
context\_processors n'interfèraient pas avec le template et que le
framework Site était paré.

**Ce qu'il fallait faire**  
Puis d'un coup (il était temps depuis 1h que je tournais en rond à tout
vérifier) je me suis rappellé mais **blocktrans** faisait des
indigestion de variables ... faut les lui faire bouffer tout cru en lui
pinçant le pif avec le keyword **with**!

```python
{% url 'registration_activate' activation_key as registration_activate %}
{% blocktrans with site_name=site.name site_domain=site.domain%}
Hello,
You wish to subscribe to the service provided by {{ site_name }}.

To confirm your subscription, go on the following page {{ site_domain }}{{ registration_activate }} to activate your account

Your subscription request will expire in  {{ expiration_days }} days if you dont confirm it.

--
2012 - {{ site_domain }} 
```

Et voilà !

Ceci m'avait sauté aux yeux avec la tentative d'utilisation de **{% url
.... %}** puisque django hurlait ses grands Dieux que je n'avais pas le
droit de le faire, donc j'avais trouvé à résoudre le problème de url,
mais là Django s'est tu sans dire que site.xxx ne gênait.

