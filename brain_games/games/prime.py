# import prompt
import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(0, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
