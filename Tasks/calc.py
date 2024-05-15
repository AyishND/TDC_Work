import sys

def start_calculator():
    while True:
        input_value = input("\nPress Enter to start. ")
        if input_value == '':
            break
        else:
            print("Invalid input! Press Enter to start.")
            continue

def print_ascii():
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |    / _____|  | |
| |___|___|___| |___| | | |  / .'   _|   | || |    / /\ \    | || |    | |       | || |   | .'       | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |   | |        | |
| |___|___|___| |___| | | |   '.___.'    | || | _/ /    \ \_ | || |   _| |__/ |  | || |   '.___.'--  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
    """)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero. ")
        return None
    else:
        return num1 / num2

def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
  
    prev_result = 0  
    while True:
        try:
            num1 = prev_result if prev_result else float(input("\nEnter num1: "))
            print("num1:", num1)

            num2 = float(input("\nEnter num2: "))
            print("num2:", num2)

            operation = input("\nChoose operation (+, -, *, /): ")

            if operation not in operations:
                print("\nInvalid operation!")
                continue
            
            result = operations[operation](num1, num2)
            if result is None:
                continue

            print("\nResult: ", result)

            choice = input("\nDo you want to continue (y/n)? ")
            if choice.lower() != 'y':
                return  
            prev_result = result

        except ValueError:
            print("\nInvalid input! Please enter a valid number ")


print_ascii()
start_calculator()

while True:
    calculator()
    start_calculator()
