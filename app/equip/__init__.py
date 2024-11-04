#This blueprint deals with all user management and login functionality

from flask import Blueprint

equip_bp = Blueprint('equip', __name__, template_folder='templates')

from . import views