import art
from game_data import data
import random

def game():
    print(art.logo)

    value1 = random.choice(data)

    print(f"Compare A: {value1['name']},{value1['description']},{value1['country']}")

    print(art.vs)

    value2 = random.choice(data)

    print(f"Against B: {value2['name']},{value2['description']},{value2['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    a = value1['follower_count']
    b = value2['follower_count']

    total = 0

    if answer == a and a > b:
        total += 1
        print("Correct")
        game()
    elif answer == b and b > a:
        total += 1
        print("Correct")
        game()
    elif answer == a and a < b:
        print(f"That's wrong. Final Score: {total}")
    elif answer == b and b > a:
        print(f"That's wrong. Final Score: {total}")

game()





