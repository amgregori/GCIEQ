#eq_cat = []
#    
#    #eq_cat = EqCategory.query.order_by(EqCategory.eqcat)
#   #eq_cat_list = [eq_cat.eqcat for cat in eq_cat]#
#
#    eq_piece = EqData.query.get_or_404(eqid)
#
#    form.cat = eq_piece.eqcat
#
#    if request.method == 'POST':
#        eq_piece.eqid = request.form['ID']
#        eq_piece.make = request.form['Make']
#        eq_piece.model = request.form['Model']  
#        eq_piece.yr = form.year.data
#        eq_piece.sn = request.form['SN']
#        eq_piece.eqcat = request.form['Category']
#        eq_piece.purch_date = form.purch_date.data
#        eq_piece.purch_price = form.purch_price.data
#        eq_piece.purch_meter = form.purch_meter.data
#        eq_piece.meter_act = form.meter_act.data
#        eq_piece.meter_job = form.meter_job.data
#        eq_piece.meter_type = request.form['Meter_Type']
#        eq_piece.loc = request.form['Location']  
#        eq_piece.note = request.form['Note']

#        try:
#            db.session.commit()

#        except:
#            flash('Update did not work.')