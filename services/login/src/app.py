from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

#third party imports
from flask_mysqldb import MySQL   ## Does NOT support yet python3.8 .. 

# importing flask configuration
from config import DevelopmentConfig

# importing dbo functions
from dbo import register_user_dbo


# Creating flask instance
app = Flask(__name__)


#Database instance 
db = MySQL(app)



## support function


## Regex validation of data.. !!!!!!! INCOMPLETE !!!!!
def is_registration_data_valid(data):
     
    return True



#API end points

""" http status code  ref. RFC 7231 HTTP/1.1
204 : No Content

"""


@app.route('/registration', methods=['POST'])
def registration():
    #getting payload in json-dict
    data = request.get_json()

    ##DEBUG Purpose 
    print(data)

    if not data:
        ## no payload received 
        return jsonify({'Logical Status Code':'204'})

    if not is_registration_data_valid(data):
        return jsonify({'Logical Status Code':'400','message':'Registration Data is Invalid !!'})
    
    #do we need exception handling for this??
    #encrypting the password
    encrypted_password = generate_password_hash(data['passwd'], method='sha1')

    ##call db operation to save data in the mysql
    register_user_dbo(
        data['fname'], data['lname'],
        data['email'], encrypted_password,
        data['user_type'], str(data['country_code'] + data['mobile_no']) 
         )

    return "Work in progress"

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/login/google')
def google_login():
    pass

@app.route('/login/linkedin')
def linkedin_login():
    pass

@app.route('/login/facebook')
def facebook_login():
    pass

