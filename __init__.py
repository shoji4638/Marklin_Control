from flask import Flask
#app = Flask(__name__)
app = Flask(__name__, static_folder="./static/")

import Marklin_Control.main      #Flaskを動かすデレクトリ名

from Marklin_Control import db
db.create_books_table()             #立上時にデータベースなかったら作成⇒db.pyを実行