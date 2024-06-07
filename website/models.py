from . import db
from flask_login import UserMixin
#for scores
class Scores(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      scores = db.Column(db.Integer)
      User_id = db.Column(db.Integer,db.ForeignKey('user.id'))
#for the users
class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String())
    score = db.relationship('Scores')