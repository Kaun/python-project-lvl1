import prompt


def start_game(game):
    NUMBER_ATTEMPTS = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

    print(game.get_description())
    for attempt in range(NUMBER_ATTEMPTS):
        question, answer = game.get_question_and_answer()
        print('Question: {}'.format(question))

        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".'
                  .format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
