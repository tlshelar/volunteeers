def register_user_dbo(mysql,fname,lname,email, encrypted_password, user_type, mobile_no):
    cur = mysql.connection.cursor()
    query = ''' insert into user (uuid, fname, lname, email, password, user_type, mobile_noauth_source,is_verified) 
            values (uuid(), %s,%s,%s,%s,%s,%s,0);'''
    
    val = [fname, lname, email, encrypted_password, user_type, mobile_no,]



def register_user_third_party_dbo(mysql, fname, lname, email):
        cur = mysql.connection.cursor()
        