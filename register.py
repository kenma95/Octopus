from db_schema import *
import hashlib

salt = b'oct'


def valid_register(uid,password):
    #do check
    if len(uid) <= 4:
        return -1, "user id is less than 4 characters/numbers."
    if len(password) < 6:
        return -1, "password is less than 6 characters/numbers"
    user_check = User.query.filter_by(user_id = uid).first()
    if user_check is not None:
        return -1,"username already existed"
    return 0, "success"


def add_user(uid,password):
    s_pwd = hashlib.sha1(salt+password).hexdigest()
    new_user = User(uid,s_pwd)
    db.session.add(new_user)
    db.session.commit()
    print "add user " + uid + " pwd" + password
