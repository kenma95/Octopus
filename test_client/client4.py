#client4
import requests

user_info = {'username': 'abc222', 'password': 'defghijk'}
r = requests.post("http://localhost:5000/register", data=user_info)
print r.text
