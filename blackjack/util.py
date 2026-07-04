import constant
import random


def calculate_hand(hand):
    total = 0
    ace_count = 0

    # Calculate the initial total (Aces as 11)
    for card in hand:
        for key in constant.CARD_VALUE:
            if card == key:
                total += constant.CARD_VALUE[key]
                if card == "A":
                    ace_count += 1

    # If busted, convert Aces from 11 to 1 one by one
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def check_for_ace(hand):
    for card in hand:
        if card == "A":
            return True
    return False


def deal_card():
    """Returns a random card from the card list."""
    return random.choice(constant.CARD_LIST)
