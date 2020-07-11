class DevelopmentConfig(object):
    SECRET_KEY = '!developer'

    #mysql configuration
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'alohmora'
    MYSQL_DB = 'login_service'
    MYSQL_CURSORCLASS = 'DictCursor'

    #Google Oauth credentials
    GOOGLE_CLIENT_ID = "919831296656-bglja6qe5m57lor0gjl6shetob5kof1b.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "hIwbdEbMqRZ8vr3948zphwDK"
    FACEBOOK_CLIENT_ID = "965059147271347"
    FACEBOOK_CLIENT_SECRET = "4861d1d74aaf0fe33eb6c38bfdeaa3b6"

    #Linkedin Oauth Credetnials
    LINKEDIN_CLIENT_ID = "86vzcgadet4n48"
    LINKEDIN_CLIENT_SECRET = "H5nYhvDUd5O425cK"