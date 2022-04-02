import random


def calculate(num1, num2, sign):
    res = 0
    if sign == '+':
        res = num1 + num2
    if sign == '-':
        res = num1 - num2
    if sign == '*':
        res = num1 * num2
    return res


def get_description():
    return 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    sign = random.choice(['+', '-', '*'])

    question = '{} {} {}'.format(num1, sign, num2)
    answer = calculate(num1, num2, sign)
    # print('Answer ', answer)
    return question, str(answer)


if __name__ == 'main':
    pass
