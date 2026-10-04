"""Main views for app."""

import os
from fractions import Fraction

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.wrappers.response import Response

from questions import get_questions

app = Flask(__name__)
if app.debug:
    app.secret_key = os.urandom(16)  # fresh key every restart → old sessions die
else:
    app.secret_key = "100digitsofpi"  # noqa: S105


def is_close(
    a: Fraction | None, b: Fraction | None, abs_tol: Fraction = Fraction(1, 100)
) -> bool:
    """Check if two fractions are close to each other. Return False if either is None."""
    if a is None or b is None:
        return False
    return abs(a - b) <= abs_tol


def parse_input(value: str) -> Fraction | None:
    """Parse a string input into a Fraction, or return None if the input is empty."""
    if value == "":
        return None

    value = value.replace(" ", "")  # Remove spaces
    value = value.replace(",", ".")  # Replace commas with dots for decimal input

    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError):
        return None


@app.route("/", methods=["GET", "POST"])
def index() -> str | Response:
    """Display main page for thomath."""
    if "nr_answered" not in session:
        session["nr_answered"] = 0
    if "difficulty" not in session:
        session["difficulty"] = "hard"

    if request.form.get("difficulty") is not None:
        new_difficulty = request.form.get("difficulty")
        if new_difficulty in ["easy", "medium", "hard"]:
            session["difficulty"] = new_difficulty
        else:
            message = f"Unknown difficulty: {new_difficulty}"
            raise ValueError(message)
        return render_template(
            "index.html",
            questions=get_questions(new_difficulty),
            answers=[],
            progress=0,
            difficulty=new_difficulty,
        )

    difficulty = session.get("difficulty", "hard")

    questions = get_questions(difficulty)

    # test if submitted answer is correct
    if request.method == "POST":
        submitted_answer = next(parse_input(i) for i in list(request.form.values()))
        correct_answer = questions[session["nr_answered"]].answer
        if is_close(submitted_answer, correct_answer):
            session["nr_answered"] += 1
            flash("Well Done, please continue.", "info")
        else:
            flash("Please try again.", "danger")
    else:
        flash("Please answer the questions", "info")

    progress = round(session["nr_answered"] / len(questions) * 100)

    if session["nr_answered"] >= len(questions):
        return redirect(url_for("success", score=100))

    return render_template(
        "index.html",
        question=questions[session["nr_answered"]],
        progress=progress,
        difficulty=difficulty,
        nr_answered=session["nr_answered"],
    )


@app.route("/success/<int:score>")
def success(score: int) -> str:
    """Display the success page with the user's score."""
    return render_template("success.html", score=score)


if __name__ == "__main__":
    app.run()
