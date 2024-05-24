from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('question.html', text= 'hello')

@auth.route('/questions')
def logout():
    return render_template('question.html', text= 'hiho')

@auth.route('/sign-up')
def sign_up():
    return '<p>sign-up</p>'
