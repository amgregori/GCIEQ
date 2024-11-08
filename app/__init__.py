"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured 
for different environments based on the value of the CONFIG_TYPE environment variable
"""
import os
from flask import Flask
from app.extensions import BCrypt
from app.extensions import db
from app.extensions import login_manager




#App Factory

def create_app():
    app = Flask(__name__)

    

    #Configure flask instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
    app.config['SECRET_KEY'] = "Sjh23sui2Swi1"

    #Initialize Database:
    db.init_app(app)

    
    #Initialize PW Hashing Function:
    #BCrypt.init_app(app)


    #Initialize Login Manager:
    #login_manager.init_app(app)


    #Register Blueprints
    register_blueprints(app)

    


    return app

def register_blueprints(app):
    from app.auth import auth_bp
    
    from app.main import main_bp
    from app.equip import equip_bp
    
    

    app.register_blueprint(auth_bp, url_prefix='/users')
   
    app.register_blueprint(equip_bp, url_prefix='/equip')
    app.register_blueprint(main_bp)