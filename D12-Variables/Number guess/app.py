import random

random_number = random.randint(1, 100)
print(random_number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess_count = 0
if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.\n")
    while guess_count <= 9:
        guess_remaining = 9 - guess_count
        guess = int(input("Make a guess: "))
        if guess > 100:
            print("The number is between 1 and 100")
            print("Guess again\n")
        elif guess < 1:
            print("The number is between 1 and 100")
            print("Guess again\n")
        elif guess > random_number:
            print("Too high")
            print("Guess again\n")
        elif guess < random_number:
            print("Too low")
            print("Guess again\n")
        else:
            print(f"Your guess is correct. The number is {random_number}")
            break
        print(f"You have {guess_remaining} guesses left")
        guess_count += 1
    print("You Lose")

elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.\n")
    while guess_count <= 4:
        guess_remaining = 4 - guess_count
        guess = int(input("Make a guess: "))
        if guess > 100:
            print("The number is between 1 and 100")
            print("Guess again\n")
        elif guess < 1:
            print("The number is between 1 and 100")
            print("Guess again\n")
        elif guess > random_number:
            print("Too high")
            print("Guess again\n")
        elif guess < random_number:
            print("Too low")
            print("Guess again\n")
        else:
            print(f"Your guess is correct. The number is {random_number}")
            break
        print(f"You have {guess_remaining} guesses left")
        guess_count += 1
    print("You Lose")

else:
    print("Invalid")