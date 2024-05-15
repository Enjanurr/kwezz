from flask import Flask , render_template
import random, copy


app = Flask(__name__)

original_question = {
'How many bones does a shark has?':['0'],
'How many bones does a human has?':['206'],
'How many countries in the world?':['195'],
'What is the largest dessert?' :['antartica'], 
}

questions = copy.deepcopy(original_question) 

def shuffle(q):
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(q.keys())
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys
 
 @app.route('/')
def quiz():
 questions_shuffled = shuffle(questions)
 for i in questions.keys():
  random.shuffle(questions[i])
 return render_template('main.html', q = questions_shuffled, o = questions)


if __name__ == '__main__':
 app.run(debug=True)