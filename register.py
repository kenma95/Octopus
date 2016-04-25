from db_schema import *
import hashlib

salt = b'oct'


def valid_register(uid,password):
    #do check
    if len(uid) <= 4:
        return False
    if len(password) < 6:
        return False
    user_check = User.query.filter_by(user_id = uid).first()
    if user_check is not None:
        return False
    return True


def add_user(uid,password):
    s_pwd = hashlib.sha1(salt+password).hexdigest()
    new_user = User(uid,s_pwd)
    db.session.add(new_user)
    db.session.commit()
    temp = {'code':0,'msg':'register successfully'}
    print "add user " + uid + " pwd" + password
    return jsonify(target_item = temp)

def reg_failed():
    temp = {'code':-1,'msg':'register failed'}
    resp = jsonify(target_item = temp)
    resp.status_code = 200
    return resp
