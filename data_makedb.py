import mysql.connector

# 今回はrootユーザーでログインする。
conn = mysql.connector.connect(host='192.168.50.7',
                                user='root',
                                password='Shinomiya4638!',
                                )
curs = conn.cursor()

curs.execute('CREATE DATABASE my_database')

curs.close()

conn.close()