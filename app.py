from flask import Flask, render_template, request, redirect, url_for
#import sqlite3

app = Flask(__name__)

DATABASE = 'food_rescue.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('index.html')
