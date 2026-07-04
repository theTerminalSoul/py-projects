print("Welcome to the Blind auction")

current_bidings = {}

is_over = False

while not is_over:
    name = input("Please Enter Your Name: ")
    bid_amount = int(input("Please Enter Bid Amount: "))

    current_bidings[name] = bid_amount

    more = input("anyone want to bid? yes or no")
    if more == "yes":
        continue
    else:
        is_over = True

high_bid_payer = None
biding_amount = 0
for key in current_bidings:
    if current_bidings[key] > biding_amount:
        high_bid_payer = key
        biding_amount = current_bidings[key]

print(f"Highest bidig is by {high_bid_payer} of biding amount {biding_amount}")
