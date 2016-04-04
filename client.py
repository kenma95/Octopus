import requests

user_info = {'username': 'abc222', 'password': 'def'}
r = requests.post("http://127.0.0.1:5000/login", data=user_info)
print r.text
