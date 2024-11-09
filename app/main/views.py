from . import main_bp
from flask import render_template, redirect, url_for, request, flash

from app.extensions import db

from app.models.equip import EqData
from app.models.equip import RMRecords
from app.models.equip import EqCategory
from app.models.equip import RMCategory

from openpyxl import load_workbook

from datetime import datetime


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
        eq_piece = EqData.query.get_or_404(id)

        
        if eq_piece.purch_price == None:
            eq_piece.purch_price = 0
            db.session.commit()
        else:
            pass
        
        if eq_piece.purch_meter == None:
            eq_piece.purch_meter = 0
            db.session.commit()
        else:
            pass
        
        if eq_piece.purch_date == None:
            eq_piece.purch_date = datetime.strptime("1950-01-01", "%Y-%m-%d")
            db.session.commit()
        else:
            pass

        if eq_piece.meter_act == None:
            eq_piece.meter_act = 0
            db.session.commit()
        else:
            pass

        if eq_piece.cur_depr == None:
            eq_piece.cur_depr = 0
            db.session.commit()
        else:
            pass

        if eq_piece.cur_rate == None:
            eq_piece.cur_rate = 0
            db.session.commit()
        else:
            pass

        if eq_piece.meter_job == None:
            eq_piece.meter_job = 0
            db.session.commit()
        else:
            pass

        if eq_piece.yr == None:
            eq_piece.yr = '1900'
            db.session.commit()
        else:
            pass

        if eq_piece.sn == None:
            eq_piece.sn = '????'
            db.session.commit()
        else:
            pass

        
            
    
   # for id in eq_id_list:
   #     eq_piece = EqData.query.get_or_404(id)
   #     flash(eq_piece.cur_depr)

   


        


    #for eq_piece in piece:
    #    if piece.purch_meter == "":
    #        OM = OM + 1
    #flash(OM)    


def flash02():

    EQList = EqData.query.order_by(EqData.eqid)

    for piece in EQList:
        flash(piece.purch_date)


   

