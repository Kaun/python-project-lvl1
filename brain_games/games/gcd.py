import random


def get_gsd(num1, num2):
    if not num2:
        return num1
    else:
        return get_gsd(num2, num1 % num2)


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'{num1} {num2}'
    answer = get_gsd(num1, num2)
    return question, str(answer)
