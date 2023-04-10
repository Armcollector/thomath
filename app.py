from flask import Flask, flash, redirect, render_template, request, url_for
import random
from datetime import date

app = Flask(__name__)
app.secret_key = "100digitsofpi"


def get_questions():
    """Return a list of 20 questions."""
    random.seed(date.today().toordinal())

    questions = []
    for _ in range(15):
        a = random.randint(2, 20)
        b = random.randint(2, 20)
        q = f"{a} * {b}"
        questions.append({"q": q, "a": str(a * b)})
    random.shuffle(questions)  # Shuffle the list of questions
    return questions


@app.route("/", methods=["GET", "POST"])
def index():
    # Define a list of 20 math questions

    if request.method == "GET":
        return render_template(
            "index.html", questions=get_questions(), answers=request.form, progress=0
        )

    submitted_answers = list(request.form.values())
    correct_answers = [str(q["a"]) for q in get_questions()]
    if submitted_answers != correct_answers:
        flash("Sorry, not all answers are correct. Please try again.", "danger")
        answers = {
            k: a if v == a else ""
            for (k, v), a in zip(request.form.items(), correct_answers)
        }
        progress = int(
            sum(a == b for a, b in zip(submitted_answers, correct_answers))
            / len(correct_answers)
            * 100
        )
        return render_template(
            "index.html", questions=get_questions(), answers=answers, progress=progress
        )

    # Calculate score and redirect to success page
    score = calculate_score(submitted_answers)
    return redirect(url_for("success", score=score))


def calculate_score(answers):
    """
    Calculate the number of correct answers given by the user.
    """
    return sum(
        str(get_questions()[i]["a"]) == answer.strip()
        for i, answer in enumerate(answers)
    )


@app.route("/success/<int:score>")
def success(score):
    return render_template("success.html", score=score)


if __name__ == "__main__":
    app.run(debug=True)
