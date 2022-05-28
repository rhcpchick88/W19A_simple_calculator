from secrets import choice
# Importing my math modules
from math_functions.addition import add
from math_functions.division import div
from math_functions.multiplication import multi
from math_functions.subtraction import sub

# Custom exception

class CalculatorInputError(Exception):
    pass

# printing separately so it appears nicely in terminal"

print("This is the best calculator, please choose from these options to begin!")
print("1: Addition")
print("2: Subtraction")
print("3: Division")
print("4: Multiplication")

# setting choice variable to whatever the user inputs

choice = input("Input the number corresponding with your selection:")

# converting the input from a string to an integer

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))


# if else, to go through each selection and do the correct function associated with it
try:
    if choice == "1":
        result=add(num1, num2)
    elif choice=="2":
        result =sub(num1, num2)
    elif choice=="3":
        result=div(num1, num2)
    elif choice=="4":
        result=multi(num1, num2)
    else:
        # call my custom exception error in if-else block
        raise CalculatorInputError 
    print(result)
# say what happens in the exception 
except CalculatorInputError:
    print("Invalid input")
