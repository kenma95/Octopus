from db_schema import *
import hashlib

salt = b'oct'

#login related
def valid_login(username,password):
    print 'checking_login...'
    s_pwd = hashlib.sha1(salt+password).hexdigest()
    valid = User.query.filter_by(user_id = username, passwd = s_pwd).first()

    return valid is not None

def log_the_user_in(username):
    print 'login succeed...'
    return 'login succeed...'
