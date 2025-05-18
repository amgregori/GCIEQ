#This blueprint deals with all user management and login functionality

from flask import Blueprint

bp_report = Blueprint('report', __name__, template_folder='templates')

from . import views