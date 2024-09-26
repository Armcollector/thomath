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
    for _ in range(3):
        a = random.randint(20, 999)
        b = random.randint(20, 999)
        q = f"{a} * {b}"
        questions.append({"q": q, "a": str(a * b)})

    for _ in range(5):
        a = random.randint(2, 100)
        b = random.randint(2, 1000)
        q = f"Hva er {a} % av {b}"
        questions.append({"q": q, "a": round(a / 100 * b, 2)})

    while len(questions) < 10:
        a = random.randint(100, 999)

        divisors = [i for i in range(2, 10) if a % i == 0]
        if not divisors:
            continue
        b = random.choice(divisors)

        q = f"{a} / {b}"
        questions.append({"q": q, "a": str(a // b)})

    while len(questions) < 13:
        a = random.randint(1000, 9999)
        b = random.randint(1000, 9999)
        b, a = sorted([a, b])
        q = f"{a} - {b}"
        questions.append({"q": q, "a": str(a - b)})

    while len(questions) < 20:
        a = random.randint(2, 10) * random.choice([-1, 1])
        b = random.randint(-100, 100)
        x = random.randint(1, 99) * random.choice([-1, 1])
        q = f"{a}x{b}={a * x + b} , x=?" if b < 0 else f"{a}x+{b}={a * x + b} , x=?"
        questions.append({"q": q, "a": str(x)})

    random.shuffle(questions)  # Shuffle the list of questions
    return questions


@app.route("/", methods=["GET", "POST"])
def index():
    if "nr_answered" not in session:
        session["nr_answered"] = 0
    if "difficulty" not in session:
        session["difficulty"] = "hard"
    # Define a list of 20 math questions

    if request.form.get("difficulty") is not None:
        new_difficulty = request.form.get("difficulty")
        if new_difficulty in ["easy", "medium", "hard"]:
            session["difficulty"] = new_difficulty
        else:
            raise ValueError(f"Unknown difficulty: {new_difficulty}")
        return render_template(
            "index.html",
            questions=get_questions(new_difficulty),
            answers=[],
            progress=0,
        )

    difficulty = session.get("difficulty", "hard")

    submitted_answers = [
        float(i) if i != "" else None for i in list(request.form.values())
    ]
    correct_answers = [float(q["a"]) for q in get_questions(difficulty)]
    if submitted_answers != correct_answers:
        answers = {
            k: "" if (v == "" or float(v) != a) else v
            for (k, v), a in zip(request.form.items(), correct_answers)
        }
        progress = int(
            sum(a == b for a, b in zip(submitted_answers, correct_answers))
            / len(correct_answers)
            * 100
        )
        if progress > session["nr_answered"]:
            flash("Well Done, please continue.", "info")
        else:
            flash("Please try again.", "danger")

        session["nr_answered"] = progress

        return render_template(
            "index.html",
            questions=get_questions(difficulty),
            answers=answers,
            progress=progress,
        )

    # Calculate score and redirect to success page
    return redirect(url_for("success", score=100))


@app.route("/success/<int:score>")
def success(score):
    return render_template("success.html", score=score)


if __name__ == "__main__":
    app.run(debug=True)
