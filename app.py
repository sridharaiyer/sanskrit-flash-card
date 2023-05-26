import json
import sqlite3

from flask import Flask, render_template, jsonify, g

app = Flask(__name__)

DATABASE = 'sanskrit-english-dictionary.db'


# Connect to the SQLite database with UTF-8 encoding
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.text_factory = str
        db.execute('PRAGMA encoding = "UTF-8"')
    return db


# Close the database connection after the request is finished
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


with open('words.json', 'r') as file:
    words = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


# Generate random entry route
@app.route('/generate')
def generate():
    # Fetch a random entry from the dictEntries table
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT word, desc FROM dictEntries ORDER BY RANDOM() LIMIT 1")
    entry = cursor.fetchone()
    cursor.close()

    # Create a JSON response with UTF-8 encoding
    response = {
        'word': entry[0],
        'desc': entry[1]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
