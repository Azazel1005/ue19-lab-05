# UE19 Lab 05

Cette application interroge l'API JokesAPI pour afficher une blague aléatoire.

## Prérequis

- Python 3.8+
- Docker installé sur votre machine

## Installation et utilisation

1. Cloner ce repository :
   ```bash
   git clone https://github.com/votre-utilisateur/ue19-lab-05.git
   cd ue19-lab-05
   
2. Installer les dépendances:
   ```bash
   pip install -r requirements.txt
   
3. Lancer l'application:
   ```bash
   python app.py
   
4. Construire l'image Docker:
   ```bash
   docker build -t jokesapp .

5. Executer le conteneur Docker:
   ```bash
   docker run --rm jokesapp
