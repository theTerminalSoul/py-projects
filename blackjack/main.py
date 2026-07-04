import currency
import game_logic

if __name__ == "__main__":
    print("!!!Welcome to the CLI casino!!!")

    # Initial buy-in
    current_balance = currency.get_initial_deposit()

    while True:
        if current_balance is None:
            print("System Error: Balance was lost. Resetting wallet to safe default.")
            current_balance = 500

        # Check if the player is out of money
        if current_balance <= 0:
            print("\nYou ran out of Money!")
            answer = input(
                "Would you like to deposit more money to keep playing? ('y'/'n'): "
            ).lower()

            if answer == "y":
                current_balance = currency.get_initial_deposit()
                continue  # Restart loop check with the fresh balance
            else:
                print("Exiting table... Thanks for playing!")
                break

        # Ask to play a round
        permission = input(
            "\nDo You Want to Play BlackJack? 'y' for Yes 'n' for No: "
        ).lower()

        if permission == "y":
            # Run the round and catch the updated balance
            new_balance = game_logic.blackjack_game(current_balance)

            # Defensive Check: Ensure game_logic didn't accidentally pass back a None
            if new_balance is not None:
                current_balance = new_balance
            else:
                print(
                    "Error returning value from table. Your previous balance has been preserved."
                )

        elif permission == "n":
            print(f"\nThanks for playing! You walked away with: ₹{current_balance}")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
