"""Questions module for the Thomas Math Quiz application."""

import random
from dataclasses import dataclass
from datetime import UTC, datetime
from fractions import Fraction


@dataclass
class Question:
    """Dataclass for a math question."""

    type: str
    question: str
    answer: Fraction


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
        questions.append(
            Question(
                type="multiplication",
                question=q,
                answer=Fraction(a * b),
            )
        )
    return questions


def addition_questions(number: int, min_value: int, max_value: int) -> list[Question]:
    """Return number of addition with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        q = f"{a} + {b}"
        questions.append(Question(type="addition", question=q, answer=Fraction(a + b)))
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
        questions.append(
            Question(type="subtraction", question=q, answer=Fraction(a - b))
        )
    return questions


def percentage_questions(number: int, min_value: int, max_value: int) -> list[Question]:
    """Return number of percentage questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(0, 100)
        b = random.randint(min_value, max_value)
        q = f"Hva er {a} % av {b}"
        questions.append(
            Question(
                type="percentage", question=q, answer=Fraction(a, 100) * Fraction(b)
            )
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
        questions.append(Question(type="division", question=q, answer=Fraction(a // b)))
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
        q = f"{a}x{b:+}={a * x + b} , x=?"
        questions.append(
            Question(type="linear_equation", question=q, answer=Fraction(x))
        )
    return questions


def linear_equations_with_brackets_questions(
    number: int, a_value: int
) -> list[Question]:
    """Return number of linear equation questions with brackets with a value.

    Of the form a(bx +- c) = dx +- e, where a, b, c, d, e are integers and x is the variable to solve for.
    """
    questions = []
    for _ in range(number):
        a = random.randint(2, a_value)
        b = random.randint(-a_value, a_value)
        c = random.randint(-a_value, a_value)
        d = random.randint(-a_value, a_value)
        x = random.randint(1, 15) * random.choice([-1, 1])
        e = a * (b * x + c) - d * x

        q = f"{a}({b}x{c:+})={d}x{e:+} , x=?"
        questions.append(
            Question(
                type="linear_equation_with_brackets", question=q, answer=Fraction(x)
            )
        )
    return questions


def fraction_multiplied_by_integer_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of fraction multiplied by integer questions with min and max values."""
    questions = []
    for _ in range(number):
        a_numerator = random.randint(min_value, max_value)
        a_denominator = random.randint(min_value, max_value)
        b_integer = random.randint(min_value, max_value)

        q = f"({a_numerator}/{a_denominator}) * {b_integer}"
        a_frac = Fraction(a_numerator, a_denominator)
        answer = a_frac * b_integer
        questions.append(
            Question(type="fraction_multiplied_by_integer", question=q, answer=answer)
        )
    return questions


def fraction_multiplication_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of fraction multiplication questions with min and max values."""
    questions = []
    for _ in range(number):
        a_numerator = random.randint(min_value, max_value)
        a_denominator = random.randint(min_value, max_value)
        b_numerator = random.randint(min_value, max_value)
        b_denominator = random.randint(min_value, max_value)

        q = f"({a_numerator}/{a_denominator}) * ({b_numerator}/{b_denominator})"
        a_frac = Fraction(a_numerator, a_denominator)
        b_frac = Fraction(b_numerator, b_denominator)
        answer = a_frac * b_frac
        questions.append(
            Question(type="fraction_multiplication", question=q, answer=answer)
        )
    return questions


def fraction_division_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of fraction division questions with min and max values."""
    questions = []
    for _ in range(number):
        a_numerator = random.randint(min_value, max_value)
        a_denominator = random.randint(min_value, max_value)
        b_numerator = random.randint(min_value, max_value)
        b_denominator = random.randint(min_value, max_value)

        q = f"({a_numerator}/{a_denominator}) / ({b_numerator}/{b_denominator})"

        a_frac = Fraction(a_numerator, a_denominator)
        b_frac = Fraction(b_numerator, b_denominator)

        answer = a_frac / b_frac
        questions.append(Question(type="fraction_division", question=q, answer=answer))
    return questions


def fraction_addition_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of fraction addition questions with min and max values."""
    questions = []
    for _ in range(number):
        a_numerator = random.randint(min_value, max_value)
        a_denominator = random.randint(min_value, max_value)
        b_numerator = random.randint(min_value, max_value)
        b_denominator = random.randint(min_value, max_value)

        q = f"({a_numerator}/{a_denominator}) + ({b_numerator}/{b_denominator})"

        a_frac = Fraction(a_numerator, a_denominator)
        b_frac = Fraction(b_numerator, b_denominator)
        answer = a_frac + b_frac
        questions.append(Question(type="fraction_addition", question=q, answer=answer))
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
    questions.extend(multiplication_questions(1, 20, 999))
    questions.extend(subtraction_questions(1, 1000, 9999))
    questions.extend(percentage_questions(2, 2, 1000))
    questions.extend(division_questions(2, 100, 999))
    questions.extend(linear_equation_questions(2, 10, 100))
    questions.extend(fraction_multiplication_questions(3, 2, 20))
    questions.extend(fraction_division_questions(3, 2, 20))
    questions.extend(fraction_addition_questions(2, 2, 20))
    questions.extend(fraction_multiplied_by_integer_questions(2, 2, 20))
    questions.extend(linear_equations_with_brackets_questions(2, 10))
    return questions
