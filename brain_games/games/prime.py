import prompt
from brain_games.control_game import (
    is_prime,
    check_answer,
    get_random_elements,
)


def game_prime():
    random_element, _, _ = get_random_elements()
    correct_answer = is_prime(random_element)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print('Question: {}'.format(random_element))
    user_answer = prompt.string('Your answer: ').lower()
    is_correct_answer = check_answer(user_answer, correct_answer)
    return False if is_correct_answer else True
