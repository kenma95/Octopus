from flask import Flask,request

import login
import search
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

'''
@app.route('/register',methods =['POST'])
def register():
    error = None
    if valid_register(request.form['request.form['username'],
    	request.form['password']):
        do_register(request.form['request.form['username'],
    	request.form['password'])
        return 'register succeed'
    else:
        return 'register not valid'
'''

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
    if 'keyword' in request.args:
        search.search_item(request.args['keyword'])
    else:
        return 'wrong format'

if __name__ == '__main__':
    app.run(debug=True)
