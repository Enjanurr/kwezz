from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=["POST","GET"])
def login():
    data = request.form
    print(data)
    return render_template('index.html', boolean=True)

@auth.route('/questions', methods=["POST","GET"])
def logout():
    return render_template('question.html')

@auth.route('/sign-up')
def sign_up():
    return '<p>sign-up</p>'
