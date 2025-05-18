
from . import bp_auth
from flask import render_template, redirect, url_for, flash
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from app.extensions import BCrypt
from app.extensions import db
from app.extensions import login_manager
from app.models.users import Users
from app.auth.forms import UserForm
from app.auth.forms import LoginForm





@bp_auth.route('/')
def auth():
    
    return 'Login Page'


