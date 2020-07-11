### db scema*
"""
+-------------+--------------+------+-----+---------+-------+
| uuid        | varchar(255) | NO   | PRI | NULL    |       |
| fname       | varchar(50)  | NO   |     | NULL    |       |
| lname       | varchar(50)  | YES  |     | NULL    |       |
| email       | varchar(320) | YES  | UNI | NULL    |       |
| password    | varchar(254) | YES  |     | NULL    |       |
| user_type   | varchar(20)  | YES  |     | NULL    |       |
| city        | varchar(50)  | YES  |     | NULL    |       |
| state       | varchar(50)  | YES  |     | NULL    |       |
| country     | varchar(60)  | YES  |     | NULL    |       |
| zipcode     | varchar(30)  | YES  |     | NULL    |       |
| dob         | date         | YES  |     | NULL    |       |
| mobile_no   | varchar(30)  | YES  |     | NULL    |       |
| is_verified | tinyint(1)   | YES  |     | 0       |       |
| auth_source | varchar(30)  | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
"""


"""
create table user (
        uuid varchar(255) PRIMARY KEY,
        fname varchar(50) NOT NULL,
        lname varchar(50),
        email varchar(320) UNIQUE,
        password varchar(254),
        user_type varchar(20),
        city varchar(50),
        state varchar(50),
        country varchar(60),
        zipcode varchar(30),
        dob date,
        mobile_no varchar(30),
        is_verified tinyint(1) default '0',
        auth_source varchar(30)
);       

"""

"""
insert into user 
(uuid, fname, lname, email, password, user_type, auth_source, mobile_no) 
values (uuid(),
 'Shardul', 'Kulkarni',
  'shardulind@gmail.com', 'jkasnfaklfnkladsnf',
   'organization', 'volunteeer', '+918275791691');

"""


##########--------------------------------------------------- DONT TOUCH: Its working perfectly fine!  
def register_user_dbo(mysql, fname, lname, email, encrypted_password, user_type, mobile_no):

    ## add exception handling
    cur = mysql.connection.cursor()
    query = '''insert into user (uuid, fname, lname, email, password, user_type, auth_source, mobile_no)
            values (uuid(), %s,%s,%s,%s,%s,%s,%s); '''


    val = [fname, lname, email, encrypted_password, user_type, 'Volunteeer', mobile_no]
    cur.execute(query, val)
    print(cur.rowcount, "Record inserted successfully into user table")
    
    mysql.connection.commit()
    cur.close()

    return True
##########---------------------------------------------------


## registration through linkedin, google, fb
def register_user_third_party_dbo(mysql, fname, lname, email, auth_source):
    cur = mysql.connection.cursor()

    query =''' insert into user (uuid, fname, lname, email, auth_source,is_verified)
            values (uuid(), %s,%s,%s,%s,1);'''

    val = [fname, lname, email,auth_source]
    cur.execute(query, val)
    print(cur.rowcount, "Record inserted successfully into user table")
    mysql.connection.commit()
    cur.close()
    return True

def does_email_registered_dbo(mysql, email):

        cursor = mysql.connection.cursor()
        query = ''' select * from user where email like %s '''

        val = [email]
        cursor.execute(query, val)
        if cursor.rowcount == 0:
                return False
        else:
                return True


def login_dbo(mysql, email, password):
    ## check is_verified

    query = ''' insert into user (mysql, email,password )
            values (email(),password());'''
    val = [email, password]
    cursor.execute(query)
    print(cursor.rowcount, "Record inserted successfully into user table")
    cursor.close()


def is_verified_dbo(mysql, email,password):
    query = ''' insert into user (mysql, email,password )
                values (email(),password());'''
    val = [email, password]
    cursor.execute(query)
    print(cursor.rowcount, "Record inserted successfully into user table")
    cursor.close()



