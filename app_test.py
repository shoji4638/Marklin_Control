#from Marklin_Control import app
from flask import Flask,render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#import sqlite3
#import re

#DATABASE = 'marklin.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///marklin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True

db = SQLAlchemy(app)

class Shohin(db.Model):
    __tablename__ = 'Shohin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)

@app.before_request
def init():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    datas = Shohin.query.all()
    return render_template('index.html', lists = datas)

@app.route('/result', methods=['POST'])
def insert():
    name_txt = request.form['name']
    price_txt = request.form['price']
    shohin = Shohin(name = name_txt, price = price_txt)

    db.session.add(shohin)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
