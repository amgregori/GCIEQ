from app.extensions import db



class EqData(db.Model):
    eqid = db.Column(db.String(50), primary_key=True, nullable=False)       # Equipment number from Maint Pro or Foundation
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    yr = db.Column(db.Integer)
    sn = db.Column(db.String(50))
    eqcat = db.Column(db.String(20))                                           # Category ID. This needs to be a foreign key.
    purch_date = db.Column(db.Date())
    purch_price = db.Column(db.Numeric(10,2))
    purch_meter = db.Column(db.Integer)
    meter_act = db.Column(db.Integer)                                        # Actual current 
    meter_job = db.Column(db.Integer)                                        # Actual reported from field
    meter_type = db.Column(db.String(20))
    loc = db.Column(db.String(100))
    note = db.Column(db.String(1000))

    def __repr__(self):
        return '<Project: %r>' % self.eqid
    

class RMRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    rmcatid = db.Column(db.Integer) # Category ID. This needs to be a foreign key.
    rmdate = db.Column(db.DateTime)
    rmcost = db.Column(db.Numeric(10,2))
    rmcurhrmi = db.Column(db.Integer)

    def __repr__(self):
        return '<Project: %r>' % self.id
    

class EqCategory(db.Model):
    eqcat = db.Column(db.String(50), primary_key = True, nullable = False, unique = True)

    def __repr__(self):
        return '<Eq Category: %r>' % self.eqcat
    

class RMCategory(db.Model):
    rmcategory = db.Column(db.String(50), primary_key = True, nullable = False, unique = True)

    def __repr__(self):
        return '<Eq Category: %r>' % self.rmcategory

class MeterType(db.Model):
    meter_type = db.Column(db.String(20), primary_key = True, nullable = False, unique = True)

    def __repr__(self):
        return '<Meter Type: %r>' %self.meter_type
