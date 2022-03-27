from brain_games.control_game import (
    check_answer,
    get_random_elements,
    nod
)
import prompt


def game_gcd():
    num_1, num_2, _ = get_random_elements()
    correct_answer = nod(num_1, num_2)
    print('Find the greatest common divisor of given numbers.')
    print('Question: {} {}'.format(num_1, num_2))
    user_answer = prompt.integer('Your answer: ')
    is_correct_answer = check_answer(user_answer, correct_answer)
    return False if is_correct_answer else True
