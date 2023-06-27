# LITReview
Une application permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.
## Objectifs:

- Un utilisateur peut demander une critique d'un livre ou d'un article particulier.
- Un utilisateur peut poster un avis sur un ticket.

## Fonctionnalités :
1. Inscrivez-vous - créez un compte
2. Connexion - Connexion utilisateur
3. Flux - La page principale de l'application où :
- Ils peuvent voir les tickets et les avis de tous les utilisateurs qu'ils suivent
- Ils doivent également voir leurs propres tickets et avis, ainsi que tous les avis en réponse à leurs propres tickets
- Ils peuvent poster leur ticket demandant une critique pour un livre ou un article de littérature
- Les utilisateurs qui les suivent peuvent ensuite déposer leurs avis en réponse au ticket.
- Les utilisateurs doivent également pouvoir publier des critiques de livres et d'articles qui n'ont pas encore de ticket.
4. Affiche la page où :
- L'utilisateur peut voir ses propres billets et avis séparément
- L'utilisateur peut modifier et supprimer ses propres tickets et avis
5. Suivez la page où :
- Les utilisateurs pourront suivre d'autres utilisateurs et devraient également avoir la possibilité de ne plus les suivre
- Les utilisateurs pourront voir qui les suit
6. Déconnectez-vous


## Commencer:
**Remarque** : Assurez-vous d'avoir python (au moins la version 3.8), l'environnement virtuel et git sur votre machine :
- `python -V` : commande pour vérifier la version python si elle est installée
- vérifiez que vous avez le module venv : `python -m venv --help` sinon veuillez vérifier https://www.python.org/downloads/. Vous pouvez également utiliser n'importe quel autre environnement virtuel pour exécuter le programme (** si vous avez choisi d'utiliser un autre environnement virtuel, les commandes suivantes ne conviennent pas pour exécuter le programme **)
- `git --version` : pour vérifier votre version de git si elle est installée ou vous pouvez la télécharger sur https://git-scm.com/downloads
 1. Cloner le dépôt sur le terminal ou l'invite de commande : `git clone https://github.com/Olivier91972/Django-web_app`
 2. Créer un environnement virtuel avec "venv"
- `cd Django-web_app` : pour accéder au dossier
- python -m venv ***nom de l'environnement*** : pour créer l'environnement virtuel - exemple : `python -m venv env`
3. Activez l'environnement virtuel :
pour unix ou macos :
- source ***nom d'environnement***/bin/activate - ex : `source env/bin/activate` si "env" est utilisé comme nom d'environnement
Pour les fenêtres:
- ***nom de l'environnement***\Scripts\activate.bat - ex : `env\Scripts\activate.bat`
4. Installez les packages avec pip : `pip install -r requirements.txt`
5. Migrez les tables vers la base de données :
- pour unix ou macos : `python3 manage.py migrate`
- pour Windows : `py manage.py migrate`
6. Lancez le programme :
- pour unix ou macos : `python3 manage.py runserver`
- pour Windows : `py manage.py runserver`
***Remarque*** : Le port par défaut s'ouvrira à 8000, si vous l'utilisez déjà utilisez un autre port comme 9000 `python3 manage.py runserver 9000` pour mac comme exemple
