# ProjetVisualisationDonnees

Projet Visualisation de données -----------------------

1) Apres avoir clonné le projet dans un dossier, allez dans la racine et créez votre environement virtuel (si vous utilisez pycharm, l'environement se crée automatiquement)
    - pour créer votre environnement virtuel allez dans l'invite de commande (ouvrez le en tant qu'admin de préférence), puis tapez : 
    py -m venv venv

2) Activez votre environement virtuel 
 - pour activer votre environnnement virtuel aller dans le répertoire venv puis Scripts et lancez activate.bat (deactvate.bat pour désactiver l'environnement) ou bien tappez sur l'invite de commande venv\Scripts\activate
 - si l'environnement ne s'active pas cela voudrait surement dire que vous ne pouvez pas activer de script inconnus. Pour remédier a cela ouvrez un terminal Powershell en tant qu'admin puis tappez la commande : 
    Set-ExecutionPolicy Unrestricted 
- Confirmez!


3) Maintenant Installez les exigences (requierement.txt avec pip)
    - pip install -r requirements.txt 

4) Pour ce Projet nous aurons besoins de quelques outils : 
    - Looping 
        Lien de téléchargement : https://www.wampserver.com/en/download-wampserver-64bits/

    - Wamp Server dans lequel vous aurez accès a phpmyadmin.
        Lien de téléchargement :
        https://www.looping-mcd.fr/

5) Nous allons premierement commencer par la création de notre base de données sur php my admin: 
    - Commencez par créer la base de donnée e_commerce dans le querySelector, pour cela utiliser le fichier creationEcommerce.sql; les différentes requêtes s' trouvent.
    - Ensuite créez les différentes tables en utilisant toujours le même fichier creationEcommerce (Assurez vous que vous utilisez bien la base e-commerce --> use e_commerce)
    
