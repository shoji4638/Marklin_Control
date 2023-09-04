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

@app.route('/itemview', methods=['GET', 'POST'])
def itemview():
#    print(request.form['mothods'])
    if request.method == 'GET':

        #Items_T = [{'id':'123', 'prooduct_no':'ABC', 'name':'DEF', 'picture':'GHI'}]
        Items_T = select_Items_T('id')
        list_len = len(Items_T)

        return render_template(
            'itemview.html',
            list_len=list_len,Items_T=Items_T
        )
    
    else:
        return 'A>/ItemView [POST]</A'

@app.route('/itemregist', methods=['GET', 'POST'])
def itemregist():
#    print(request.form['mothods'])
    if request.method == 'GET':

        Items_T = select_Items_T('id')
        list_len = len(Items_T)

        return render_template(
            'itemregist.html',
            list_len=list_len,Items_T=Items_T
        )
    
    else:
        
        id = request.form['id']
        product_no = request.form['product_no']
        name = request.form['name']
        picture = request.form['picture']

        input_train = {
            'id': id,
            'product_no': product_no,
            'name': name,
            'picture': picture
        }

        if (id != ''): #入力確認 英数字10文字
            print('New Data')

            con = sqlite3.connect(DATABASE)
            con.execute('REPLACE INTO Item_T (id,product_no,name,picture) VALUES(?, ?, ?, ?)',
                        [id, product_no, name, picture])
            con.commit()
            con.close()
            msg_error = '正常に更新しました'
        else:
            msg_error = 'TagIDフォーマットに異常があります!?'

#    Items_T = [{'id':'9999', 'prooduct_no':'9999', 'name':'9999', 'picture':'999'}]
    Items_T = select_Items_T('id')

    return render_template(
        '/itemview.html',
        Items_T=Items_T
    )
    return 'A>/ItemRegist [POST]</A'

@app.route('/database', methods=['GET', 'POST'])
def database():
#    print(request.form['mothods'])
    if request.method == 'GET':

        trains = select_trains('id')
            
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
    """TagID情報の変更をPOST受信の処理
    Args:
        ChangeId (10Byte:[0-9a-fA-Fx]): _description_
    Returns:
        render_template(
        '/database.html',
        trains=trains,input_train=input_train)
    """
    Request_msg = request.form['action']

    print("ChangeID:",ChangeId," action:",Request_msg)


    trains = select_trains('id')

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

    if sort_order == 'id_up':
        trains = select_trains('id')
    elif sort_order == 'id_down':
        trains = select_trains('id DESC')
    elif sort_order == 'type_up':
        trains = select_trains('type')
    elif sort_order == 'type_down':
        trains = select_trains('type DESC')
    elif sort_order == 'name_up':
        trains = select_trains('name')
    elif sort_order == 'name_down':
        trains = select_trains('name DESC')
    elif sort_order == 'length_up':
        trains = select_trains('length')
    elif sort_order == 'length_down':
        trains = select_trains('length DESC')
    else:
        trains = select_trains('id')

    input_train = {
        'id': '',
        'type': '',
        'name': '',
        'length': '',
        'picture': ''
    }

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

    input_train = {
        'id': id,
        'type': type,
        'name': name,
        'length':length,
        'picture': picture
    }

    if (result := re.compile('[0-9A-Fa-f]{10}').fullmatch(id)): #入力確認 英数字10文字
        print('Length Match!!!!:',result.group(0))

        con = sqlite3.connect(DATABASE)
        con.execute('REPLACE INTO trains (id,type,name,length,picture) VALUES(?, ?, ?, ?, ?)',
                    [id, type, name, length, picture])
        con.commit()
        con.close()
        msg_error = '正常に更新しました'
    else:
        msg_error = 'TagIDフォーマットに異常があります！？'
#        print(msg_error)

    trains = select_trains('id')

#    return redirect(url_for('database'))
    return render_template(
        '/database.html',
        trains=trains,input_train=input_train,msg_error=msg_error
    )

def select_trains(sort_order):

    print(sort_order)
    con = sqlite3.connect(DATABASE)
    db_trains = con.execute("SELECT * FROM trains ORDER BY {}".format(sort_order)).fetchall()
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
    print(trains)

    return trains

def select_Items_T(sort_order):

    print(sort_order)
    con = sqlite3.connect(DATABASE)
    db_Items_T = con.execute("SELECT * FROM Item_T ORDER BY {}".format(sort_order)).fetchall()
    con.close()

    Items_T = []
    for i,row in enumerate(db_Items_T):
        Items_T.append({
            'id': row[0],
            'product_no': row[1],
            'name': row[2],
            'picture': row[3],
            'num': i})
    #print(Items_T)

    return Items_T