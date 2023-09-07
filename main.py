#from Marklin_Control import app
from flask import Flask,render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from db_make_table import *
from db_setting import session

#import sqlite3
import re
import os

DATABASE = 'marklin.db'

main = Flask(__name__)
#engine = create_engine("mariadb+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
#main.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///marklin.db'
#engine = create_engine("sqlite:///foo.db") # 相対パスの指定の場合
#engine = create_engine("sqlite:////absolute/path/to/foo.db") # 絶対パスの指定の場合
#main.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////C:\Users\s_shi\Documents\git\Marklin_Control\marklin.db'
#main.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////C:/Users/s_shi/Documents/git/Marklin_Control/marklin.db'
main.config['SQLALCHEMY_DATABASE_URI']= 'mariadb+pymysql://root:Shinomiya4638!@192.168.50.7/ShojiHomeDB?charset=utf8mb4'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
main.config['SQLALCHEMY_ECHO']=True

# @main.before_request
# def init():
#     db.create_all()

@main.route('/')
def index():

    return render_template(
        'index.html'
    )

@main.route('/<string:ChangeId>/ProductChange', methods=['POST'])
def ProductChange_data(ChangeId):

#    Request_msg = request.form['action']
#    print("ChangeID:",ChangeId," action:",Request_msg)

    trains = select_Product_trains('id')
    input_train = {}

    # con = sqlite3.connect(DATABASE)
    # db_trains = con.execute("SELECT * FROM trains WHERE id = '{}'".format(ChangeId)).fetchall()        
    # input_train = {
    #     'id': db_trains[0][0],
    #     'type': db_trains[0][1],
    #     'name': db_trains[0][2],
    #     'length': db_trains[0][3],
    #     'picture': db_trains[0][4]
    # }

    # con.close()

    return render_template(
        '/itemview.html',
        trains=trains,input_train=input_train
    )

@main.route('/product_register', methods=['GET', 'POST'])
def product_register():

    if request.method == 'POST':
        id = request.form['id']
        ProductNo = request.form['ProductNo']
        type = request.form['type']
        name = request.form['name']
        length = request.form['length']
        picture = request.form['picture']

        input_product = {
            'id': id,
            'ProductNo': ProductNo,
            'type': type,
            'name': name,
            'length':length,
            'picture': picture
        }
    
        trains_db = Trains_db()
        trains_db.id = id
        trains_db.product_no = ProductNo
        trains_db.type = type
        trains_db.name = name
        trains_db.length = length
        trains_db.picture = picture
        session.add(trains_db)
        session.commit()
        msg_error = '正常に更新しました'
    else:
        msg_error = 'TagIDフォーマットに異常があります！？'
#        print(msg_error)

    Items_T = select_Product_trains('id')
    print(Items_T)

#    return redirect(url_for('database'))
    return render_template(
        '/productview.html',
         Items_T= Items_T, input_product= {}, msg_error= msg_error
    )


@main.route('/productdata', methods=['GET', 'POST'])
def productdata():
#    print(request.form['mothods'])
    if request.method == 'GET':

        #Items_T = [{'id':'123', 'prooduct_no':'ABC', 'name':'DEF', 'picture':'GHI'}]
        Items_T = select_trains_T('id DESC')
        list_len = len(Items_T)

        input_product = {
            'id':'0',
            'product_no':'1234',
            'type':'機関車'
        }

        return render_template(
            'productview.html',
            list_len=list_len,Items_T=Items_T[4400:4550],input_product=input_product
        )
    
    else:
        return 'A>/ItemView [POST]</A'

@main.route('/itemregist', methods=['GET', 'POST'])
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

@main.route('/database', methods=['GET', 'POST'])
def database():
#    print(request.form['mothods'])
    if request.method == 'GET':
        trains = select_trains('id')
        input_trains = session.query(Trains_db). \
            filter(Trains_db.id == "000220"). \
            all()
        #print(type(input_trains[0].id),input_trains[0].id)

        if input_trains != []:

            input_train = {
                'Trainsid': input_trains[0].id,
                'product_no': input_trains[0].product_no,
                'type': input_trains[0].type,
                'name': input_trains[0].name,
                'length': input_trains[0].length,
                'picture': input_trains[0].picture
            }
        
        else:
            input_train = {
                'Trainsid': '',
                'product_no': '',
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

@main.route('/trainserch', methods=['GET', 'post'])
def tarainserch():

#    if request.method == 'POST':
    Tagid = '{:0>10}'.format(request.form['Tagid'])
    # print(type(request.form['Tagid']))
    # if request.form['Tagid'].hexdigits == True:
    #     Tagid = '{:06x}'.format(hex(request.form['Tagid']))
    # else:
    #     Tagid = ''
    if 0 < int(Tagid, 16) and 0xFFFFFFFFFF >= int(Tagid, 16):
        pass
    Trainid = '{:0>6}'.format(request.form['Trainid'])

    if 0 < int(Trainid) and 100000 >= int(Trainid):
        search_word = 'id = ' + str(int(Trainid))
    else:
        search_word = 'id'
    print(search_word)
    #product_no = request.form['Productno']
#    print('Serch Word: ',Tagid,' :',Trainid,' :',product_no)

    trains = search_trains(serch_word)

    input_trains = session.query(Trains_db). \
        filter(Trains_db.id == Trainid). \
        all()
    
    if input_trains != []:
        print(type(input_trains[0].id),input_trains[0].id)
        input_train = {
            'Trainsid': input_trains[0].id,
            'product_no': input_trains[0].product_no,
            'type': input_trains[0].type,
            'name': input_trains[0].name,
            'length': input_trains[0].length,
            'picture': input_trains[0].picture
        }
    else:
        input_train = {
            'Trainsid': '??????',
            'product_no': '??????',
            'type': '',
            'name': '??????',
            'length': '??????',
            'picture': '??????'
        }


    return render_template(
        'database.html',
        trains=trains,input_train=input_train
    )

@main.route('/<string:ClearId>/clear', methods=['POST'])
def clear_id(ClearId):

    print("ClearID:",ClearId)
#    con = sqlite3.connect(DATABASE)
#    db_trains = con.execute("delete from trains where id = '{}'".format(ClearId))
##    print(db_trains)
#    con.commit()
#    con.close()
    session.query(Trains_db). \
        filter(Trains_db.id == ClearId).delete()
    session.commit()

    return redirect(url_for('database'))

@main.route('/<string:ChangeId>/change', methods=['POST'])
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

@main.route('/<string:sort_order>/sort', methods=['POST'])
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

@main.route('/registar', methods=['POST'])
def register():
    try:
        Tagid = request.form['Tagid']
        Trainid = request.form['Trainid']
        product_no = request.form['Productno']
        type = request.form['type']
        name = request.form['name']
        length = request.form['length']
        picture = request.form['picture']
    except:
        Tagid = request.form['Tagid']
        Trainid = request.form['Trainid']
        product_no = request.form['Productno']
        type = ''
        name = request.form['name']
        length = request.form['length']
        picture = request.form['picture']

    input_train = {
        'Tagid': Tagid,
        'Trainid': Trainid,
        'product_no': product_no,
        'type': type,
        'name': name,
        'length':length,
        'picture': picture
    }

    print('input_train',input_train)


    if (result := re.compile('[0-9A-Fa-f]{10}').fullmatch(Tagid)): #入力確認 英数字10文字
        print('Length Match!!!!:',result.group(0))

        item_db = Item_db()
        item_db.Tagid = Tagid
        item_db.Trains_id = Trainid
        session.add(item_db)
        session.commit()
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

def search_trains(sort_order):

    datas = session.query(Trains_db).filter(Trains_db.id == '200').all()
#    datas = session.query(Item_db.Tagid,Item_db.Trains_id,Trains_db.product_no,Trains_db.name,Trains_db.picture). \
#        outerjoin(Trains_db, Item_db.Tagid==Trains_db.id). \
#        all()
#    print('datas:',type(datas),datas)
    trains_list = []
#    for i,row in enumerate(datas):
    for i,row in enumerate(datas):
#        print('i:',i,' row:',row)
        trains_list.append({    
            'id': row.id,    
            'product_no': row.product_no,  
            'name': row.name,
            'length': row.length,
            'picture': row.picture
            })
#           'length': row.length,
#            'picture': os.path.basename(row.picture),
#            'num': i})
    #print(trains_list)

    return trains_list


def select_Product_trains(sort_order):

    datas = session.query(Trains_db).all()
#    datas = session.query(Item_db.Tagid,Item_db.Trains_id,Trains_db.product_no,Trains_db.name,Trains_db.picture). \
#        outerjoin(Trains_db, Item_db.Tagid==Trains_db.id). \
#        all()
#    print('datas:',type(datas),datas)
    trains_list = []
#    for i,row in enumerate(datas):
    for i,row in enumerate(datas):
#        print('i:',i,' row:',row)
        trains_list.append({    \
            'id': row.id,    \
            'product_no': row.product_no,  \
            'name': row.name,
            'length': row.length,
            'picture': row.picture
            })
#           'length': row.length,
#            'picture': os.path.basename(row.picture),
#            'num': i})
    #print(trains_list)
    return trains_list


def select_trains(sort_order):

    print(sort_order)
#    datas = session.query(Item_db.Tagid, Item_db.Trains_id, Trains_db.type, Trains_db.name, Trains_db.length,  Trains_db.product_no, Trains_db.picture
#        ).join(Item_db, Trains_db.id == Item_db.Trains_id)
    datas = session.query(Item_db.Tagid, Item_db.Trains_id, Trains_db.type, Trains_db.name, Trains_db.length,  Trains_db.product_no, Trains_db.picture
        ).join(Item_db, Trains_db.id == Item_db.Trains_id)

    print('datas:',type(datas),datas)

    trains_list = []
#    for i,row in enumerate(datas):
    for i,row in enumerate(datas):
        print('datas[',i,']:',row)
        trains_list.append({
            'tagid': row[0],
            'trainid': row[1],
            'type': row[2],
            'name': row[3],
            'length': row[4],
            'product_no': row[5],
            'picture': row[6]})
#           'length': row.length,
#            'picture': os.path.basename(row.picture),
#            'num': i})
    #print(trains_list)

    return trains_list

def select_trains_T(sort_order):

    print('Select Trains Table')
    print(sort_order)
#    con = sqlite3.connect(DATABASE)
#    db_Items_T = con.execute("SELECT * FROM Item_T ORDER BY {}".format(sort_order)).fetchall()
#    con.close()
#    db_trains_T = session.query().order_by(Trains_db.id).all()
    db_trains_T = session.query(Trains_db).all()

    Items_T = []
    for i,row in enumerate(db_trains_T):
        Items_T.append({
            'id': row.id,
            'product_no': row.product_no,
            'name': row.name,
            'picture': row.picture,
            'num': i})
    #print(Items_T)

    return Items_T