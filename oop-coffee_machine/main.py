from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


termianl_menu = Menu()
terminal_maker = CoffeeMaker()
terminal_machine = MoneyMachine()


is_on = True
while is_on:
    print("Welcome the Terminal Coffee machine")
    options = termianl_menu.get_items()
    choice = input(f"What would you like? ({options})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        terminal_maker.report()
        terminal_machine.report()
    else:
        drink = termianl_menu.find_drink(choice)
        if drink is not None:
            if terminal_maker.is_resource_sufficient(drink):
                terminal_machine.make_payment(drink.cost)
                terminal_maker.make_coffee(drink)
