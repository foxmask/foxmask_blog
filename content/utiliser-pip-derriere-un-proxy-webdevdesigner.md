Title: Utiliser pip derrière un proxy - webdevdesigner
Date: 2022-02-03 13:14:54.486563+00:00
Author: FoxMaSk 
Tags: pip, python, proxy
Category: link
Status: published





# Utiliser pip derrière un proxy - webdevdesigner

[Utiliser pip derrière un proxy - webdevdesigner](https://webdevdesigner.com/q/using-pip-behind-a-proxy-7267/)


j\&#39;essaie d\&#39;utiliser [pip](https://over.wiki/pip/) derrière un
[proxy](https://over.wiki/proxy/) au travail.

l\&#39;Une des réponses de ce post a suggéré d\&#39;utiliser CNTLM . Je l\&#39;ai
installé et configuré par cet autre post , mais l\&#39;exécution
`cntlm.exe -c cntlm.ini -I -M http://google.com` a donné l\&#39;erreur
`Connection to proxy failed, bailing out` .

j\&#39;ai aussi essayé `pip install -–proxy=user:pass@localhost:3128` (le
port CNTLM par défaut...
