import prompt
import random
from brain_games.control_game import (
    check_answer,
    craft_element,
    get_random_elements,
    generate_arithmetic_progression,
)


def game_progression():
    first_element, step, _ = get_random_elements()
    length_seq = random.randint(5, 10)
    progression = generate_arithmetic_progression(
        first_element, step, length_seq
    )
    question, answer = craft_element(progression)
    print('What number is missing in the progression?')
    print('Question: {}'.format(question))
    user_answer = prompt.integer('Your answer: ')
    is_correct_answer = check_answer(user_answer, answer)
    return False if is_correct_answer else True
