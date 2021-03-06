import os

from flask import Flask,jsonify
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://test_user1:@localhost/shopping_list'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Item(db.Model):
    item_id = db.Column(db.String(40), primary_key=True)
    store_id = db.Column(db.String(40), primary_key=True)
    item_name = db.Column(db.String(120), unique=False)
    price = db.Column(db.Numeric(6,2),unique =False)
    description = db.Column(db.Text(3000), unique=False)
    photo = db.Column(db.String(120))
    remain = db.Column(db.Integer,unique=False)
    locx = db.Column(db.Integer,unique = False)
    locy = db.Column(db.Integer,unique = False)

    def to_json3(self):
	return {'item_id' : self.item_id
	    ,'locx' : self.locx
	    ,'locy': self.locy
    }


    def to_json2(self):
        return {'item_id' : self.item_id
            ,'item_name' : self.item_name
            ,'store_id': self.store_id
            ,'price' : str(self.price)
            ,'description' : self.description
            ,'photo' : self.photo
            ,'remain' : self.remain
            }

    def to_json1(self):
        return {'item_id' : self.item_id
            ,'item_name' : self.item_name
            ,'store_id': self.store_id
            ,'price' : str(self.price)
            }



    def __init__(self, item_id,\
		 store_id,item_name,price,description,photoaddr):
        self.item_id = item_id
        self.store_id = store_id
        self.item_name = item_name
        self.price =price
        self.description = description
        self.photo = photoaddr

    def __repr__(self):
        return '<Item %r>' % self.item_id



class User(db.Model):
    user_id = db.Column(db.String(40), primary_key=True)
    user_name = db.Column(db.String(40), unique=False)
    passwd = db.Column(db.String(255), unique=False)
    avatar = db.Column(db.String(120))

    def __init__(self, user_id, passwd):
        self.user_id = user_id
        self.passwd = passwd
        self.avatar = '111'

    def __repr__(self):
        return '<User %r>' % self.user_id




class Store(db.Model):
    store_id = db.Column(db.String(40), primary_key=True)
    store_name = db.Column(db.Text(3000), unique=False)
    address = db.Column(db.Text(3000),unique=False)

    def to_json1(self):
        return {'store_id' : self.store_id
            ,'store_name' : self.store_name
            ,'address': self.address
            }



    def __init__(self, store_id,\
		 store_name,address):
        self.store_id = store_id
        self.store_name =store_name
        self.address = address
  

    def __repr__(self):
        return '<Store %r>' % self.item_id

class User_Store(db.Model):
    store_id = db.Column(db.String(40), primary_key=True)
    userid  = db.Column(db.String(40),primary_key = True)

    def __init__(self, store_id,user_id):
        self.store_id = store_id
        self.userid = user_id
  
    def __repr__(self):
	return '<Userstore %r>' % self.store_id 
    def get_store_id(self):
	return self.store_id
