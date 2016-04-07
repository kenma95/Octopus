import requests

payload = {'keyword':'Xbox','store_id' : 's1'}
r = requests.get('http://162.243.203.93:5000/search',params=payload)
print r.text
