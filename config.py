import os
from dotenv import load_dotenv
load_dotenv()

# Find absolute path to top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = True
    
    SECRET_KEY = os.getenv('SECRET_KEY', default='8cda0a26e987b29d7da05fa0b0b2bb51')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'gceq.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'gceq.db')  

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default="sqlite:///" + os.path.join(basedir, 'gcllc.db'))