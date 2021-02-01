import logging
import os
import psycopg2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    pg_uri = os.environ.get('PG_URI')
    print(pg_uri + '\n')

    db_conn = psycopg2.connect(pg_uri)
    cursor = db_conn.cursor()

    cursor.execute("SELECT current_database()")
    result = cursor.fetchone()
    print("Successfully connected to: {}".format(result[0]) + '\n')


    return 'Hello, World!'
