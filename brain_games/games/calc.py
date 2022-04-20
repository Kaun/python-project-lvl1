import random
import operator


def get_description():
    return 'What is the result of the expression?'


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    operand1 = random.randint(0, 100)
    operand2 = random.randint(0, 100)
    operation = random.choice(list(operations.keys()))

    question = f'{operand1} {operation} {operand2}'
    answer = operations[operation](operand1, operand2)

    return question, str(answer)
