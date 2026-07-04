# Learn about rendomization and python list

import random

options = ["Rock", "Paper", "Scissor"]
print("Wellcome to the Rock Paper Scissor game")
# player input
player_choice = input("Enter your choice (Rock, Paper, Scissor): ").lower()

bot_choice = random.choice(options).lower()
print(f"Bot choose {bot_choice}")

if player_choice == "rock" and bot_choice == "paper":
    print("You Loose")
elif player_choice == "rock" and bot_choice == "scissor":
    print("You Won!!")

elif player_choice == "scissor" and bot_choice == "rock":
    print("You Loose")
elif player_choice == "scissor" and bot_choice == "paper":
    print("You Won!!")

elif player_choice == "paper" and bot_choice == "scissor":
    print("You Loose")
elif player_choice == "paper" and bot_choice == "rock":
    print("You Won!!")

else:
    print("it's Tie")
