from . import db
from flask_login import UserMixin
#for scores
class Scores(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      scores = db.Column(db.Integer)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)  # ForeignKey should match the name of the table 'users'
      user = db.relationship('Users', back_populates='scores', uselist=False)  # One-to-one relationship


#for the users
class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String())
    scores = db.relationship('Scores', back_populates='user')# One-to-one relationship

# for the questions


def __repr__(self):
      return f"<Student {self.name}>"


