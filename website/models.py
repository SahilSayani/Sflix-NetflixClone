from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    #first_name,last_name,username
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')
# class Entity(db.Model):
#     id=db.Column(db.Integer,primary_key=True)


# class Entity(db.Model):
#     __bind_key__ = 'sflix'
#     __tablename__ = 'categories'
#     id = db.Column('id',db.Integer, primary_key=True)
#     name = db.Column('name', db.String(255), unique=True)

