# Utiliser une image Python 3
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans l'image
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter l'application
CMD ["python", "app.py"]
