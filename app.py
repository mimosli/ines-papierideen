from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)


# Serve images directly from the images/ folder
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)


# ===== MAIN PAGES =====

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/glueckwunschkarten')
def glueckwunschkarten():
    return render_template('glueckwunschkarten.html')


@app.route('/einladungskarten')
def einladungskarten():
    return render_template('einladungskarten.html')


@app.route('/geldgeschenke')
def geldgeschenke():
    return render_template('geldgeschenke.html')


@app.route('/dekoratives')
def dekoratives():
    return render_template('dekoratives.html')


@app.route('/textiles')
def textiles():
    return render_template('textiles.html')


# ===== CONTACT FORM =====

@app.route('/kontakt', methods=['POST'])
def kontakt():
    name    = request.form.get('name', '')
    email   = request.form.get('email', '')
    message = request.form.get('message', '')
    # TODO: send e-mail or save to database
    print(f"Neue Nachricht von {name} <{email}>:\n{message}")
    return redirect(url_for('home') + '#kontakt')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
