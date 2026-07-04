import game_logic

if __name__ == "__main__":
    while True:
        permission = input(
            "\nDo You Want to Play BlackJack? 'y' for Yes 'n' for No: "
        ).lower()
        if permission == "y":
            game_logic.blackjack_game()
        else:
            print("Thanks for playing!")
            break
