
from . import main_bp
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



@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/db', methods=['GET', 'POST'])
def dbutil():
    


    

    if request.method == 'POST':        
        if 'eq_cat_update' in request.form:
            
            # Check that the file is correct:

            category_file = request.files['EqCatFile']
            
            df = pd.read_excel(category_file)
            
            col_1 = df.columns[0]
            col_2 = df.columns[1]

            
            check_columns = (col_1 == 'eq_category_no' and col_2 == 'description')

            if check_columns:
                check = "OK"

                df.rename(columns={'eq_category_no': 'cat_id', 'description': 'cat_desc'}, inplace=True)

                extg_data = pd.read_sql_table('eq_category', engine)
                comb_data = pd.concat([extg_data, df], ignore_index=True)

                

                add = comb_data[~comb_data.duplicated(keep=False)]

                
                add.to_sql('eq_category', engine, if_exists='append', index=False)

                LenExt = len(extg_data)
                LenNew = len(df)
                LenCom = len(comb_data)
                LenAdd = len(add)

                return render_template('main/dbutil.html',col_1=col_1, col_2=col_2, check=check, LenExt=LenExt,
                                    LenNew=LenNew, LenCom=LenCom, LenAdd=LenAdd)

              
            else:
                check = "No Good"              

                return render_template('main/dbutil.html', check=check)
            
            
    
                  
    if 'eq_usage_import' in request.form:
            
            # Check that the file is correct:

            eq_usage_file = request.files['EqUsageFile']

            file_check = eq_usage_file_check(eq_usage_file)

            if file_check == 'OK':

                imported_rows = eq_usage_import(eq_usage_file)

                flash(imported_rows)
                flash(eq_usage_file.filename)
            
            
            
                
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
    
    