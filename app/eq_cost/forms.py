from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired



class FrmEqData(FlaskForm):
    eq_no = StringField('ID:')
    eq_desc = StringField('Description:')
    year = DecimalField("Year:")
    sn = StringField('Serial Number:')
    cat = SelectField('Category:')
    purch_date = DateField('Purchase Date:')
    purch_price = DecimalField("Purchase Price:")
    purch_meter = DecimalField("Orig. Meter:")
    meter_act = DecimalField("Current Meter:")
    meter_job = DecimalField("HJ Meter:")
    meter_type = StringField('Meter_Type')
    loc = StringField("Location:")
    note = StringField('Note:')
    cur_depr = DecimalField("Current Depreciation:")
    cur_rate = DecimalField("Current Rate:")
    submit = SubmitField("Submit Changes")