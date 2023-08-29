import sqlite3

DATABASE = 'marklin.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute('CREATE TABLE IF NOT EXISTS trains (type, name, length, picture)')
    con.close()