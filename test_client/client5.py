#client5
import requests

user_info = {'username': 'abc@abc.com', 'password': 'defdefdef'}
r = requests.post("http://localhost:5000/register", data=user_info)
print r.text
