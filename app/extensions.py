from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

BCrypt = Bcrypt()

login_manager = LoginManager()