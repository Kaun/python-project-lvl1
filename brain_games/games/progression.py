# from brain_games.control_game import (
#     check_answer,
#     is_even,
#     get_random_elements,
#     nod
# )
# import prompt
import random

def generate_arithmetic_progression():
    
    lenght_seq = random.randint(5,10)
    seq = []
    step = random.randint(0, 100)
    element = random.randint(0, 100)
    print(step) 
    print('What number is missing in the progression?')
    question = " ".join(map(str,generate_arithmetic_progression()))
    print('Question: {}'.format(num_1, num_2))
    #TODO: add function generate_arifmetic_seq() and craft element seq
    for i in range(lenght_seq):
        seq.append(element)
        element += step
    craft_element_number = random.randint(0, lenght_seq)
    craft_element = seq.pop(craft_element_number)
    seq.insert(craft_element_number, '..')
    return seq
        
# print(" ".join(map(str,flexiple)))    
print(" ".join(map(str,generate_arithmetic_progression())))    