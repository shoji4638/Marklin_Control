from Marklin_Control import app
from flask import render_template, request, redirect,url_for
import sqlite3
DATABASE = 'marklin.db'

@app.route('/')
def index():

    return render_template(
        'index.html'
    )

@app.route('/database')
def database():

    con = sqlite3.connect(DATABASE)
    db_trains = con.execute('SELECT * FROM trains').fetchall()
    con.close()

    trains = []
    for row in db_trains:
        trains.append({
            'type': row[0],
            'name': row[1],
            'length': row[2],
            'picture': row[3]})

    return render_template(
        'database.html',
        trains=trains
    )

@app.route('/registar', methods=['POST'])
def register():
    type = request.form['type']
    name = request.form['name']
    length = request.form['length']
    picture = request.form['picture']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO trains VALUES(?, ?, ?, ?)',
                [type, name, length, picture])
    con.commit()
    con.close()

    return redirect(url_for('database'))