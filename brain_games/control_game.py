import prompt
import random


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def is_prime(num):
    divider = 2
    while num % divider != 0:
        divider += 1
    return 'yes' if divider == num else 'no'


def nod(num_1, num_2):
    while True:
        rest = num_1 % num_2
        if rest != 0:
            num_1 = num_2
            num_2 = rest
        else:
            return num_2


def generate_arithmetic_progression(element, step, length_seq):
    seq = []
    for i in range(length_seq):
        seq.append(element)
        element += step
    return seq


def craft_element(seq):
    seq_craft_el = seq[:]
    craft_el_number = random.randint(0, len(seq) - 1)
    craft_element = seq_craft_el.pop(craft_el_number)
    seq_craft_el.insert(craft_el_number, '..')
    seq_str = " ".join(map(str, seq_craft_el))
    return (seq_str, craft_element)


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
    print('Hello, {}!'.format(name))
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
