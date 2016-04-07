import requests

user_info = {'username': 'abc222', 'password': 'def'}
r = requests.post("http://162.243.203.93:5000/login", data=user_info)
print r.text
