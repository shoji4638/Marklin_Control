import mysql.connector

# 今回はrootユーザーでログインする。
conn = mysql.connector.connect(host='192.168.50.7',
                                user='root',
                                password='Shinomiya4638!',
                                database='new_schema',
                                charset="utf8mb3")

curs = conn.cursor()
curs.execute("""CREATE TABLE users(
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(32) NOT NULL)""")
curs.close()

conn.close()