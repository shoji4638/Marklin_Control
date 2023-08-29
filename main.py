from Marklin_Control import app
from flask import render_template, request, redirect,url_for
import sqlite3
import re
DATABASE = 'marklin.db'

#@app.route('/')
#def index():
#
#    return render_template(
#        'index.html'
#    )

@app.route('/')
def index():

    return render_template(
        'index.html'
    )


@app.route('/posttest',methods = ['POST'])
def posttest():

    try:
        print(request.form['action'],request.form['action'][4:])
        con = sqlite3.connect(DATABASE)
        db_trains = con.execute("delete from trains where id = '{}'".format(request.form['action'][4:]))
        print(db_trains)
        con.commit()
        con.close()
        return redirect(url_for('database'))

    except:
        print(request.form['change'])
        
        return redirect(url_for('database', methods = 'ABC'))

#    print(request.form['change'])
#    return redirect(url_for('index'))

@app.route('/database')
def database():

#    print(request.form['mothods'])

    con = sqlite3.connect(DATABASE)
    db_trains = con.execute('SELECT * FROM trains').fetchall()
    con.close()

    trains = []
    for i,row in enumerate(db_trains):
        trains.append({
            'id': row[0],
            'type': row[1],
            'name': row[2],
            'length': row[3],
            'picture': row[4],
            'num': i})

    return render_template(
        'database.html',
        trains=trains
    )

@app.route('/registar', methods=['POST'])
def register():
    id = request.form['id']
    type = request.form['type']
    name = request.form['name']
    length = request.form['length']
    picture = request.form['picture']

    p = re.compile('[0-9a-zA-Z]+')
    print(p.fullmatch(id).group())
    if len(p.fullmatch(id).group()) == 10:
        print('Length Match!!!!')

        con = sqlite3.connect(DATABASE)
        con.execute('INSERT INTO trains VALUES(?, ?, ?, ?, ?)',
                [id, type, name, length, picture])
        con.commit()
        con.close()
    else:
        print('入力エラー')

    return redirect(url_for('database'))