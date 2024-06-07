from flask import Blueprint, render_template, request
from . import db
auth = Blueprint('auth',__name__)

'''from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Route to handle data submission
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        # Retrieve data from the request
        name = request.form['name']

        # Create a new student object
        new_student = Student(name=name)

        try:
            # Add the new student to the session and commit changes to the database
            db.session.add(new_student)
            db.session.commit()
            return 'Student added successfully!'
        except:
            # If an error occurs, rollback changes
            db.session.rollback()
            return 'An error occurred while adding the student.'

if __name__ == '__main__':
    # Create the database tables
    db.create_all()
    app.run(debug=True)
'''
#send data to the data base (needed to be done)
@auth.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
       student_name = request.form.get('name')

    data = request.form
    print(data)
    return render_template('index.html', boolean=True)
    
@auth.route('/questions', methods=["POST","GET"])
def logout():
    return render_template('question.html')

@auth.route('/sign-up')
def sign_up():
    return '<p>sign-up</p>'
