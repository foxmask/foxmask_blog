Title: Python ChatGPT, CCBV, Metaclasses
Date: 2023-06-18 17:00
Author: foxmask
Category: Techno
Tags: chatgpt, python, cbv, metaclasses, django
Slug: pythno-chatgpt-ccbv-metaclasses
Status: published



# Python et ChatGPT : attention !

> ChatGPT: Your Personal Python Coding Mentor

> Beware of Incorrect and Irrelevant Information[](https://realpython.com/chatgpt-coding-mentor-python/#beware-of-incorrect-and-irrelevant-information "Permanent link")
>
Now that you’ve signed up for ChatGPT, you probably want to give it a spin! But before you hit the throttle, it’s important to know what kinds of issues you might run into. While large language models offer several new possibilities for enhancing your studies, you need to remember the potentially negative effects of using ChatGPT as your coding mentor:
>
>-   **Overreliance:** Leaning too heavily on ChatGPT for answers can hinder your own learning. You build brain paths by thinking, struggling, checking your understanding, and memorizing information.
>-   **Accuracy:** ChatGPT’s responses may often be inaccurate or irrelevant. You need to fact-check all of its answers! Otherwise, you might learn wrong concepts and bad practices.

https://realpython.com/chatgpt-coding-mentor-python/

Un petit passage sur le [discord de l'afpy](https://www.afpy.org/discord) pour demander un coup de main (sans en être gêné) devrait largement vous aider  


# Les Metaclasses

La [doc python](https://docs.python.org/3/reference/datamodel.html#metaclasses) etant un poil légère sur la question, chez [RealPython](https://realpython.com/python-metaclasses/), on nous explique la magie derrière les Metaclasses utilisées par Django et SQLAlchemy. La meme notion abordée chez [Zest de Savoir](https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/4-classes/2-metaclasses/) pour les francophones.


# CCBV.co.uk et DRF.co

à toutes finzutiles 

1 - Quand on veut creuser les `ClassBasedView`  en allant directement à l'essentiel et decouvrir qui herite de qui et quoi, où chopper tel parms de l'url, ou comment paginer ou  passer un self.request.user dans une ListView.

2 - Egalement, on est souvent devant les questions du genre 
- mais où je suis dans le workflow des methodes des CBV ?
- quand puis je utiliser `get_context_data` plutot que `get_queryset` ou quand me servir des 2 ?

Le kiff, vous verrez, quand on commence à bien saisir la chose, c'est de se faire ses propres Mixins pour reduire le code à peau de chagrin en evitant de retrouver 'n' fois le meme code dans 'n' xxxViews differentes.

Django fourni une quantité astronomique de `Mixins` évidement, comme le très très connu `LoginRequiredMixin`

Qui permet avec ce bout de code 

```python
class Home(LoginRequiredMixin, MySoftwareVersionMixin, CreateView):
   [...]
```
de permettre de créer un object si et seulement si, l'utilisateur est connecté.

Vous verrez dans les regles d'utilisations des mixins, qu'il faut toujours les mettre avant la View. 
Le mixin `MySoftwareVersionMixin` pourrait servir à peupler le context d'une page (dans (`get_context_data` de la View) pour afficher la version de son soft dans un pied de page for example

Avec https://ccbv.co.uk/ et son petit frere pour Django Rest Framework https://www.cdrf.co/ , vous voilà pourvus


# Django 5 - Resultat des elections du conseil de pilotage

[En un coup d'oeil](https://www.djangoproject.com/weblog/2023/may/16/django-5x-steering-council-election-results/)


# Django release de secu

[pour les versions 4.2.1, 4.1.9, 3.2.19 (la version LTS)](https://www.djangoproject.com/weblog/2023/may/03/security-releases/) 


# Pastèque : Le Pastebin de de l'afpy 

Lachez les autres site de "copier/coller de code" pour celui de l'afpy :D

https://p.afpy.org/


# HTTPX : requests en meuh !

[Version 0.24.1](https://github.com/encode/httpx/releases/tag/0.24.1) is Sortie !

[HTTPX](https://www.python-httpx.org/) continue son bonhomme de chemin https://github.com/encode/httpx/releases !
Les releases sortent avec dichotomie

