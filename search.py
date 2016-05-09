import db_schema
from db_schema import Item
from flask import jsonify



def search_item(keyword,storeid,order='item_id',offset=0):
    item_list = Item.query.filter_by(store_id = storeid).filter(Item.item_name.like('%'+keyword+'%')).\
		order_by(order).limit(20).offset(offset).all()
    print item_list
    temp=[]
    for item in item_list:
        temp.append(item.to_json1())
    print temp
    return jsonify(json_list=temp)


def get_item(itemid,storeid):
    target_item = Item.query.filter_by(item_id = itemid\
,store_id =storeid).first()
    if target_item is None:
	target_item = find_none()
    temp = target_item.to_json2()
    return jsonify(target_item=temp)

def find_none():
    return {'item_id' : ''
            ,'item_name' : ''
            ,'store_id': ''
            ,'price' : 0
            ,'description' : ''
            ,'photo' : ''
            ,'remain' : 0
            }


def get_loc(itemid,storeid):
    target_item = Item.query.filter_by(item_id = itemid\
,store_id =storeid).first()
    temp =target_item.to_json3()
    return jsonify(target_item=temp)
