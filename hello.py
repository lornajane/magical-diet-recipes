import os
import psycopg2

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# pg_uri = os.environ.get('PG_URI')
# db_conn = psycopg2.connect(pg_uri)


@app.route('/')
def hello_world():
    pg_uri = os.environ.get('PG_URI')
    print(os.environ)
    if pg_uri:
        print(pg_uri + '\n')

        db_conn = psycopg2.connect(pg_uri)
        cursor = db_conn.cursor()

        cursor.execute("SELECT current_database()")
        result = cursor.fetchone()
        print("Successfully connected to: {}".format(result[0]) + '\n')

    return 'Hello, World!'


@app.route('/temp')
def templated():
    # invent nonsense influencer words to go with the "meals"
    tagline = []
    tagline.append("")
    tagline.append("Perfect choice for those cold winter evenings")
    tagline.append("Bring a touch of nostalgia to the table tonight")
    tagline.append("A little piece of luxury - you're worth it!")
    tagline.append("Keep perspective with a little moment of joy")
    tagline.append("Bubbles of excitement to brigten and lift you")
    tagline.append("A healthy dose of something special works wonders")
    tagline.append("Seeing the situation from both sides is a true gift")
    tagline.append("Making time for reflection is part of the battle")
    tagline.append("Mealtimes give us chance to smile, and briefly pause")
    tagline.append("Bringing options for dreamers, poets and dancers")

    return render_template('index.html', tagline=tagline)


@app.route('/rating', methods=['POST'])
def posted():
    print("Data received")
    data = request.form
    print(data)

    # put this into the table

    return "OK"
