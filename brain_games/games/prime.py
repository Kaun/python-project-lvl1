# import prompt
import random


def is_prime(num):
    if num < 1:
        return False
    else:
        divider = 2
        while num % divider != 0:
            divider += 1
    return True if divider == num else False


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
