import random


def even(num):
    return True if num % 2 == 0 else False


number_attempts = 3
attempt = 0

print('Welcome to the Brain Games!')
player_name = input('May I have your name? ')
print('Hello, {}!'.format(player_name))
print('Answer "yes" if the number is even, otherwise answer "no".')
while attempt < number_attempts:
    attempt += 1
    random_num = random.randint(0, 100)
    is_even = even(random_num)
    print('Question:', random_num)
    answer = input('')
    if (answer == 'yes' and is_even) or (answer == 'no' and not is_even) :
        print('Correct!')
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, 'yes' if is_even else 'no' ))
        break
if attempt == number_attempts:
    print('Congratulations, {}!'.format(player_name))
else:
    print("Let's try again, {}!".format(player_name))