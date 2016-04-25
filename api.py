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
    uid = request.form['username']
    password = request.form['password']
    if register.valid_register(uid,password):
	return register.add_user(uid, password)
    else: 
        return register.reg_failed()


@app.route('/login', methods=['POST'])
def login_router():
    if login.valid_login(request.form['username'],
    	request.form['password']):
        return login.log_the_user_in(request.form['username'])
    else:
    	error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return {'code':"-1",'msg':'login fail...'}
    return login.login_failed()	

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
    app.debug = True
    app.run(host = '0.0.0.0')
