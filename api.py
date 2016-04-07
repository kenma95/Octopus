from flask import Flask,request

import db_schema
import login
import search
import register
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'




@app.route('/register',methods =['POST'])
def register_router():
    error = None
    code,msg = register.valid_register(request.form['username'],\
        request.form['password'])

    if code == 0:
        register.add_user(request.form['username'],\
    	   request.form['password'])
        return 'register succeed'
    else:
        return msg


@app.route('/login', methods=['POST'])
def login_router():
    error = None
    if login.valid_login(request.form['username'],
    	request.form['password']):
        return login.log_the_user_in(request.form['username'])
    else:
    	error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    print 'login fail...'
    return 'login fail...'

@app.route('/search', methods=['GET'])
def search_router():
    error =None
    if 'keyword' in request.args and 'store_id' in request.args :
        return search.search_item(request.args['keyword'],request.args['store_id'])
    else:
        return 'wrong format'

@app.route('/get_item', methods=['GET'])
def get_item_router():
    error =None
    if 'item_id' in request.args and 'store_id' in request.args:
        return search.get_item(request.args['item_id'],request.args['store_id'])
    else:
        return 'wrong format'





if __name__ == '__main__':
    app.run(debug=True)
