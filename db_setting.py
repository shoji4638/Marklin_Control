from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

dialect = "mariadb"
driver = "pymysql"
username = "root"
password = "Shinomiya4638!"
host = "192.168.50.7"
port = "3306"
database = "ShojiHomeDB"
charset_type = "utf8mb4"
db_url = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type}"
##mariadb+pymysql://root:Shinomiya4638!@192.168.50.7/ShojiHomeDB?charset=utf8mb4
#db_url = f"sqlite:///C:/Users/s_shi/Documents/git/Marklin_Control/marklin.db"

# DB接続するためのEngineインスタンス
ENGINE = create_engine(db_url, echo=True)

# DBに対してORM操作するときに利用
# Sessionを通じて操作を行う
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

# 各modelで利用
# classとDBをMapping
Base = declarative_base()