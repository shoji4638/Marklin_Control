from flask import Flask
app = Flask(__name__)
import Marklin_Control.main      #Flaskを動かすデレクトリ名

from Marklin_Control import db
db.create_books_table()