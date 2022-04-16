import random


def get_description():
    return 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 20)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = list(range(start, (start + length * step), step))

    progression[hidden_index], answer = '..', progression[hidden_index]
    question = ' '.join(map(str, progression))

    return question, str(answer)
