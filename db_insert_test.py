from db_make_table import *
from db_setting import session

trains_db = Trains_db()
trains_db.id = '1234567989A'
trains_db.type = '貨車'
trains_db.name = 'DB103'
trains_db.length = 230
trains_db.picture = '5.jpg'
session.add(train_t)
session.commit()