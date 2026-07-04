import random
import constant


def choose_random_word():
    return random.choice(constant.WORDS).lower()


def make_hidden(word):
    # Cleaner, faster Pythonic way to build a string of underscores
    return "_" * len(word)


def check_guess(char, word):
    indices = []
    for i, c in enumerate(word):
        if c == char:
            indices.append(i)

    # If list is not empty, return data; otherwise return False
    return (char, indices) if indices else False


def make_visible(result, hidden_word):
    if not result:
        return hidden_word

    guessed_char, indices = result
    word_letters = list(hidden_word)

    for index in indices:
        word_letters[index] = guessed_char

    return "".join(word_letters)
