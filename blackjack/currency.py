def get_initial_deposit():
    """Prompts the user to make an initial deposit to start the game."""
    while True:
        deposit = int(input("Enter your initial deposit amount to buy-in: ₹"))
        if deposit <= 0:
            print("Deposit must be greater than zero.")
        else:
            print(f"Deposit successful! Your starting balance is: ₹{deposit}\n")
            return deposit


def place_bet(balance):
    print(f"\nYour current balance is: ₹{balance}")
    bet = int(input("Enter your bet amount: ₹"))
    if bet <= 0:
        print("Bet must be greater than zero.")
    elif bet > balance:
        print("Insufficient funds! You cannot bet more than you have.")
    else:
        return bet


def handle_payout(balance, bet, outcome):
    if outcome == "win":
        new_balance = balance + bet
        print(f"You won ₹{bet}! New balance: ₹{new_balance}")
        return new_balance
    elif outcome == "lose":
        new_balance = balance - bet
        print(f"You lost ₹{bet}. New balance: ₹{new_balance}")
        return new_balance
    elif outcome == "tie":
        print(f"It's a tie. Your bet of ₹{bet} was returned. Balance: ₹{balance}")
        return balance
