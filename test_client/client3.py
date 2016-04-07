import requests

payload = {'item_id':'i2','store_id' : 's1'}
r = requests.get('http://localhost:5000/get_item',params=payload)
print r.text
