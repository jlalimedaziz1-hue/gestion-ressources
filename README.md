# Gestion des ressources

## Description

Application web développée avec Django permettant de gérer des ressources pédagogiques.

## Fonctionnalités

- Gestion des catégories.
- Affichage des ressources.
- Consultation des détails d'une ressource.
- Ajout d'une ressource.
- Modification d'une ressource.
- Suppression d'une ressource.
- Filtrage des ressources par catégorie.

## Technologies utilisées

- Python
- Django
- SQLite
- HTML
- CSS

## Installation

1. Cloner ou télécharger le projet.
2. Créer un environnement virtuel :

```bash
python -m venv venv
```

3. Activer l'environnement virtuel sous Windows :

```powershell
venv\Scripts\activate
```

4. Installer les dépendances :

```bash
pip install -r requirements.txt
```

5. Appliquer les migrations :

```bash
python manage.py migrate
```

6. Créer un superutilisateur :

```bash
python manage.py createsuperuser
```

7. Lancer le serveur :

```bash
python manage.py runserver
```

## Accès

- Site web : http://127.0.0.1:8000/
- Administration : http://127.0.0.1:8000/admin/

## Tests

Pour tester l'application :

```bash
python manage.py test
```

Les fonctionnalités à tester sont l'affichage, l'ajout, la modification, la suppression et le filtrage des ressources par catégorie.
