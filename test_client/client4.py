#client4
import requests

user_info = {'username': 'abc222', 'password': 'afjakfjdef'}
r = requests.post("http://localhost:5000/login", data=user_info)
print r.text
