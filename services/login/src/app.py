from flask import Flask, request, jsonify, url_for,redirect
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os

#third party imports
from flask_mysqldb import MySQL   ## Does NOT support yet python3.8 .. 
from flask_dance.contrib.linkedin import make_linkedin_blueprint, linkedin
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.google import make_google_blueprint, google

# importing flask configuration
from config import DevelopmentConfig

# importing dbo functions
from dbo import (register_user_dbo, does_email_registered_dbo,
                register_user_third_party_dbo)


# Creating flask instance
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

#Database instance 
db = MySQL(app)

#handling environment variable 
#os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


#initiating instacnces for flask dance
linkedin_blueprint = make_linkedin_blueprint(client_id=app.config['LINKEDIN_CLIENT_ID'],client_secret=app.config['LINKEDIN_CLIENT_SECRET'],scope='r_liteprofile,r_emailaddress',redirect_url='/login/linkedin')
facebook_blueprint = make_facebook_blueprint(client_id=app.config['FACEBOOK_CLIENT_ID'],client_secret=app.config['FACEBOOK_CLIENT_SECRET'],redirect_url='/login/facebook')
google_blueprint = make_google_blueprint(client_id=app.config['GOOGLE_CLIENT_ID'],client_secret=app.config['GOOGLE_CLIENT_SECRET'],redirect_url='/login/google')


app.register_blueprint(linkedin_blueprint,url_prefix='/linkedin_login')
app.register_blueprint(facebook_blueprint,url_prefix='/facebook_login')
app.register_blueprint(google_blueprint,url_prefix='/google_login')


## support function

def third_party_user_handler(email, fname, lname, auth_source):
    ## check if email is registered:
    registered = does_email_registered_dbo(db, email)
    print("registered: " + str(registered))
    if not registered:
        db_status = register_user_third_party_dbo(db,fname, lname, email, auth_source)
    
        if db_status:
            return jsonify({"Logical Status Code":"200", "message":"User Registered Successfully",
                            "data":{
                                "fname" : fname,
                                "lname" : lname
                            }
                            })
        
        else:
            return "something went wrong"

    ## if not registered,register 
    elif registered:
        print("start login procedure")
    ## else login

    return "Something went wrong"



##### @ Kajal
## Regex validation of data for login !!!!!!!!!!! INCOMPLETE !!!!!!
# if data is valid return true
# else false
def is_login_data_valid(data):
    return True




###### @ Asmita
## Regex validation of data.. !!!!!!! INCOMPLETE !!!!!
# if data is valid return true
# else false
## Regex validation of data.. !!!!!!! INCOMPLETE !!!!!

def is_registration_data_valid(data):
        return True
"""
    #FNAME
    pattern_fname = '[a-z|A-Z]{2,50}'
    flag = re.match(pattern_fname, data['fname'])
    print("fname:" + str(flag))
    if not flag:
        return False
    
    #LNAME
    pattern_lname = '[a-z|A-Z]{3,40}'
    flag = re.match(pattern_lname, data['lname'])
    print("fname:" + str(flag))
    if not flag:
        return False

    #EMAIL
    pattern_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    flag = re.match(pattern_email, data['email'])
    print("email:" + str(flag))
    if not flag:
        return False

    #MOBILE_NUMBER
    pattern_mobile_no = '^[2-9]{2}[0-9]{8}$'
    flag = re.match(pattern_mobile_no, data['mobile_no'])
    print("mob:" + str(flag))
    if not flag:
        return False

    # COUNTRY_CODE
    pattern_country_code = '(\+\d{1-3})|(\d{1,4})'
    flag = re.match(pattern_country_code, data['country_code'])
    print("country code:" + str(flag))
    if not flag:
        return False

    #PASSWORD
    pattern_password = '^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!#%?&]{6,20}$'
    flag = re.match(pattern_password, data['password'])
    print("pswd:" + str(flag))
    if not flag:
        return False

    return True
"""


### Development purpose endpoint
@app.route('/')
def index():
    return "<a href='/login/facebook'>facebook</a>|  |<a href='/login/linkedin'>linkedin</a>| |<a href='/login/google'>google</a>"


@app.route('/delete_all_user_dev')
def delete_all_user_dev():
    cur = db.connection.cursor()
    query = " delete from user"
    cur.execute(query)
    db.connection.commit()
    cur.close()
    return "ALl users deleted"

@app.route('/get_all_user_dev')
def get_all_user_dev():
    cur = db.connection.cursor()
    query = '''select * from user; '''
    cur.execute(query)

    data = cur.fetchall();
    cur.close()
    return jsonify({'users':data})




#API end points

""" http status code  ref. RFC 7231 HTTP/1.1
204 : No Content

"""



##########--------------------------------------------------- DONT TOUCH: Its working perfectly fine!  
@app.route('/registration', methods=['POST'])
def registration():
    #getting payload in json-dict
    data = request.get_json()

    ##DEBUG Purpose 
    print(data)

    if not data:
        ## no payload received 
        return jsonify({'Logical Status Code':'204', "messsage":"Bad Request"})

    if not is_registration_data_valid(data):
        return jsonify({'Logical Status Code':'400','message':'Registration Data is Invalid !!'})
    
    if does_email_registered_dbo(db, data['email']):
        return jsonify({'Logical Status Code': '409 ','message':'Email id already registered'}) 

    #do we need exception handling for this??
    #encrypting the password
    encrypted_password = generate_password_hash(data['passwd'], method='sha1')

    ##call db operation to save data in the mysql
    db_status = register_user_dbo(db,
        data['fname'], data['lname'],
        data['email'], encrypted_password,
        data['user_type'], str(data['country_code'] + data['mobile_no']) 
         )
    
    if db_status:
        return jsonify({"Logical Status Code":"200", "message":"User Registered Successfully",
                        "data":{
                            "fname" : data['fname'],
                            "lname" : data['lname']
                        }
                        })
    else:
        return jsonify({"Logical Status Code":" ", "message":"Something went wrong"})

    return "Wor"
##########--------------------------------------------------- 



@app.route('/login', methods=['POST'])
def login():

    #data
    #validation regex
    #email_id exists?  
    #password?  login_dbo()
        #not is_verified?
            #response code: 206
        #is_verified == true
            #response code: 200

    pass



## @ TUSHAR
@app.route('/login/google')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    account_info = google.get('oauth2/v2/userinfo')
    print(account_info)
    if account_info.ok:
        account_info_json = account_info.json()
        print(account_info_json)
        user = {}
        #add exception handling for key error
        user['email'] = account_info_json['email']
        user['firstName'] = account_info_json['given_name']
        user['lastName'] = account_info_json['family_name']
        return user
    return "Error!!!"


##########--------------------------------------------------- DONT TOUCH: Its working perfectly fine!  
@app.route('/login/linkedin')
def linkedin_login():
    if not linkedin.authorized:
        return redirect(url_for('linkedin.login'))
    
    profile_info = linkedin.get('me')
    email_info = linkedin.get('emailAddress?q=members&projection=(elements*(handle~))')
    
    if profile_info.ok and email_info.ok:
        email_json = email_info.json()
        profile_json = profile_info.json()
        user = {}
        user['email'] = email_json['elements'][0]['handle~']['emailAddress']
        user['firstName'] = profile_json['firstName']['localized']['en_US']
        user['lastName'] = profile_json['lastName']['localized']['en_US']
        
        return third_party_user_handler(user['email'],user['firstName'], user['lastName'], 'linkedin')
##########---------------------------------------------------




@app.route('/login/facebook')
def facebook_login():
    if not facebook.authorized:
        return redirect(url_for('facebook.login'))
    account_info = facebook.get('me?fields=id,name,email')
    print(account_info)
    if account_info.ok:
        account_info_json = account_info.json()
        user = {}
        user['email'] = account_info_json['email']
        user['firstName'] = account_info_json['name'].split()[0]
        user['lastName'] = account_info_json['name'].split()[1]
        return user
    return "Error!!!"



if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')