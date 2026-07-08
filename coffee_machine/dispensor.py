import util
import menu


def brew_coffee(drink_type, user_money):
    if not util.is_sufficient(drink_type):
        print("Sorry, there are not enough ingredients to make this drink.")
        return

    drink_price = menu.MENU[drink_type]["price"]

    if util.valid_amount(user_money, drink_price):
        change = util.calculate_money(drink_type, user_money)

        util.utilis_item(drink_type)

        print(f"\n☕ Here is your {drink_type.capitalize()}. Enjoy!!!")
        if change and change > 0:
            print(f"💵 Here is your change: ₹{change}")

    else:
        print(
            f"You can't do that! ₹{user_money} is not enough. A {drink_type} costs ₹{drink_price}."
        )
