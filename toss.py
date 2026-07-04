import random

choice = input("(H) Heads or (T) Tail")
print("Flip the Coin")

result = None
random_number = int(random.random() * 10)
if random_number <= 5:
    print("its Head")
else:
    print("its Tail")
