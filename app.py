import random
from datetime import date

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "100digitsofpi"


def get_questions(difficulty):
    if difficulty == "easy":
        return get_easy_questions()
    elif difficulty == "medium":
        return get_medium_questions()
    elif difficulty == "hard":
        return get_hard_questions()
    else:
        raise ValueError(f"Unknown difficulty: {difficulty}")


def get_easy_questions():
    """Return a list of 20 questions."""
    random.seed(date.today().toordinal())

    questions = []
    for _ in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        q = f"{a} * {b}"
        questions.append({"q": q, "a": str(a * b)})

    while len(questions) < 9:
        a = random.randint(500, 2500)
        b = random.randint(500, 2500)
        q = f"{a} + {b}"
        questions.append({"q": q, "a": str(a + b)})

    while len(questions) < 12:
        a = random.randint(500, 2500)
        b = random.randint(500, 2500)
        b, a = sorted([a, b])
        q = f"{a} - {b}"
        questions.append({"q": q, "a": str(a - b)})

    random.shuffle(questions)  # Shuffle the list of questions
    return questions


def get_medium_questions():
    """Return a list of 20 questions."""
    random.seed(date.today().toordinal())

    questions = []
    for _ in range(6):
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        q = f"{a} * {b}"
        questions.append({"q": q, "a": str(a * b)})

    while len(questions) < 11:
        a = random.randint(1500, 7500)
        b = random.randint(1500, 7500)
        q = f"{a} + {b}"
        questions.append({"q": q, "a": str(a + b)})

    while len(questions) < 14:
        a = random.randint(1000, 6000)
        b = random.randint(1000, 6000)
        b, a = sorted([a, b])
        q = f"{a} - {b}"
        questions.append({"q": q, "a": str(a - b)})

    random.shuffle(questions)  # Shuffle the list of questions
    return questions


def get_hard_questions():
    """Return a list of 16 questions."""
    random.seed(date.today().toordinal())

    questions = []
    for _ in range(7):
        a = random.randint(20, 50)
        b = random.randint(20, 50)
        q = f"{a} * {b}"
        questions.append({"q": q, "a": str(a * b)})

    while len(questions) < 12:
        a = random.randint(20, 80)

        divisors = [i for i in range(2, a) if a % i == 0]
        if not divisors:
            continue
        b = random.choice(divisors)

        q = f"{a} / {b}"
        questions.append({"q": q, "a": str(a // b)})

    while len(questions) < 16:
        a = random.randint(1000, 9999)
        b = random.randint(1000, 9999)
        b, a = sorted([a, b])
        q = f"{a} - {b}"
        questions.append({"q": q, "a": str(a - b)})

    random.shuffle(questions)  # Shuffle the list of questions
    return questions


@app.route("/", methods=["GET", "POST"])
def index():
    # Define a list of 20 math questions

    if difficulty := request.form.get("difficulty"):
        if difficulty == "easy":
            session["difficulty"] = "easy"
        elif difficulty == "medium":
            session["difficulty"] = "medium"
        elif difficulty == "hard":
            session["difficulty"] = "hard"
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    difficulty = session.get("difficulty", "hard")

    if request.method == "GET":
        return render_template(
            "index.html",
            questions=get_questions(difficulty),
            answers=request.form,
            progress=0,
        )

    submitted_answers = list(request.form.values())
    correct_answers = [str(q["a"]) for q in get_questions(difficulty)]
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
            "index.html",
            questions=get_questions(difficulty),
            answers=answers,
            progress=progress,
        )

    # Calculate score and redirect to success page
    score = calculate_score(submitted_answers, difficulty)
    return redirect(url_for("success", score=score))


def calculate_score(answers, difficulty):
    """
    Calculate the number of correct answers given by the user.
    """
    return sum(
        str(get_questions(difficulty)[i]["a"]) == answer.strip()
        for i, answer in enumerate(answers)
    )


@app.route("/success/<int:score>")
def success(score):
    return render_template("success.html", score=score)


if __name__ == "__main__":
    app.run(debug=True)
