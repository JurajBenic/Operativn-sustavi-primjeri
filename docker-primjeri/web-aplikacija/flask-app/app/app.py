import os
import logging
from psycopg_pool import ConnectionPool
from flask import Flask, render_template, jsonify, request, redirect, url_for

DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
DB_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
DB_PORT = os.getenv('POSTGRES_PORT', '5433')
DB_NAME = os.getenv('POSTGRES_DB', 'operacijski-sustavi')


logging.basicConfig(level=logging.INFO)


db = ConnectionPool(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    min_size=1,
    max_size=10
)


with db.connection() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS studenti (
            id SERIAL PRIMARY KEY,
            ime TEXT NOT NULL,
            prezime TEXT NOT NULL,
            godina_rodenja INTEGER NOT NULL,
            jmbag TEXT NOT NULL,
            email TEXT
        );
    """)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/studenti')
def studenti():
    with db.connection() as conn:
        result = conn.execute("SELECT * FROM studenti;")
        studenti = result.fetchall()
        print("*" * 20)
        print(f"Fetched students: {studenti}")
    return render_template('studenti.html', studenti=studenti)


@app.route('/studenti/add', methods=['GET', 'POST'])
def dodaj_studenta():
    if request.method == 'POST':
        ime = request.form.get('ime')
        prezime = request.form.get('prezime')
        jmbg = request.form.get('jmbag')
        email = request.form.get('email')
        godina_rodenja = request.form.get('godina_rodenja')

        if not all([ime, prezime, jmbg, godina_rodenja]):
            return render_template('studenti_add.html', error='Ime, prezime, JMBAG i godina rodenja su obavezni!'), 400

        with db.connection() as conn:
            conn.execute(
                "INSERT INTO studenti (ime, prezime, jmbag, email, godina_rodenja) VALUES (%s, %s, %s, %s, %s);",
                (ime, prezime, jmbg, email, godina_rodenja)
            )
            conn.commit()

        return redirect(url_for('studenti'))

    return render_template('studenti_add.html')


if __name__ == '__main__':
    # Use gevent WSGI server for better performance
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('0.0.0.0', 5000), app, log=None)
    http_server.serve_forever()
    
    # Uncomment the line below to run the Flask app directly
    # app.run(debug=True, host='0.0.0.0', port=5001)



