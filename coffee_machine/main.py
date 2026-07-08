import util
import dispensor
import menu

machine_on = True

while machine_on:
    print("\n=== Welcome to the Terminal Coffee Machine ===")
    util.display_option()
    print("Special commands: 'report' to view stock | 'off' to shutdown")

    user_choice = input("\nWhat would you like? ").strip().lower()

    if user_choice == "off":
        print("Shutting down... Goodbye!")
        machine_on = False
    elif user_choice == "report":
        util.print_report()
    elif user_choice in menu.MENU:
        try:
            inserted_money = int(input("Please insert money (₹): "))
            dispensor.brew_coffee(user_choice, inserted_money)
        except ValueError:
            print("Invalid payment type. Please enter a valid number.")
    else:
        print("Invalid selection. Please choose from the menu or use a command.")
