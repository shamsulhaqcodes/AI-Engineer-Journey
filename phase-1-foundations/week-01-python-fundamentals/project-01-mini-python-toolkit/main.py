# P1: Mini Python Toolkit (menu CLI: 1.Calculator, 2.Grade Checker, 3.Number Guessing Game, 4.Exit)

import random

def get_int(prompt):
    """Keep asking until the user types a valid whole number."""
    while(True):
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calc(n1, n2):
    operation = input("Enter an operation (x, /, +, -): ")
    if(operation == "x"):
        return n1 * n2
    elif(operation == "/"):
        if(n2 == 0):
            print("Error: can't divide by zero.")
            return None
        return n1 / n2
    elif(operation == "+"):
        return n1 + n2
    elif(operation == "-"):
        return n1 - n2
    else:
        print("Invalid operation!")
        return None

def grade_checker(tm, ob):
    if(tm <= 0 or ob < 0 or ob > tm):
        print("Error: marks are invalid.")
        return None, None

    percentage = (ob/tm)*100
    if(percentage >= 90):
        grade = "A+"
    elif(percentage >= 80):
        grade = "A"
    elif(percentage >= 70):
        grade = "B"
    elif(percentage >= 60):
        grade = "C"
    elif(percentage >= 50):
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

def guessing_game():
    count = 0
    secret_num = random.randint(1, 100)

    while(True):
        num = get_int("Guess a number between 1 to 100: ")
        if(num < 1 or num > 100):
            print("Out of range! Try a number from 1 to 100.")
            continue

        count += 1

        if(secret_num == num):
            print(f"You guessed it in {count} attempt(s)!")
            break
        elif(secret_num < num):
            print("Lower number please.")
        else:
            print("Higher number please.")

def exit_program():
    print("Goodbye!")

def toolkit(n):
    if(n == 1):
        num1 = get_int("Enter number 1: ")
        num2 = get_int("Enter number 2: ")
        result = calc(num1, num2)
        if result is not None:
            print(f"Result: {result}")

    elif(n == 2):
        total_marks = get_int("Enter total marks: ")
        obtained_marks = get_int("Enter obtained marks: ")
        percentage, grade = grade_checker(total_marks, obtained_marks)
        if percentage is not None:
            print(f"Percentage: {percentage:.2f}%  |  Grade: {grade}")

    elif(n == 3):
        guessing_game()

    else:
        print("Error: Invalid choice. Please enter 1, 2, 3 or 4.")


while True:
    n = get_int("""
Welcome to Mini Python Toolkit
Choose a command by entering a number:
1 ---> Calculator
2 ---> Grade Checker
3 ---> Number Guessing Game
4 ---> Exit
""")
    if n == 4:
        exit_program()
        break

    toolkit(n)

    