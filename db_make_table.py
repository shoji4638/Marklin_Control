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
    __tablename__ = 'trains_T'
    id = Column(String(16), primary_key=True)
    product_no = Column(String(10))
    name = Column(String(128))
    maker_id = Column(Integer)
    name_d = Column(String(128))
    detail = Column(String(256))
    type = Column(Integer)
    type2 = Column(Integer)
    type3 = Column(Integer)
    seihin_no = Column(String(128))
    scale_id = Column(Integer)
    length = Column(Integer)
    picture = Column(String(64))

class Item_db(Base):
    __tablename__ = 'itemdb'
    Tagid = Column(String(16), primary_key=True)
    Trains_id = Column(String(16))

class Maker_db(Base):
    __tablename__ = 'maker_T'
    id = Column(Integer, primary_key=True)
    maker_name = Column(String(45))
    maker_name_j = Column(String(45))

class Type_db(Base):
    __tablename__ = 'type_T'
    id = Column(Integer, primary_key=True)
    type1 = Column(String(45))
    type2 = Column(String(45))
    type3 = Column(String(45))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)