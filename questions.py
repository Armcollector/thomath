"""Questions module for the Thomas Math Quiz application."""

import random
from dataclasses import dataclass
from datetime import UTC, datetime
from fractions import Fraction
from typing import Literal


@dataclass
class Question:
    """Dataclass for a math question."""

    type: str
    question: str
    answer: Fraction | str
    evaluation_type: Literal["Fraction", "str"]


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
        a = random.randint(min_value, max_value) / 10 ** (random.randint(0, 3))
        b = random.randint(min_value, max_value) / 10 ** (random.randint(0, 3))
        q = f"{a} * {b}"
        questions.append(
            Question(
                type="multiplication",
                question=q,
                answer=Fraction(a * b),
                evaluation_type="Fraction",
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
        questions.append(
            Question(
                type="addition",
                question=q,
                answer=Fraction(a + b),
                evaluation_type="Fraction",
            )
        )
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
            Question(
                type="subtraction",
                question=q,
                answer=Fraction(a - b),
                evaluation_type="Fraction",
            )
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
                type="percentage",
                question=q,
                answer=Fraction(a, 100) * Fraction(b),
                evaluation_type="Fraction",
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
        questions.append(
            Question(
                type="division",
                question=q,
                answer=Fraction(a // b),
                evaluation_type="Fraction",
            )
        )
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
            Question(
                type="linear_equation",
                question=q,
                answer=Fraction(x),
                evaluation_type="Fraction",
            )
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

        b = random.choice([i for i in range(-a_value, a_value + 1) if i != 0])
        c = random.randint(-a_value, a_value)

        d = random.choice([i for i in range(-a_value, a_value + 1) if i != 0])

        x = random.randint(1, 15) * random.choice([-1, 1])
        e = a * (b * x + c) - d * x

        q = f"{a}({b}x{c:+})={d}x{e:+} , x=?"
        questions.append(
            Question(
                type="linear_equation_with_brackets",
                question=q,
                answer=Fraction(x),
                evaluation_type="Fraction",
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
            Question(
                type="fraction_multiplied_by_integer",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
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
            Question(
                type="fraction_multiplication",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
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
        questions.append(
            Question(
                type="fraction_division",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def linear_function_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of function questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        x = random.randint(min_value, max_value)

        q = f"Anta f(x) = {a}x{b:+}, hva er f({x})?"
        answer = Fraction(a * x + b, 1)
        questions.append(
            Question(
                type="function", question=q, answer=answer, evaluation_type="Fraction"
            )
        )
    return questions


def linear_function_question_slope_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of linear function slope questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)

        q = f"Anta f(x) = {a}x{b:+}, hva er stigningstallet?"
        answer = Fraction(a, 1)
        questions.append(
            Question(
                type="linear_function_slope",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def linear_function_question_constant_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of linear function constant questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)

        q = f"Anta f(x) = {a}x{b:+}, hva er konstantleddet?"
        answer = Fraction(b, 1)
        questions.append(
            Question(
                type="linear_function_constant",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
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
        questions.append(
            Question(
                type="fraction_addition",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def bracket_multiplication_question_simple(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of bracket multiplication questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        c = random.randint(min_value, max_value)

        q = f"({a}{b:+}) * {c}"
        answer = Fraction(a + b, 1) * Fraction(c, 1)
        questions.append(
            Question(
                type="bracket_multiplication",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def bracket_multiplication_question_complex(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of complex bracket multiplication questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        c = random.randint(min_value, max_value)
        d = random.randint(min_value, max_value)

        q = f"({a}{b:+}) * ({c}{d:+})"
        answer = Fraction(a + b, 1) * Fraction(c + d, 1)
        questions.append(
            Question(
                type="bracket_multiplication",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def bracket_multiplication_question_variables(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of bracket multiplication (ax+b) (cx+d) questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        c = random.randint(min_value, max_value)
        d = random.randint(min_value, max_value)
        e: int = random.randint(min_value, max_value)

        q = f"Anta funksjonen f(x) = ({a}x{b:+}) * ({c}x{d:+}). Hva er verdien når x = {e}?"
        answer = Fraction(a * e + b, 1) * Fraction(c * e + d, 1)
        questions.append(
            Question(
                type="bracket_multiplication",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
    return questions


def bracket_multiplication_question_variables_complex(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of complex bracket multiplication (ax+b) (cx+d) questions with min and max values."""
    questions = []

    possible_values = list(set(range(min_value, max_value + 1)) - {0, -1, 1})

    for _ in range(number):
        a = random.choice(possible_values)
        b = random.choice(possible_values)
        c = random.choice(possible_values)
        d = random.choice(possible_values)

        q = f"Forenkle uttrykket(skriv på formen xa^2+yab+zb^2) <br> ({a}a{b:+}b) * ({c}a{d:+}b):"

        a_squares = a * c
        ab_coeff = a * d + b * c
        b_squares = b * d

        answer = ""
        if a_squares != 0:
            if a_squares == 1:
                answer += "+a^2"
            else:
                answer += f"{a_squares:+}a^2"
        if ab_coeff != 0:
            if ab_coeff == 1:
                answer += "+ab"
            else:
                answer += f"{ab_coeff:+}ab"

        if b_squares != 0:
            if b_squares == 1:
                answer += "+b^2"
            else:
                answer += f"{b_squares:+}b^2"

        answer = answer.removeprefix("+")

        questions.append(
            Question(
                type="bracket_multiplication",
                question=q,
                answer=answer,
                evaluation_type="str",
            )
        )
    return questions


def cube_volume_questions(
    number: int, min_value: int, max_value: int
) -> list[Question]:
    """Return number of cube volume questions with min and max values."""
    questions = []
    for _ in range(number):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        c = random.randint(min_value, max_value)
        q = f"Beregn volumet av en kuboide med sider {a},{b},{c}."
        answer = Fraction(a * b * c, 1)
        questions.append(
            Question(
                type="cube_volume",
                question=q,
                answer=answer,
                evaluation_type="Fraction",
            )
        )
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
    questions.extend(multiplication_questions(0, 20, 999))
    questions.extend(subtraction_questions(0, 1000, 9999))
    questions.extend(percentage_questions(1, 2, 1000))
    questions.extend(division_questions(1, 100, 999))
    questions.extend(linear_equation_questions(2, 10, 100))
    questions.extend(fraction_multiplication_questions(2, 2, 20))
    questions.extend(fraction_division_questions(2, 2, 20))
    questions.extend(fraction_addition_questions(2, 2, 20))
    questions.extend(fraction_multiplied_by_integer_questions(2, 2, 20))
    questions.extend(linear_equations_with_brackets_questions(2, 10))
    questions.extend(linear_function_questions(3, 2, 20))
    questions.extend(linear_function_question_slope_questions(1, -20, 20))
    questions.extend(linear_function_question_constant_questions(1, -20, 20))
    questions.extend(bracket_multiplication_question_complex(1, -20, 20))
    questions.extend(bracket_multiplication_question_simple(1, -20, 20))
    questions.extend(bracket_multiplication_question_variables(3, -5, 5))
    questions.extend(bracket_multiplication_question_variables_complex(5, -5, 5))
    questions.extend(cube_volume_questions(2, 1, 10))
    return questions
