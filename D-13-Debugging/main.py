# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("Please try again with a numerical number like 15")
#     age = int(input("How old are you?"))
#
# if age > 18:
#     print(f"You can drive at {age}.")

import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1 , 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate(1, 2, 3, 5, 8, 13 )