from . import main_bp
from flask import render_template, redirect, url_for, request, flash
from app.extensions import db
from app.models.equip import Equip
from app.models.equip import EqCategory
from app.models.equip import EqUsage


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

        if 'eq_cat_update' in request.form:
            eq_cat_import()

    return render_template('main/dbutil.html')


def flash01():
    '''
    EQList = Equip.query.order_by(Equip.eq_no)

    eq = []

    OM = 0

    eq_id_list = [eq.eq_no for eq in EQList]
    
    for id in eq_id_list:
        eq_piece = Equip.query.get_or_404(id)

        
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
   '''
   
    flash("Button #1!!")    


def flash02():

    EQList = Equip.query.order_by(Equip.eq_no)

    for piece in EQList:
        flash(piece.eq_purch_date)


   

def eq_cat_import():
    category_list = []
    category_file = request.files["EqCatFile"]
    added = 0
    skipped = 0

    Workbook = load_workbook(category_file)
    Worksheet = Workbook.active

    if Worksheet.cell(row=1,column=1).value == 'eq_category_no':
        flash('Correct File.')
            
        for row in Worksheet.iter_rows():
            RowCells = []
            for cell in row:
                RowCells.append(cell.value)
            category_list.append(tuple(RowCells))
    
            del category_list[0]
        
        for row in category_list:
            cat = EqCategory.query.filter_by(cat_id = row[0]).first()
    
            if cat is None:
                new_category = EqCategory(cat_id = row[0], cat_desc=row[1])
                db.session.add(new_category)
                db.session.commit()
                added += 1
        
            else:
                skipped += 1

        #flash('Skipped: ' + str(skipped))
        #flash('Added: '+ str(added))
    else:
        flash('You Chose the Wrong File')
        return render_template('main/dbutil.html')
        
    
    