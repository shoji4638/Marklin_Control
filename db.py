import sqlite3

DATABASE = 'marklin.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute('CREATE TABLE IF NOT EXISTS trains (id PRIMARY KEY, type text, name text, length integer, picture text)')
    con.close()

    con = sqlite3.connect(DATABASE)
#    con.execute('DROP TABLE Item_T')
    con.execute('CREATE TABLE IF NOT EXISTS Item_T (id PRIMARY KEY, product_no text, name text, picture text)')
    con.close()