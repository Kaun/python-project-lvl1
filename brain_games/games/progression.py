import random


def generate_arithmetic_progression(element, step, length_seq):
    seq = []
    for i in range(length_seq):
        seq.append(element)
        element += step
    return seq


def get_description():
    return 'What number is missing in the progression?'


def get_question_and_answer():
    first_element = random.randint(0, 100)
    step = random.randint(1, 100)
    length_seq = random.randint(5, 10)
    hidden_index = random.randint(0, length_seq)

    progression = generate_arithmetic_progression(
        first_element, step, length_seq
    )
    progression[hidden_index], answer = '..', progression[hidden_index]
    question = ' '.join(map(str, progression))

    return question, str(answer)
