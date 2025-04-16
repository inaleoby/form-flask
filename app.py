from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration pour la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la base de données
db = SQLAlchemy(app)

# Définir le modèle pour la base de données
class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Route pour afficher le formulaire
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Créer un objet Info
        new_info = Info(name=name, email=email)

        # Ajouter l'objet à la base de données
        db.session.add(new_info)
        db.session.commit()

        return redirect(url_for('form'))

    return render_template('form.html')

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)

