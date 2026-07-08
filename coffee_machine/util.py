import menu


def display_option():
    print("Availble option for you:")
    for option, data in menu.MENU.items():
        print(f"{option} ₹ {data['price']}")


def is_sufficient(drink):
    required_ingrediant = menu.MENU[drink]

    for item in required_ingrediant:
        if item == "price":
            continue

        if required_ingrediant[item] > menu.STOCK[item]:
            return False

    return True


def utilis_item(drink):
    required_ingrediant = menu.MENU[drink]

    for item in required_ingrediant:
        if item == "price":
            continue

        menu.STOCK[item] -= required_ingrediant[item]


def calculate_money(drink, amount):
    required_ingrediant = menu.MENU[drink]
    drink_amount = required_ingrediant["price"]
    if valid_amount(amount, drink_amount):
        if drink_amount == amount:
            menu.STOCK["price"] += drink_amount
        elif drink_amount < amount:
            change = amount - drink_amount
            menu.STOCK["price"] += drink_amount
            return change
    else:
        print("Your Amount is not Valid")


def valid_amount(user_amount, drink_amount):
    if user_amount < drink_amount:
        return False
    else:
        return True


# function to print the stock
def print_report():
    print("\n--- Current Machine Stock ---")
    print(f"Water:  {menu.STOCK['water']}ml")
    print(f"Milk:   {menu.STOCK['milk']}ml")
    print(f"Coffee: {menu.STOCK['coffee']}g")
    print(f"money Collected: {menu.STOCK['price']}")
    print("-----------------------------\n")
