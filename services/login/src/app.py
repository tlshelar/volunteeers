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
app.config.from_object(DevelopmentConfig)

#Database instance 
db = MySQL(app)



## support function

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
def is_registration_data_valid(data):
     
    return True


### Development purpose endpoint
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
    pass

@app.route('/login/linkedin')
def linkedin_login():
    pass

@app.route('/login/facebook')
def facebook_login():
    pass



if __name__ == '__main__':
    app.run(debug=True)