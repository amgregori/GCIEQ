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
    from app.auth import bp_auth
    from app.eq_cost import bp_eq_cost
    from app.eq_use import bp_eq_use
    from app.main import bp_main
    from app.reports import bp_report  

    app.register_blueprint(bp_auth, url_prefix='/login')
    app.register_blueprint(bp_eq_cost, url_prefix='/eq_cost')
    app.register_blueprint(bp_eq_use, url_prefix='/eq_use')
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_report, url_prefix='/report')