class Config:
    SECRET_KEY= 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    DB_HOST= '127.0.0.1'
    DB_USER= 'root'
    DB_PASSWORD= ''
    DB_NAME= 'flask_login'
    

config = {
    'development': DevelopmentConfig
}