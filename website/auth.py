from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Users   # Import the Student model

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        student_name = request.form.get('name')
        new_student = Users(student_name=student_name)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('auth.questions'))  # Redirect to the questions route after successful login
    
    # Code below should execute when the request method is not POST
    data = request.form
    print(data)
    return render_template('question.html', boolean=True)
    
@auth.route('/questions', methods=["POST", "GET"])
def questions():
    return render_template('question.html')

@auth.route('/sign-up')
def sign_up():
    return '<p>sign-up</p>'
