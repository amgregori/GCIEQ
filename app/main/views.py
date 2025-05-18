
from . import bp_main
from flask import render_template, redirect, url_for, request, flash
from app.extensions import db
from app.models.equip import Equip
from app.models.equip import EqCategory
from app.models.equip import EqUsage
from openpyxl import load_workbook
from datetime import datetime

from sqlalchemy import create_engine
from config import engine

import pandas as pd



from .functions import eq_usage_file_check, eq_usage_import



@bp_main.route('/')
def index():
    current_user = None
    user = None

    tables = ['eq_usage', 'eq_category', 'equip_calc', 'equip']





    return render_template('main/index.html', current_user=current_user, user=user, tables=tables)


    
    