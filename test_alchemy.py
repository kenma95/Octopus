import os
#..
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://test_user1:@localhost/shopping_list'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)



class Item(db.Model):
    item_id = db.Column(db.String(40), primary_key=True)
    item_name = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(120), unique=True)
    photo = db.Column(db.String(120))

    def __init__(self, item_id, description,photo_addr):
        self.item_id = item_id
        self.description = description
        self.photo = photo_addr

    def __repr__(self):
        return '<Item %r>' % self.item_id

class User(db.Model):
    	user_id = db.Column(db.String(40), primary_key=True)
	user_name = db.Column(db.String(40), unique=False)
	passwd = db.Column(db.String(40), unique=False)
	avatar = db.Column(db.String(120))

    	def __init__(self, user_id, passwd):
        	self.user_id = user_id
        	self.passwd = passwd
		self.avatar = '111'
    	def __repr__(self):
        	return '<User %r>' % self.user_id
