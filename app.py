from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

DATABASE = 'community_pantry'

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

@app.route('/add', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        food_name = request.form['food_name']
        quantity = request.form['quantity']
        description = request.form['description']
        pickup_address = request.form['pickup_address']
        contact_number = request.form['contact_number']
  
        # Insert the data into the database
        db = get_db()
        db.execute('INSERT INTO Pantry (FoodName, Quantity, Description, PickupAddress, ContactNumber) VALUES (?, ?, ?, ?, ?)', (food_name, quantity, description, pickup_address, contact_number))
        db.commit()
        db.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_food.html')

@app.route('/availableFood')
def available_food():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sqlite_select_query = """SELECT * from Pantry"""
    cursor.execute(sqlite_select_query)
    food_items = cursor.fetchall()
    
    return render_template('available_food.html',food_items=food_items)

if __name__ == '__main__':
    app.run(debug=True)