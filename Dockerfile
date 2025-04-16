# Utiliser une image légère de Python
FROM python:3.11-alpine  

# Définir le répertoire de travail
WORKDIR /app

RUN apk add --no-cache postgresql-dev gcc musl-dev

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip3 install --no-cache-dir -r requirements.txt  

# Copier tout le code source
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000  

# Définir la commande de demarrage 
CMD ["python", "app.py"]
