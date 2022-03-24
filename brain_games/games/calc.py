from brain_games.control_game import (
    calculate,
    check_answer,
    get_random_elements
)
import prompt


def game_calc():
    num_1, num_2, sign = get_random_elements()
    correct_answer = calculate(num_1, num_2, sign)
    print('Question: {} {} {}'.format(num_1, sign, num_2))
    user_answer = prompt.integer('Your answer: ')
    is_correct_answer = check_answer(user_answer, correct_answer)
    return False if is_correct_answer else True


if __name__ == 'main':
    pass
