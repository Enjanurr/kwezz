'''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(2), nullable=False)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade'''
'''
from . import db
from flask_login import UserMixin

class Score(db.model):
    id = db.Column(db.integer,primary_key=True)
    student_score = db.column(db.integer, db.ForeignKey('user.student_id'))
     
class User(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True)
    score = db.relationship('Score')
'''
