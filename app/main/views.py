from . import main_bp
from flask import render_template, redirect, url_for, request, flash
from app.extensions import db
from app.models.equip import Equip
from app.models.equip import EqCategory
from app.models.equip import EqUsage

import pandas as pd


from openpyxl import load_workbook

from datetime import datetime


@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/db', methods=['GET', 'POST'])
def dbutil():

    #df = pd.DataFrame()
    #row_display = 'row'

     

    if request.method == 'POST':

        
        if 'eq_cat_update' in request.form:
            
            # Check that the file is correct:

            category_file = request.files['EqCatFile']

            Workbook = load_workbook(category_file)
            Worksheet = Workbook.active
            
            

            #df = pd.read_excel(category_file)

            #col_1 = df.columns[0]
            #col_2 = df.columns[1]

            col_1 = Worksheet.cell(row=1,column=1).value
            col_2 = Worksheet.cell(row=1,column=2).value

            check_columns = (col_1 == 'eq_category_no' and col_2 == 'description')

            if check_columns:
                check = "OK"
            else:
                check = "No Good"

            #file_OK = (file[0] == 'eq_category_no')

            #if file_OK:
            #    check = "OK"
            #else:
            #    check = "No Good"

            #flash(check)

            

            return render_template('main/dbutil.html',col_1=col_1, col_2=col_2, check=check)


        '''
            category_list = []
            category_file = request.files["EqCatFile"]
            added = 0
            skipped = 0
   
            Workbook = load_workbook(category_file)
            Worksheet = Workbook.active
    
            if Worksheet.cell(row=1,column=1).value == 'eq_category_no':

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

            
                    

            else:
                file = "Incorrect"
        '''
            #return render_template('main/dbutil.html', file=file, skipped=skipped, added=added)

            
            

        #if 'eq_list_update' in request.form:
        #    eq_list_import()
 
    
   
    return render_template('main/dbutil.html')

    

        
def eq_list_import():
    equipment_list = []
    equipment_file = request.files["EqListFile"]
    added = 0
    skipped = 0

    Workbook = load_workbook(equipment_file)
    Worksheet = Workbook.active

    if Worksheet.cell(row=1,column=1).value == 'equipment_no':
        flash('Correct Eq List File.')
            
        for row in Worksheet.iter_rows():
            RowCells = []
            for cell in row:
                RowCells.append(cell.value)
            equipment_list.append(tuple(RowCells))
    
            del equipment_list[0]
        '''
        Stopped here. Need to complete mapping for equipment list file.
        
        '''
        for row in equipment_list:
            piece = Equip.query.filter_by(eq_id = row[0]).first()
    
            if piece is None:
                new_category = Equip(eq_no = row[0], eq_desc=row[1],
                                     eq_sn = row[4], eq_yr = row[3],
                                     eq_cat_no = row[7], eq_purch_price = row[10],
                                     ea_purch_date = [5], rate_oper_syst = row[8])
                db.session.add(new_category)
                db.session.commit()
                added += 1
        
            else:
                skipped += 1
        flash(len(equipment_list))
        flash('Skipped: ' + str(skipped))
        flash('Added: '+ str(added))
    else:
        flash('You Chose the Wrong File')
        return render_template('main/dbutil.html')
   
    return render_template('main/dbutil.html')
    
    