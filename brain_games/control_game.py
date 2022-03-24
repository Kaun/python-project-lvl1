import prompt
import random


def get_random_elements():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    sign = random.choice(['+', '-', '*'])
    return (num_1, num_2, sign)


def calculate(num_1, num_2, sign):
    res = 0
    if sign == '+':
        res = num_1 + num_2
    elif sign == '-':
        res = num_1 - num_2
    elif sign == '*':
        res = num_1 * num_2
    return res


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,{}!'.format(name))
    return name


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'."
              .format(user_answer, correct_answer))
        return False


def start_game(game, user_name):
    number_attempts = 3
    attempt = 0
    while attempt < number_attempts:
        attempt += 1
        is_game_over = game()
        if is_game_over:
            break
    if attempt == number_attempts:
        print('Congratulations, {}!'.format(user_name))
    else:
        print("Let's try again, {}!".format(user_name))


