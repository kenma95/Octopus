class ItemSchema(ma.Schema):
	class Metat:
		#Fields to expose
		fields = ('item_id','item_name','price','address')
item_schema = ItemSchema()
item_schema = ItemSchema(many=True)
