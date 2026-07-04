# Capital and Small Alphabets
import random

alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# Numbers (as strings)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Common Special Characters
special_characters = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    ";",
    ":",
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
]

print("Wellcomt to the Password Generator")
number_of_alphet = int(input("How many alphabets you want in your Password:\n"))
number_of_number = int(input("How many numbers you want in your Password:\n"))
number_of_spe_char = int(
    input("How many special character you want in your Password:\n")
)


master_list = []
# for random alphbet
for _ in range(number_of_alphet):
    random_alphbet = random.choice(alphabets)
    master_list.append(random_alphbet)

# for random number
for _ in range(number_of_number):
    random_number = random.choice(numbers)
    master_list.append(random_number)

for _ in range(number_of_spe_char):
    random_spe_char = random.choice(special_characters)
    master_list.append(random_spe_char)

print(master_list)
random.shuffle(master_list)

password = "".join(master_list)

print(f"Your Password is: {password}")
