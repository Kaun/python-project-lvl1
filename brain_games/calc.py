# import prompt
import random


def welcome_user():
    # name = prompt.string('May I have your name? ')
    name = input('May I have your name? ')
    print('Hello,{}!'.format(name))
    return name


def random_elements():
    num_1 = random.randint(0,100)
    num_2 = random.randint(0,100)
    sign = random.choice(['+', '-', '*'])
    return (num_1, num_2, sign)


def calculate(num_1, num_2, sign):
    res = 0
    match sign:
        case '+':
            res = num_1 + num_2
        case '-':
            res = num_1 - num_2
        case '*':
            res = num_1 * num_2
    return res
   

def cycl_game(game):
    number_attempts = 3
    attempt = 0
    while attempt < number_attempts:
        attempt += 1
        game()
        

def game_calc():
    num_1, num_2, sign = random_elements()
    res = calculate(num_1, num_2, sign)
    print('Question: {} {} {}'.format(num_1, sign, num_2))
    print(res)
    
    

def main():
    player_name = welcome_user()
    cycl_game(game_calc)



main()

# print('Welcome to the Brain Games!')
# player_name = input('May I have your name? ')
# print('Hello, {}!'.format(player_name))
# print('What is the result of the expression?')
