import random


def get_gcd(num1, num2):
    while True:
        rest = num1 % num2
        if rest != 0:
            num1 = num2
            num2 = rest
        else:
            return num2


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    answer = get_gcd(num1, num2)
    return question, str(answer)
