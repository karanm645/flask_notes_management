from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now)#func gets current date and time and stores default value for date
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
    
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)# no user can have the same email (150 character limit)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note')