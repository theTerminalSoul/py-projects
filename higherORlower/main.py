from random import choice
import data
import util

print("Welcome to the Higher and Lower game!")
print("Can you guess who has more followers on social media?")
print("-" * 50)

correct_guess = 0

# Pick the first person outside the loop
person1 = choice(data.data)

game_on = True

while game_on:
    person2 = choice(data.data)
    while person1 == person2:
        person2 = choice(data.data)

    print(
        f"\nCompare A: {person1['person']}, a {person1['occupation']} from {person1['country']}."
    )
    print("vs")
    print(
        f"Against B: {person2['person']}, a {person2['occupation']} from {person2['country']}."
    )

    print(
        f"\nDoes {person2['person']} (B) have 'high' or 'low' followers compared to {person1['person']} (A)?"
    )
    while True:
        guess = input("Take Guess (high/low): ").strip().lower()
        if guess in ["high", "low"]:
            break
        else:
            print("Kindly Write exacty high or low")

    result = util.compare_follower(person1, person2)

    if guess == result:
        correct_guess += 1
        print(f"Correct! Current score: {correct_guess}")

        person1 = person2
    else:
        print("Game Over. You lose!")
        game_on = False

print("-" * 50)
print(f"Final Score: You guessed correctly {correct_guess} times!")
