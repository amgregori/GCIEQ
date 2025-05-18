#This blueprint deals with all user management and login functionality

from flask import Blueprint

bp_eq_cost = Blueprint('eq_cost', __name__, template_folder='templates')

from . import views