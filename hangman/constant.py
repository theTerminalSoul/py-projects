WORDS = [
    "elephant",
    "giraffe",
    "penguin",
    "kangaroo",
    "dolphin",
    "leopard",
    "python",
    "terminal",
    "keyboard",
    "program",
    "website",
    "database",
    "adventure",
    "galaxy",
    "horizon",
    "umbrella",
    "treasure",
    "pyramid",
    "jazz",
    "whiskey",
    "blizzard",
    "matrix",
    "buffalo",
    "phantom",
]

HANGMAN_STAGES = [
    # Stage 0: Initial state (0 wrong guesses)
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    # Stage 1: Head added (1 wrong guess)
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    # Stage 2: Body added (2 wrong guesses)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    # Stage 3: Left Arm added (3 wrong guesses)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    # Stage 4: Right Arm added (4 wrong guesses)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    # Stage 5: Legs added - GAME OVER (5 wrong guesses)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """,
]
