import art
import game_data
import random

def game():
    print(art.logo)

    value1 = random.choice(list(game_data.data))

    print(f"Compare A: {value1['name']},{value1['description']},{value1['country']}")

    print(art.vs)

    value2 = random.choice(list(game_data.data))

    print(f"Against B: {value2['name']},{value2['description']},{value2['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    print(answer)

    a = value1['follower_count']
    b = value2['follower_count']

    print(a)
    print(b)

    total = 0

    if answer == a and a > b:
        total += 1
        print(total)
        game()
    elif answer == b and b > a:
        total += 1
        print(total)
        game()
    elif answer == a and a < b:
        print(f"That's wrong. Final Score: {total}")
    elif answer == b and b > a:
        print(f"That's wrong. Final Score: {total}")







