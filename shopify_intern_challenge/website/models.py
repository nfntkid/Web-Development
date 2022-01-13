#from datetime import timezone
#from sqlalchemy.sql.schema import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func






class User(db.Model, UserMixin):
    # define the schema for the repo
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    fullName = db.Column(db.String(150))
    notes = db.relationship('Note')
    images = db.relationship('Img')







class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
  





class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


 