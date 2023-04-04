# WePynaire sur les permission au sein d'un projet Django

Pour lancer ce serveur de développement du code de cet atelier, il vous faut
tout d'abord installer pipenv sur votre système à l'aide de `pip install pipenv`
ou mieux, si vous être utilisateur de pipx `pipx install pipenv`.

Ensuite, il vous suffit de suivre la procédure suivante:

1. Cloner le code de ce dépôt à l'aide de git ou le télécharger sous forme d'archive zip
2. Ouvrez un terminal à la racine du projet
3. Renommer le fichier .env-exemple en .env et remplacer la valeur de la variable SECRET_KEY
4. Créer un répertoire vide nommé .venv à la racine du projet
5. Installer les dépendances avec la commande `pipenv install --dev`
6. Exécuter les migrations avec `pipenv run python manage.py migrate`
7. Créez un superutilisateur avec `pipenv run python manage.py createsuperuser` et suivez les instructions
8. Charger les données de départ avec `pipenv run python manage.py loaddata data`
9. Lancer le serveur de développement avec `pipenv run python manage.py runserver`

Si vous désirez expérimenter avec le notebook Jupyter nommé **laboratoire.ipynb**, il suffit de lancer le
shell avec la commande `pipenv run python manage.py shell_plus --notebook`. Votre navigateur web va
directement ouvrir une page d'exploration dans laquelle vous pourrez consulter ce fichier.