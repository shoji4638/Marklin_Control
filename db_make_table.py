from sqlalchemy import Column, Integer, String, DateTime, Sequence
from db_setting import ENGINE, Base
from datetime import datetime
import sys

# class User(Base):
#     """
#     UserModel
#     """
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     email = Column(String(255))
#     age = Column(Integer)
#     created_at = Column('created', DateTime, default=datetime.now, nullable=False)
#     updated_at = Column('modified', DateTime, default=datetime.now, nullable=False)

class Trains_db(Base):
    #con.execute('CREATE TABLE IF NOT EXISTS trains (id PRIMARY KEY, type text, name text, length integer, picture text)')
#    __tablename__ = 'trains'
    __tablename__ = 'trains_T'
    id = Column(String(16), primary_key=True)
    product_no = Column(String(10))
    name = Column(String(128))
    maker_id = Column(Integer)
    type = Column(String(16))
    length = Column(Integer)
    picture = Column(String(64))

class Item_db(Base):

    __tablename__ = 'itemdb'
    Tagid = Column(String(16), primary_key=True)
    Trains_id = Column(String(16))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)