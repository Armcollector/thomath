from flask import Flask, render_template, request
import random
from datetime import date

app = Flask(__name__)


def get_questions():
    """Return a list of 20 questions."""
    random.seed(date.today().toordinal)

    questions = []
    for _ in range(20):
        a = random.randint(2, 20)
        b = random.randint(2, 20)
        q = f"{a} * {b}"
        questions.append({'q': q, 'a': str(a * b)})
    random.shuffle(questions)  # Shuffle the list of questions
    return questions

@app.route('/')
def index():
    # Define a list of 20 math questions

    return render_template('index.html', questions= get_questions())

@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's answers from the form
    answers = [request.form[f'answer{str(i)}'] for i in range(1, 21)]

    # Define the correct answers to the questions
    correct_answers = [q['a'] for q in  get_questions()]

    # Compute the number of correct answers
    num_correct = sum(answers[i] == correct_answers[i] for i in range(20))

    return render_template('submit.html', num_correct=num_correct)

if __name__ == '__main__':

    app.run(debug=True)
    
