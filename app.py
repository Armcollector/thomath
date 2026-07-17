"""Main views for app."""

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.wrappers.response import Response

from questions import get_questions

app = Flask(__name__)
app.secret_key = "100digitsofpi"  # noqa: S105


@app.route("/", methods=["GET", "POST"])
def index() -> str | Response:
    """Display main page for thomath."""
    if "nr_answered" not in session:
        session["nr_answered"] = 0
    if "difficulty" not in session:
        session["difficulty"] = "hard"
    if "attempts" not in session:
        session["attempts"] = 0
    # Define a list of 20 math questions

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

    submitted_answers = [
        float(i) if i != "" else None for i in list(request.form.values())
    ]
    correct_answers = [float(q.answer) for q in get_questions(difficulty)]
    if submitted_answers != correct_answers:
        answers = {
            k: "" if (v == "" or float(v) != a) else v
            for (k, v), a in zip(request.form.items(), correct_answers, strict=False)
        }
        progress = int(
            sum(
                a == b for a, b in zip(submitted_answers, correct_answers, strict=False)
            )
            / len(correct_answers)
            * 100
        )
        if progress > session["nr_answered"]:
            flash("Well Done, please continue.", "info")
        elif progress <= session["nr_answered"] and request.method == "POST":
            flash("Please try again.", "danger")
        else:
            flash("Please answer the questions", "info")

        session["nr_answered"] = progress

        return render_template(
            "index.html",
            questions=get_questions(difficulty),
            answers=answers,
            progress=progress,
            difficulty=difficulty,
        )

    # Calculate score and redirect to success page
    return redirect(url_for("success", score=100))


@app.route("/success/<int:score>")
def success(score: int) -> str:
    """Display the success page with the user's score."""
    return render_template("success.html", score=score)


if __name__ == "__main__":
    app.run()
