from flask import Flask , render_template, redirect, url_for
import random, copy
app = Flask(__name__)

original_question = {
    'How many bones does a shark has?':['0'],
    'How many bones does a human has?':['206'],
    'How many countries in the world?':['195'],
    'What is the largest dessert?' :['antartica'];
    ''
}
def shuffle(q):

questions = copy.deepcopy(original_question)

@app.route("/")
def index():
    return render_template("index.html")