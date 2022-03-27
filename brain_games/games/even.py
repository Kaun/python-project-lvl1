from brain_games.control_game import (
    check_answer,
    is_even,
    get_random_elements,
)
import prompt


def game_even():
    random_num, _, _ = get_random_elements()
    correct_answer = is_even(random_num)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question:', random_num)
    user_answer = prompt.string('Your answer: ')
    is_correct_answer = check_answer(user_answer.lower(), correct_answer)
    return False if is_correct_answer else True
