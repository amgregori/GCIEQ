from . import bp_report
#from flask_login import login_required
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

from openpyxl import load_workbook

from app.extensions import db

from app.models.equip import Equip
from app.models.equip import EqCategory
from app.models.equip import EqUsage


from .forms import FrmEqData

from datetime import datetime



#from app.extensions import db
#from app.models.equip import Jobs
#from app.eqip.forms import NewJobForm



@bp_report.route('/', methods=['GET', 'POST'])
def report_main():
    return 'Reports Main Page'
