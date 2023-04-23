Title: Personnaliser les CSS de ses sites favroris
Date: 2022-05-07 08:52:54.452649+00:00
Author: FoxMaSk 
Category: link
Tags: css, mastodon
Status: published





# Personnaliser les CSS de ses sites favroris

[Personnaliser les CSS de ses sites favroris](None)

Sur mastodon, au detour d&#39;une question à un admin de l&#39;instance où je lui demande 

&#34;pourriez vous mettre des CSS qui prennent toute la largeur du browser quand on coche la case &#39;activer l interface avancée&#39;&#34;

Un utilisateur m&#39;a fait une reponse :

utilisez une extension du browser pour appliquer ces regles ci :

```css
.public-layout .column-0 .public-account-header__image { background: #6494ed; }
.public-layout .column-0 .public-account-header__image img { object-fit: contain; }

@media screen and (min-width: 631px) { .column { flex-grow: 1; } }
@media screen and (min-width: 631px) and (max-width: 1919px) { .drawer { width: 250px; } }
.rich-formatting h2, .rich-formatting h3 { margin-top: 30px; }
```

avec l&#39;extension : https://stylebot.dev/

et le tour est joué