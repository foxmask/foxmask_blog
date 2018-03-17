Title: Migrer de Evernote vers Joplin
Date: 2018-03-17 12:00
Author: foxmask
Tags: Joplin, Evernote
Category: Techno
Slug: migrer-evernote-joplin
Status: published


Petit tuto pour migrer sans encombres ses affaires depuis Evernote vers Joplin.

# Exporter les notes Evernote

Pour importer ses notes Evernote, d'abord exportez les depuis le client Evernote sous windows (en les selectionnant toutes d'un coup) dans une fichier sous le format .enex.

# Importer

Puis, une fois fait, depuis le client Joplin, ouvrez "Fichier > Import > Evernote Export File"

Mon bon gros paquet de 2500 notes (pour une poids de 650Mo) a été intégré sur mon vioc PC un Quad Core avé 6Go de RAM, de 8ans d'age en 25mnn alors que sur la babasse de compet @ work : 10mn...

J'ai dû m'y reprendre à deux fois.

Raison ? 

Hé bien, l'import ne gère pas la création des dossiers existants, et tout arrive dans une dossier Evernote. 

Du coup, pour préparer le terrain en amont, depuis Evernote, j'ai affecté à mes notes, le tag du nom de son dossier où elles se trouvaient.


# Preparer le terrain avant la synchronisation

Une fois l'import effectué, on prendra le temps de retirer les tags créés "expres" pour la migration, mais pas tout de suite.

Pourquoi ?

Comme dit juste avant, l'import ne créé pas les dossiers. Donc : 

* on va créer les dossiers manquants dans joplin à la mimine
* on va cliquer sur chaque tag et faire glisser toutes les notes dans le dossier de destination du même nom que son tag

Du coup on se rend compte que si on supprime les tags avant, l'opération de dispatching va être empirque, voire impossible.

# Synchronisation

Une fois fait tout ce mic mac, on va synchroniser les notes sur OneDrive, pour qu'ensuite ses notes soient dispo sur mobile.

Pour mon cas 2500 notes produisent 8500 " objets " qu'il faut synchroniser. Donc j'ai laissé tel quel afin que la synchornisation se fasse sans encombre.

# Finalisation

Au bout de quelques soirées, la synchro finie, on peut supprimer les tags ajoutés précédemment dans la foulée, et enfin profiter :)


# La suite ?

On va attendre que Joplin s'enrichisse de fonctionnalités, par exemple :

sur le filtrage de notes: 

* recherche une chaine de caractères mais dans un dossier donné 
* recherche une chaine de caractères mais dans un dossier donné sur une période donnée 

sur le suppport de la prise en charge de plus de documents puisque les pdf ou odt n'y ont pas droit de citer pour le moment

etc...

Pour le moment je cherche un moyen de créer des notes en me passant du moindre "client" desktop/mobile.
