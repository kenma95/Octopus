import requests

payload = {'keyword':'Xbox','store_id' : 's1'}
r = requests.get('http://localhost:5000/search',params=payload)
print r.text
