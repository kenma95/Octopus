import db_schema
from db_schema import Store
from flask import jsonify
#search related Item



def get_all():
    store_list = Store.query.filter(Store.store_name is not None). all()
    temp=[]
    for item in store_list:
        temp.append(item.to_json1())
    print temp
    return jsonify(json_list=temp)
