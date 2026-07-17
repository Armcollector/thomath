"""Questions module for the Thomas Math Quiz application."""

import random
from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class Question:
    """Dataclass for a math question."""

    type: str
    question: str
    answer: str


def get_questions(difficulty: str) -> list[Question]:
    """Return a list of questions based on the difficulty level."""
    if difficulty == "easy":
        questions = get_easy_questions()
    elif difficulty == "medium":
        questions = get_medium_questions()
    elif difficulty == "hard":
        questions = get_hard_questions()
    else:
        difficulty_message = f"Unknown difficulty: {difficulty}"
        raise ValueError(difficulty_message)

    random.shuffle(questions)  # Shuffle the list of questions
    return questions


def multiplication_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of multiplication with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        q = f"{a} * {b}"
        questions.append(Question(type="multiplication", question=q, answer=str(a * b)))
    return questions


def addition_questions(number: int, min_value: int, max_value: int) -> list[Question]:
    """Return number of addition with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        q = f"{a} + {b}"
        questions.append(Question(type="addition", question=q, answer=str(a + b)))
    return questions


def subtraction_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of subtraction with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        q = f"{a} - {b}"
        questions.append(Question(type="subtraction", question=q, answer=str(a - b)))
    return questions


def percentage_questions(number: int, min_value: int, max_value: int) -> list[Question]:
    """Return number of percentage questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(0, 100)
        b = random.randint(min_value, max_value)
        q = f"Hva er {a} % av {b}"
        questions.append(
            Question(type="percentage", question=q, answer=str(round(a / 100 * b, 2)))
        )
    return questions


def division_questions(number: int, min_value: int, max_value: int) -> list[Question]:
    """Return number of division questions with min and max values."""
    questions = []
    while len(questions) < number:
        a = random.randint(min_value, max_value)

        divisors = [i for i in range(2, 10) if a % i == 0]
        if not divisors:
            continue
        b = random.choice(divisors)

        q = f"{a} / {b}"
        questions.append(Question(type="division", question=q, answer=str(a // b)))
    return questions


def linear_equation_questions(
    number: int, a_value: int, b_value: int
) -> list[Question]:
    """Return number of linear equation questions with a and b values."""
    questions = []
    for _ in range(number):
        a = random.randint(2, a_value) * random.choice([-1, 1])
        b = random.randint(-b_value, b_value)
        x = random.randint(1, 99) * random.choice([-1, 1])
        q = f"{a}x{b}={a * x + b} , x=?" if b < 0 else f"{a}x+{b}={a * x + b} , x=?"
        questions.append(Question(type="linear_equation", question=q, answer=str(x)))
    return questions


def get_easy_questions() -> list[Question]:
    """Return a list of NUMBER_OF_EASY_QUESTIONS questions."""
    random.seed(datetime.now(tz=UTC).date().toordinal())

    questions = []
    questions.extend(multiplication_questions(5, 1, 10))
    questions.extend(addition_questions(4, 500, 2500))
    questions.extend(subtraction_questions(3, 500, 2500))
    return questions


def get_medium_questions() -> list[Question]:
    """Return a list of NUMBER_OF_MEDIUM_QUESTIONS questions."""
    random.seed(datetime.now(tz=UTC).date().toordinal())

    questions = []
    questions.extend(multiplication_questions(6, 10, 20))
    questions.extend(addition_questions(5, 1500, 7500))
    questions.extend(subtraction_questions(3, 1000, 6000))
    return questions


def get_hard_questions() -> list[Question]:
    """Return a list of NUMBER_OF_HARD_QUESTIONS questions."""
    random.seed(datetime.now(tz=UTC).date().toordinal())

    questions = []
    questions.extend(multiplication_questions(3, 20, 999))
    questions.extend(subtraction_questions(4, 1000, 9999))
    questions.extend(percentage_questions(3, 2, 1000))
    questions.extend(division_questions(2, 100, 999))
    questions.extend(linear_equation_questions(7, 10, 100))
    return questions
