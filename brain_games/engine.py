import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!')

    print(game.get_description())

    rounds_count = 3
    for attempt in range(rounds_count):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ').lower()
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"(Correct answer was '{correct_answer}').\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')

    print('Congratulations, {name}!')
