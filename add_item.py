from db_schema import *
import uuid

def add_item_db(store_id,item_name,item_price,item_desc,filename):
    item_id = uuid.uuid1()
    item = Item(item_id,\
		 store_id,item_name,item_price,item_desc,filename)
    db.session.add(item)
    db.session.commit()
