from test_alchemy import *
#search related

def search_item(keyword,storeid,order='item_id',offset=0):
    item_list = Item.query.filter_by(item_name.like('keyword'),store_id = storeid).order(order).limit(10).offset(offeset)
    result_list = item_schema.dump(item_list)
    return jsonify(result_list.data)
