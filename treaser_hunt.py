print("Wellcome To my Treasur Hunt Game")
print("Your Mission is to find the Hidden Treaser")
print(
    """
    You wake up on a jagged, black-sand beach. The last thing you remember was a storm tearing your ship apart. In your hand, you are clutching a 
    waterlogged journal belonging to Captain Avery, a notorious pirate who vanished a century ago.
    Before you lie two paths:
        Path A: Head into the Shrouded Jungle, where glowing fungi illuminate a narrow trail.
        Path B: Follow the Sea Caves along the cliffside, where the tide seems to be rushing out.
    """
)

# Game variables to track items
has_scarab = False
has_spyglass = False
game_over = False

choice1 = input("Do you go to the (A) Shrouded Jungle or (B) Sea Caves? ").upper()

# ================= CHAPTER 2: THE JUNGLE =================
if choice1 == "A":
    print(
        """
        You push through thick vines. The air is heavy. Suddenly, you stumble upon an ancient, moss-covered stone altar. Resting on top of it is a 
        Golden Scarab with emerald eyes.
        """
    )
    choice2 = input(
        "Would you (A) Pick up scarab (B) Leave it and keep walking: "
    ).upper()
    if choice2 == "A":
        print("\nclick......!(sound from some mechanism)")
        print("Congratulation!! you got scarab")
        has_scarab = True
    elif choice2 == "B":
        print("\nYou miss the key but keep walking forward safely.")
    else:
        print("\nInvalid choice! You wander aimlessly.")

# ================= CHAPTER 2: THE CAVES =================
elif choice1 == "B":
    print(
        """
        The caves are dripping and cold. As you walk deeper, you find the remains of an old smuggler's camp. 
        There is a locked iron chest and a skeleton holding a rusty Iron Key.
        """
    )
    choice3 = input(
        "Would you (A) Take key and open chest (B) Ignore and explore deeper tunnel: "
    ).upper()
    if choice3 == "A":
        print("\nCongratulation!! you got the Spyglass and the map fragment!")
        has_spyglass = True
    elif choice3 == "B":
        print(
            "\nohhh..! You Got lost and your health is reduced, but you eventually find a way out."
        )
    else:
        print("\nInvalid choice! You trip in the dark.")
else:
    print("\nYou stand still on the beach until the tide pulls you out to sea.")
    game_over = True


# ================= CHAPTER 3 & 4: THE VOLCANO AND TREASURY =================
if not game_over:
    print(
        """
        ----------------------------------------------------------------------
        CHAPTER 3: THE HEART OF THE ISLAND
        
        Eventually, your path leads you deep into the caldera of a dormant volcano. 
        Before you stands a massive, sealed stone door engraved with a giant serpent.
        """
    )

    # Check if player can open the door based on their route/items
    door_open = False

    if has_scarab:
        print(
            "You notice an empty socket on the serpent's head. You place the Golden Scarab inside."
        )
        print("The machinery clicks, and the giant door slowly grinds open!")
        door_open = True
    elif has_spyglass:
        print(
            "The door is tightly shut. You use your Spyglass to look at the high ceiling runes."
        )
        print("The runes reveal a secret password: 'Avery'.")
        password = input("Enter the password to open the door: ")
        if password.lower() == "avery":
            print("The password is correct! The stone door rumbles open.")
            door_open = True
        else:
            print("Incorrect password! The ceiling collapses on you.")
    else:
        print(
            "The door is locked, and you have no items to open it. You are trapped here forever."
        )

    # Final Room: The Treasure Riddle
    if door_open:
        print(
            """
            ----------------------------------------------------------------------
            CHAPTER 4: THE TREASURE ROOM
            
            The door opens to reveal a chamber filled with piles of gold and a glowing chalice! 
            Suddenly, the ghostly spirit of Captain Avery appears, raising his cutlass!
            
            'Only those worthy may claim the prize,' the ghost booms. 
            'Answer my riddle: What runs, but never walks, has a bed, but never sleeps?'
            """
        )

        riddle_answer = input("Your answer: ").lower()

        if riddle_answer == "river" or riddle_answer == "a river":
            print("\nThe ghost smiles, turns to stardust, and vanishes.")
            print("CONGRATULATIONS! You have claimed the treasure and won the game! 🏆")
        else:
            print("\n'WRONG!' shouts the ghost. He strikes you down with his cutlass.")
            print("GAME OVER. Your soul is trapped on the island forever.")
    else:
        print("GAME OVER. You failed to reach the treasure.")
