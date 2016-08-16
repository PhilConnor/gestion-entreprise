# Installation du projet

## Configuration de l'environnement

 1 - Installation de Python 3

[Site officiel de python](https://www.python.org/downloads/)

 2 - Installation de PIP

[How to install pip](https://pip.pypa.io/en/latest/installing/)

 3 - Installation des packages requis

>**NOTE :** Cet exemple est pour un usage sous Debian

```
cd ../gestion-entreprise/
pip install -r requirements.txt
```

 4 - Mettez à jour votre base de données

>**NOTE :** Cet exemple est pour un usage sous Debian

 ```
 cd ../src/gestion_entreprise/
 python manage.py migrate
 ```

# Lancement de votre application

 1 - Lancer votre serveur
 
>**NOTE :** Cet exemple est pour un usage sous Debian
 
```
cd ../plateforme-de-vote-budgetaire/plateforme_budgetaire/
python manage.py runserver
```

 2 - Rendez-vous à l'addresse `127.0.0.1:8000`, ou `localhost:8000` avec votre navigateur
