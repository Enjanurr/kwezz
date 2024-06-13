from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Users, Questions
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('question.html')

@auth.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        student_name = request.form.get('name')
        user = Users.query.filter_by(student_name=student_name).first()
        if not user:
            new_student = Users(student_name=student_name)
            db.session.add(new_student)
            db.session.commit()
            user = new_student
        login_user(user)
        return render_template('index.html')  # Redirect to the questions route after successful login
    return render_template('index.html')  # Render the login form template for GET requests

@auth.route('/questions', methods=["GET", "POST"])
@login_required  # Ensure only logged-in users can access this route
def questions():
    question = Questions.query.first()  # Assuming you want to display the first question from the database
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == question.correct_answer:
            flash('Correct answer!', 'success')
        else:
            flash('Wrong answer, try again.', 'danger')
        # After processing the answer, you might want to redirect or render the same template again
        return redirect(url_for('auth.questions'))  # Redirect to questions page to display another question or the same question
    return render_template('question.html', question=question)  # Render the questions template and pass the question object

@auth.route('/logout')
@login_required  # Ensure only logged-in users can log out
def logout():
    logout_user()
    return redirect(url_for('auth.login'))  # Redirect to the login page after logout
    