from . import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255), nullable=False)
    scores = db.relationship('Scores', back_populates='user', uselist=False)

class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)  # Changed to singular 'score' for clarity
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship('Users', back_populates='scores')

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    questions_text = db.Column(db.String(), nullable=False)  # Corrected typo in column name
    correct_answer = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Question {self.questions_text}>"
