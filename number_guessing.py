import random

print("Welcome to the Number Guessing Game")
print("I'm Thinking of number from 1 to 100")

correct_number = random.randint(1, 100)

game_level = input("Choose Difficulty: easy or hard: ")

total_attempt = 10

if game_level == "hard":
    total_attempt = 5

print(f"Total guess remaining {total_attempt}")
while total_attempt:
    your_guess = int(input("Enter Your Guess:"))

    if your_guess == correct_number:
        print(f"You got it!! The number was {correct_number}")
        break
    elif your_guess > correct_number:
        print("Too High")
        total_attempt -= 1
        print(f"Total guess remaining {total_attempt}")
    elif your_guess < correct_number:
        print("Too Less")
        total_attempt -= 1
        print(f"Total guess remaining {total_attempt}")

    if total_attempt == 0:
        print(f"psssss.The number was: {correct_number}")
