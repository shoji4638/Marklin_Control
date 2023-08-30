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

@app.route('/database', methods=['GET', 'POST'])
def database():

#    print(request.form['mothods'])

    if request.method == 'GET':

        trains = select_trains('id')
#        con = sqlite3.connect(DATABASE)
#        db_trains = con.execute('SELECT * FROM trains').fetchall()
#        con.close()

 #       trains = []
 #       for i,row in enumerate(db_trains):
 #           trains.append({
 #               'id': row[0],
 #               'type': row[1],
 #               'name': row[2],
 #               'length': row[3],
 #               'picture': row[4],
 #               'num': i})
            
        input_train = {
            'id': '',
            'type': '',
            'name': '',
            'length': '',
            'picture': ''
        }

        return render_template(
            'database.html',
            trains=trains,input_train=input_train
        )
    
    else:
        return 'A>ABC</A'

@app.route('/<string:ClearId>/clear', methods=['POST'])
def clear_id(ClearId):

    print("ClearID:",ClearId)
    con = sqlite3.connect(DATABASE)
    db_trains = con.execute("delete from trains where id = '{}'".format(ClearId))
#    print(db_trains)
    con.commit()
    con.close()
    return redirect(url_for('database'))

@app.route('/<string:ChangeId>/change', methods=['POST'])
def change_data(ChangeId):

    print("ChangeID:",ChangeId)

    trains = select_trains('id')

#    db_trains = con.execute('SELECT * FROM trains ORDER BY id').fetchall()
#    trains = []
#    for i,row in enumerate(db_trains):
#        trains.append({
#            'id': row[0],
#            'type': row[1],
#            'name': row[2],
#            'length': row[3],
#            'picture': row[4],
#           'num': i})


    con = sqlite3.connect(DATABASE)
    db_trains = con.execute("SELECT * FROM trains WHERE id = '{}'".format(ChangeId)).fetchall()        
    input_train = {
        'id': db_trains[0][0],
        'type': db_trains[0][1],
        'name': db_trains[0][2],
        'length': db_trains[0][3],
        'picture': db_trains[0][4]
    }

    con.close()

    return render_template(
        '/database.html',
        trains=trains,input_train=input_train
    )


@app.route('/<string:sort_order>/sort', methods=['POST'])
def sort_order(sort_order):
    print(sort_order)

    return render_template(
        '/database.html',
        trains=trains,input_train=input_train
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
#        con.execute('INSERT INTO trains VALUES(?, ?, ?, ?, ?)',
#                [id, type, name, length, picture])
#        con.execute("delete from trains where id = '{}'".format(id))
#        con.execute('REPLACE INTO trains VALUES(?, ?, ?, ?, ?)',
#                [id, type, name, length, picture])
        con.execute('REPLACE INTO trains (id,type,name,length,picture) VALUES(?, ?, ?, ?, ?)',
                    [id, type, name, length, picture])
        con.commit()
        con.close()
        msg_error = '正常に更新しました'
    else:
        msg_error = 'TagIDフォーマットに異常があります！？'
        print(msg_error)

    trains = select_trains('id')

#    con = sqlite3.connect(DATABASE)
#    db_trains = con.execute('SELECT * FROM trains ORDER BY id').fetchall()
#    con.close()
#
#    trains = []
#    for i,row in enumerate(db_trains):
#        trains.append({
#            'id': row[0],
#            'type': row[1],
#            'name': row[2],
#            'length': row[3],
#            'picture': row[4],
#            'num': i})
        
    input_train = {
        'id': '',
        'type': '',
        'name': '',
        'length': '',
        'picture': ''
    }

#    return redirect(url_for('database'))
    return render_template(
        '/database.html',
        trains=trains,input_train=input_train,msg_error=msg_error
    )

def select_trains(sort_order):
    
    print(sort_order)
    con = sqlite3.connect(DATABASE)
    db_trains = con.execute('SELECT * FROM trains ORDER BY {}'.format(sort_order)).fetchall()
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

    return trains