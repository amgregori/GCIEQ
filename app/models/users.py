from app.extensions import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name_first = db.Column(db.String(50), nullable=False)
    name_last = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(500))

    def __repr__(self):
        return '<E-Mail: %r>' % self.email