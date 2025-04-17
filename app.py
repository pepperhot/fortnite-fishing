from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    data = request.get_json()
    print("Données reçues :", data)

    with open("data.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"message": "Données enregistrées"}), 200

if __name__ == '__main__':
    app.run()
