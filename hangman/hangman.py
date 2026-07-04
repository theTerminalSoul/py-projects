import constant
import util

game_over = False
wrong_guess = 0
max_guess = 5
your_guess = []

print("=========================================")
print("    Welcome to the HangMan Game!         ")
print("=========================================")
print("Can you guess the hidden word and save the HangMan?\n")

random_word = util.choose_random_word()
hidden = util.make_hidden(random_word)

# Print initial empty gallows and the blank word
print(constant.HANGMAN_STAGES[wrong_guess])
print(f"Word to guess: {' '.join(hidden)}")
print(f"Word length: {len(hidden)} letters")

while not game_over:
    # Clean user input
    guessed_char = input("\nEnter your guess: ").strip().lower()

    your_guess.append(guessed_char)

    # Validate input length
    if len(guessed_char) != 1 or not guessed_char.isalpha():
        print("Please enter exactly one alphabetic letter.")
        continue

    # Check the guess directly
    result = util.check_guess(guessed_char, random_word)

    if result:
        # Update hidden word string
        hidden = util.make_visible(result, hidden)
        print(f"your Current Guesses are {your_guess}")
        print(f"\nCorrect! -> {' '.join(hidden)}")

        # Check win condition
        if hidden == random_word:
            print("\n🎉 Congratulations!! You Saved HangMan! 🎉")
            game_over = True
    else:
        wrong_guess += 1
        print(f"\nWrong Guess! Remaning attempts: {max_guess - wrong_guess}")
        print(f"your Current Guesses are {your_guess}")
        print(constant.HANGMAN_STAGES[wrong_guess])
        print(f"Word status: {' '.join(hidden)}")
        print(f"your Current Guesses are {your_guess}")

        # Check lose condition
        if wrong_guess == max_guess:
            print("\n💀 Game Over!!! You Killed HangMan. 💀")
            print(f"The correct word was: {random_word}")
            game_over = True
