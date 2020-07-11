### db scema*
"""
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| uuid        | binary(16)   | NO   | PRI | NULL    |       |
| fname       | varchar(30)  | NO   |     | NULL    |       |
| lname       | varchar(30)  | YES  |     | NULL    |       |
| email       | varchar(50)  | YES  |     | NULL    |       |
| password    | varchar(128) | NO   |     | NULL    |       |
| user_type   | varchar(15)  | NO   |     | NULL    |       |
| city        | varchar(60)  | YES  |     | NULL    |       |
| state       | varchar(50)  | YES  |     | NULL    |       |
| country     | varchar(60)  | YES  |     | NULL    |       |
| zip_code    | varchar(30)  | YES  |     | NULL    |       |
| dob         | date         | YES  |     | NULL    |       |
| mob_no      | varchar(15)  | YES  |     | NULL    |       |
| is_verified | tinyint(1)   | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
"""

def register_user_dbo(mysql,fname,lname,email, encrypted_password, user_type, mobile_no):
    cur = mysql.connection.cursor()
    query = ''' insert into user (uuid, fname, lname, email, password, user_type, mobile_noauth_source,is_verified) 
            values (uuid(), %s,%s,%s,%s,%s,%s,0);'''
    
    val = [fname, lname, email, encrypted_password, user_type, mobile_no,]



def register_user_third_party_dbo(mysql, fname, lname, email):
        cur = mysql.connection.cursor()
        
        query = 
        val = []


def does_email_registered_dbo(mysql, email):

        query = 
        val = 

def login_dbo(mysql, email, password):
        ## check is_verified

        query = 
        val = 

def is_verified_dbo(mysql, email):

        query ="" 
        val =[]
