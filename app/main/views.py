from . import main_bp
from flask import render_template, redirect, url_for, request, flash

from app.extensions import db

from app.models.equip import EqData
from app.models.equip import RMRecords
from app.models.equip import EqCategory
from app.models.equip import RMCategory

from openpyxl import load_workbook


@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/db', methods=['GET', 'POST'])
def dbutil():

    if request.method == 'POST':
        if 'dbfix' in request.form:
            flash01()

        if 'dbupdate' in request.form:
            flash02()

    return render_template('main/dbutil.html')


def flash01():
    EQList = EqData.query.order_by(EqData.eqid)

    eq = []

    OM = 0

    eq_id_list = [eq.eqid for eq in EQList]

    for id in eq_id_list:
        piece = EqData.query.get(id)

    for eq_piece in piece:
        if piece.purch_meter == "":
            OM = OM + 1
    flash(OM)    


def flash02():
    flash('DB Update Button Was Pressed')

