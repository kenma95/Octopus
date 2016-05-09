from db_schema import *

from random import choice
from string import ascii_uppercase

def add_item_db(store_id,item_name,item_price,item_desc,filename):
    item_id = (''.join(choice(ascii_uppercase) for i in range(30)))
    item = Item(item_id,\
		 store_id,item_name,item_price,item_desc,filename)
    item.locx = 0
    item.locy = 0  
    db.session.add(item)
    db.session.commit()
def get_store_by_user(user_id):
    store = User_Store.query.filter_by(userid = user_id).first()
    return store.get_store_id()

def add_failed():
    return "add failed"
def check_valid_add(itemname,storeid):
    item = Item.query.filter_by(store_id = storeid,item_name=itemname).first()
    return item is None
