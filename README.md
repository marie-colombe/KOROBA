******Projet KOROBA****



LEAD: NYOA Ama Marie-Colombe

DEVELOPPEUR BACK-END:
- TIAN Bi Toi Ange
- DIARRASSOUBA Ibrahim
- NYOA Ama Marie-Colombe
  

DEVELOPPEUR FRONT-END:
- GOULIZAN Racine
- BERTHE Habib
- NYOA Ama Marie-Colombe

***Nos differentes fonctionnalités***

. Gestion des clients

.Gestion du panier

.Gestion de la méthode de paiement

.Gestion des commandes

.Gestion des produits

.Gestion des artisans


***Comment exécuter notre application***

 Installer python sur sa machine

pour vérifier qu'il a bien été installé taper la commande suivante dans le terminal:

python --version 

Vous devez avoir un resultat similaire a cette ligne (la version peut ne pas etre la même)

python 3.12.6

Si pas fait au préalable, vous pouvez télécharger le fichier d'installation sur https://www.python.org/downloads/ 


Avoir Postgresql installé sur sa machine , si vous l'avez pas, vous pouvez le telecharger sur https://www.postgresql.org/download/


Créer un dosssier pour contenir tout notre projet

Ouvrir le terminal et se déplacer jusqu'au dossier ave la commande cd 

Creer l'environnement virtuel avec

python -m venv env

Activer son environnement virtuel

.\env\Scripts\activate

Telecharger le projet avec ce lien ou avec la commande

git clone https://github.com/marie-colombe/KOROBA-BACK-END.git

Apres telechargement, s'assurer d'avoir l'environnement virtuel ainsi que les dossiers et fichiers
du projet telechargés dans le dossier (celui creer au depart et sur qui pointe notre terminal)

Installer les dépendances de notre projet avec la commande suivante: 

pip install -r requirements.txt

On s'assure d'avoir creer une base de donnée dans Postegresql et on verifie
la configuration dans le fichier settings.py contenu dans le dossier management.

On lance nos migrations avec

  python src\manage.py makemigrations 
    
  python src\manage.py migrate 
    
  On lance notre projet

  python src\manage.py runserver

  On va dans le navigateur et on tape

   http://127.0.0.1:8000




