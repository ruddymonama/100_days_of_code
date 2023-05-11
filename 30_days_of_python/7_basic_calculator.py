# 21 April 2023
# Day 7 of #100DaysOfCode and #30DaysOfPython
# By Ruddy Starr
# Code to simulate basic calculator by asking input of 2 numbers
# from user and using add(), subract(), multiply(), divide() functions

# addition
def add(a,b):
    sum = a + b
    print(f"\nAddition: {a} + {b} = {sum}\n")

# subtraction
def subtract(a,b):
    diff = a - b
    print(f"Subtraction: {a} - {b} = {diff}\n")

# multiplication
def multiply(a,b):
    prod = a*b
    print(f"Multiplication: {a} x {b} = {prod}\n")

# division
def divide(a,b):
    if b == 0:
        print(f"Division: Error, division by 0! {a} / 0 = UNDEFINED") # prompt when dividing by 0.
    else:
        quot = a/b
        print(f"Division: {a} / {b} = {quot}\n")

# Main basic calulcator
def basic_calculator():
    print("!!! Welcome to the Basic Calculator V1.0 !!!")
    # prompt user to enter 2 numbers of interest
    num1 = eval(input("\nEnter your first number of choice: "))
    num2 = eval(input("Enter second number of choice: "))

    # calculate add, subtract, multiply and divide operations.
    add(num1,num2)
    subtract(num1,num2)
    multiply(num1,num2)
    divide(num1,num2)

basic_calculator()

    