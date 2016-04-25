from db_schema import *
import hashlib
from flask import jsonify


salt = b'oct'

#login related
def valid_login(username,password):
    print 'checking_login...'
    s_pwd = hashlib.sha1(salt+password).hexdigest()
    valid = User.query.filter_by(user_id = username, passwd = s_pwd).first()

    return valid is not None

def log_the_user_in(username):
    print username + ' login succeed...'
    temp =  {'code':0,'msg':'login successfully'}
    return jsonify(target_item = temp)

def login_failed():
    temp = {'code':-1,'msg':'login failed'}
    resp = jsonify(target_item = temp)
    resp.status_code = 200
    return resp
