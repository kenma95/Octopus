from flask import Flask,request

import db_schema
import login
import search
import register
import add_item
import os
import get_store
from werkzeug import secure_filename
app = Flask(__name__)


UPLOAD_FOLDER = 'static/img/item'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_store',methods = ['GET'])
def get_store_all():
   return get_store.get_all()
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


@app.route('/get_loc', methods=['GET'])
def get_loc_router():
    error =None
    if 'item_id' in request.args and 'store_id' in request.args:
        return search.get_loc(request.args['item_id'],request.args['store_id'])
    else:
        return 'wrong format'

@app.route('/add_item', methods=['POST'])
    if login.valid_login(request.form['username'],
    	request.form['password']):
        #get store id
        store_id = get_store_by_user(request.form['username'])
        if 'item_name' in request.args:
            item_name = request.form['item_name']
            if not check_valid_add(item_name,store_id):
                return add_item.add_failed()
        else:
            return add_item.add_failed()
        if 'item_desc' in request.args:
            item_desc = request.form['item_desc']
        else:
             item_desc = None
        if 'item_price'in request.args:
            item_price = float(request.form['item_price'])
        else:
            item_price =None
        if 'item_img' in request.args:
            img_file = request.files['file']
            filename = secure_filename(file.filename)
        else:
            filename = None
        add_item.add_item_db(store_id,item_name,item_price,item_desc,filename)
        upload_file(img_file)


def upload_file(img_file):
    if img_file and allowed_file(img_file.filename):
        filename = secure_filename(img_file.filename)
        img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
