import random
import constant
import util
import art


def play_turn(player_hand):
    """Handles the player's turn (Hitting or Standing).

    Returns:
        int: The final score of the player after their turn.
    """
    while True:
        hit_or_stand = input("Do you want to Hit ('h') Or Stand ('s'): ").lower()

        if hit_or_stand == "h":
            player_hand.append(deal_card())
            player_hand_val = util.calculate_hand(player_hand)
            print(f"Your Hand is: {player_hand}")
            print(f"Your hand value is: {player_hand_val}")

            if player_hand_val > 21:
                return player_hand_val  # Busted

        elif hit_or_stand == "s":
            return util.calculate_hand(player_hand)


def play_dealer_turn(dealers_hand, hole_card):
    """Handles the dealer's turn after the player stands."""
    dealers_hand.append(hole_card)
    dealer_hand_val = util.calculate_hand(dealers_hand)
    print(f"\nDealer reveals hole card. Dealer's hand is: {dealers_hand}")
    print(f"Dealer's hand value is: {dealer_hand_val}")

    # Dealer hits until they reach at least 17
    while dealer_hand_val < 17:
        dealers_hand.append(deal_card())
        dealer_hand_val = util.calculate_hand(dealers_hand)
        print(f"Dealer hits. Dealers hand is: {dealers_hand}")
        print(f"Dealer's hand value is: {dealer_hand_val}")

    return dealer_hand_val


def determine_winner(player_score, dealer_score):
    """Compares scores and prints the final outcome."""
    print("\n--- Final Results ---")
    print(f"Your Final Score: {player_score}")
    print(f"Dealer's Final Score: {dealer_score}")

    if dealer_score > 21:
        print("Dealer Busted!!! You Win 🏆")
    elif player_score > dealer_score:
        print("Player Won!!! 🏆")
    elif dealer_score > player_score:
        print("Dealer Win 🎰")
    else:
        print("It's a Tie 🤝")


def blackjack_game():
    """Main game loop for a single round of Blackjack."""
    print(art.art)

    # Initial Deal
    player_hand = [deal_card(), deal_card()]
    dealers_hand = [deal_card()]
    hole_card = deal_card()  # Kept hidden until player stands

    print(f"Your Hand is: {player_hand}")
    player_score = util.calculate_hand(player_hand)
    print(f"Your hand value is: {player_score}")

    print(f"Dealer's visible hand is: {dealers_hand}")

    # Instant Natural Blackjack Check
    if player_score == 21:
        print("Blackjack! You Won!!! 🏆")
        return

    # Player Turn
    player_score = play_turn(player_hand)
    if player_score > 21:
        print("You Busted!! Dealer Wins 🎰")
        return

    # Dealer Turn
    dealer_score = play_dealer_turn(dealers_hand, hole_card)

    # Evaluate Game
    determine_winner(player_score, dealer_score)


def deal_card():
    """Returns a random card from the card list."""
    return random.choice(constant.CARD_LIST)


def play_turn(player_hand):
    """Handles the player's turn (Hitting or Standing).

    Returns:
        int: The final score of the player after their turn.
    """
    while True:
        hit_or_stand = input("Do you want to Hit ('h') Or Stand ('s'): ").lower()

        if hit_or_stand == "h":
            player_hand.append(deal_card())
            player_hand_val = util.calculate_hand(player_hand)
            print(f"Your Hand is: {player_hand}")
            print(f"Your hand value is: {player_hand_val}")

            if player_hand_val > 21:
                return player_hand_val  # Busted

        elif hit_or_stand == "s":
            return util.calculate_hand(player_hand)


def play_dealer_turn(dealers_hand, hole_card):
    """Handles the dealer's turn after the player stands."""
    dealers_hand.append(hole_card)
    dealer_hand_val = util.calculate_hand(dealers_hand)
    print(f"\nDealer reveals hole card. Dealer's hand is: {dealers_hand}")
    print(f"Dealer's hand value is: {dealer_hand_val}")

    # Dealer hits until they reach at least 17
    while dealer_hand_val < 17:
        dealers_hand.append(deal_card())
        dealer_hand_val = util.calculate_hand(dealers_hand)
        print(f"Dealer hits. Dealers hand is: {dealers_hand}")
        print(f"Dealer's hand value is: {dealer_hand_val}")

    return dealer_hand_val


def determine_winner(player_score, dealer_score):
    """Compares scores and prints the final outcome."""
    print("\n--- Final Results ---")
    print(f"Your Final Score: {player_score}")
    print(f"Dealer's Final Score: {dealer_score}")

    if dealer_score > 21:
        print("Dealer Busted!!! You Win 🏆")
    elif player_score > dealer_score:
        print("Player Won!!! 🏆")
    elif dealer_score > player_score:
        print("Dealer Win 🎰")
    else:
        print("It's a Tie 🤝")


def blackjack_game():
    """Main game loop for a single round of Blackjack."""
    print(art.art)

    # Initial Deal
    player_hand = [deal_card(), deal_card()]
    dealers_hand = [deal_card()]
    hole_card = deal_card()  # Kept hidden until player stands

    print(f"Your Hand is: {player_hand}")
    player_score = util.calculate_hand(player_hand)
    print(f"Your hand value is: {player_score}")

    print(f"Dealer's visible hand is: {dealers_hand}")

    # Instant Natural Blackjack Check
    if player_score == 21:
        print("Blackjack! You Won!!! 🏆")
        return

    # Player Turn
    player_score = play_turn(player_hand)
    if player_score > 21:
        print("You Busted!! Dealer Wins 🎰")
        return

    # Dealer Turn
    dealer_score = play_dealer_turn(dealers_hand, hole_card)

    # Evaluate Game
    determine_winner(player_score, dealer_score)
