print("Print Welcome to the Calculator")


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


done_calculation = False

while not done_calculation:
    num1 = int(input("Enter Number one: "))
    operator = input("Enter Operator (+, -, *, /)")
    num2 = int(input("Enter Number Two: "))

    match operator:
        case "+":
            print(add(num1, num2))
        case "-":
            print(sub(num1, num2))
        case "*":
            print(mul(num1, num2))
        case "/":
            print(divide(num1, num2))
        case _:
            print("Kindly enter valid operator")

    done = input("Enter 'y' for continue & 'n' for end")
    if done == "n":
        done_calculation = True
