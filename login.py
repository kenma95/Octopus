from test_alchemy import *

#login related
def valid_login(username,password):
    print 'checking_login...'
    valid = User.query.filter_by(user_id = username, passwd = password).first()

    return valid is not None

def log_the_user_in(username):
    print 'login succeed...'
    return 'login succeed...'

