from sqlalchemy import create_engine

class config(object):
    SECRET_KEY = "ClaveSecreta"
    SESSION_COOKIE_SECURE = False
    

class DevelopEmConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1/bdidgs803"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 