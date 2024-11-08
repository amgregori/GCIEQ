from . import equip_bp
#from flask_login import login_required
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

from openpyxl import load_workbook

from app.extensions import db

from app.models.equip import EqData
from app.models.equip import RMRecords
from app.models.equip import EqCategory
from app.models.equip import RMCategory

from .forms import FrmEqData




#from app.extensions import db
#from app.models.equip import Jobs
#from app.eqip.forms import NewJobForm



@equip_bp.route('/', methods=['GET', 'POST'])
def equip_main():

    form = FrmEqData()
    title = "Master Equipment List"
    eqlist = EqData.query.order_by(EqData.eqid)

    return render_template('/equip/equipmain.html', title=title, eqlist=eqlist, form=form)
    





@equip_bp.route('/eq_data', methods=['GET', 'POST'])
def eq_data():
    form = FrmEqData()

    title = 'Equipment Details'

    eqid_l = EqData.query.order_by(EqData.eqid)
    eqid_list = [(eqid.eqid, eqid.make) for eqid in eqid_l]

    eq_cat = EqCategory.query.order_by(EqCategory.eqcat)

    form.eqid.choices = eqid_list

    


    return render_template('/equip/eq_data.html', form=form, title=title)
    
@equip_bp.route('/equip/eq_edit/<eqid>', methods=['GET', 'POST'])
def eq_edit(eqid):
    form = FrmEqData()
    title = "Equipment Data"

    eq_piece = EqData.query.get_or_404(eqid)

    eq_cat_l = EqCategory.query.order_by(EqCategory.eqcat)
    eq_cat_list = [cat.eqcat for cat in eq_cat_l]
    eq_cat = EqCategory.query.order_by(EqCategory.eqcat)

    form.cat.choices = eq_cat_list



    form.cat.data = eq_piece.eqcat

    

    if request.method == "POST" and form.validate_on_submit():

        eq_piece.note = form.note.data

       
        rate = request.form['note']
     
        flash(rate)


    
        try:

            #db.session.commit()           
            

            #flash(form.cur_depr.data)
            
            


            return render_template('/equip/eq_data.html', form=form, eq_piece=eq_piece, eqid=eqid, eq_cat=eq_cat)
        
        except:
            flash("Something went wrong.")
    
    else:
       flash(form.errors)             


    return render_template('/equip/eq_data.html', form=form, eq_piece=eq_piece, eqid=eqid, eq_cat=eq_cat)
    #return render_template('/equip/eq_data.html', form=form, eq_piece=eq_piece)
