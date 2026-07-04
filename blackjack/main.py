import random
import constant
import util
import art


permission = input("Do You Want to Play BlackJack 'y' for Yes 'n' for No:").lower()
if permission == "y":
    print(art.art)

    game_on = True
    while game_on:
        player_hand = []
        dealers_hand = []
        player_hand_val = 0
        dealer_hand_val = 0
        for _ in range(2):
            player_card = random.choice(constant.CARD_LIST)
            player_hand.append(player_card)

        print(f"Your Hand is:{player_hand}")
        player_hand_val = util.calculate_hand(player_hand)
        print(f"Your hand value is:{player_hand_val}")

        # Choosing dealers hand
        dealers_card = random.choice(constant.CARD_LIST)
        hole_card = random.choice(constant.CARD_LIST)
        dealers_hand.append(dealers_card)
        print(f"dealears hand is:{dealers_hand}")
        dealer_hand_val = util.calculate_hand(dealers_hand)
        print(f"dealers hand value is:{dealer_hand_val}")

        # calculate next moves
        if player_hand_val == 21:
            print("You Won!!!")
            game_on = False

        print("You can hit or stand")
        ask_again = True
        while ask_again:
            hit_or_stand = input("DO you want to Hit Or Stand:").lower()

            if hit_or_stand == "h":
                extra_card = random.choice(constant.CARD_LIST)
                player_hand.append(extra_card)
                print(f"Your Hand is:{player_hand}")

                # util.calculate_hand automatically manages Aces dynamically
                player_hand_val = util.calculate_hand(player_hand)
                print(f"Your hand value is:{player_hand_val}")

                # Clean bust check
                if player_hand_val > 21:
                    print("You Busted!! Dealer Win")
                    ask_again = False
                    game_on = False

            elif hit_or_stand == "s":
                dealers_hand.append(hole_card)
                print(f"dealears hand is:{dealers_hand}")
                dealer_hand_val = util.calculate_hand(dealers_hand)
                print(f"dealers hand value is:{dealer_hand_val}")

                if dealer_hand_val == 21:
                    print("Dealer Won!!")
                    ask_again = False
                    game_on = False

                # Dealer logic automatically respects the new Ace handling inside util
                while dealer_hand_val < 17:
                    extra_card = random.choice(constant.CARD_LIST)
                    dealers_hand.append(extra_card)
                    dealer_hand_val = util.calculate_hand(dealers_hand)
                    print(f"Dealers hand is: {dealers_hand}")

                if dealer_hand_val > 21:
                    print("Dealear Busted!!! You Win")
                    ask_again = False
                    game_on = False
                elif dealer_hand_val > player_hand_val and dealer_hand_val < 21:
                    print("Dealer Win")
                    ask_again = False
                    game_on = False
                elif dealer_hand_val == player_hand_val:
                    print("Its Tie")
                    ask_again = False
                    game_on = False
                else:
                    print("Player Won!!!")
                    ask_again = False
                    game_on = False
