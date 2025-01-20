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

        if 'eq_list_update' in request.form:
            eq_list_import()


    return render_template('main/dbutil.html')

    


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

    if Worksheet.cell(row=1,column=1).value == 'equipment_no':
                    
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
        
def eq_list_import():
    equipment_list = []
    equipment_file = request.files["EqListFile"]
    added = 0
    skipped = 0

    Workbook = load_workbook(equipment_file)
    Worksheet = Workbook.active

    if Worksheet.cell(row=1,column=1).value == 'eq_category_no':
        flash('Correct File.')
            
        for row in Worksheet.iter_rows():
            RowCells = []
            for cell in row:
                RowCells.append(cell.value)
            equipment_list.append(tuple(RowCells))
    
            del equipment_list[0]
        '''
        Stopped here. Need to complete mapping for equipment list file.
        
        '''
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
   
    return render_template('main/dbutil.html')
    
    