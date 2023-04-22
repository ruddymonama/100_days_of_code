import math
# 20 April 2023
# Day 6 of #100DaysOfCode and #30DaysOfPython
# By Ruddy Starr
# Code to convert binary number (base2 - [0,1]) to decimal number (base10 - [0,1,2,3,4,5,6,7,8,9])

def binary_to_decimal():
    print("\n * _ * _ * WELCOME TO BINARY-TO-DECIMAL CONVERTER * _ * _ *")
    # Prompt user to enter base2 binary digits
    binary = input("\nEnter the base2 binary number: ")
    
    # chop down 'bits' string into int characters inside array
    bits = [] # empty array for integer chars
    i = 0 # initialise counter

    while i < (len(binary)): # loop through length of input 'binary' string
        bit = int(binary[i]) # turn each string char into integer char
        bits.append(bit) # add to bits array
        i += 1
    # create decimal var initialised, and calculate decimal value.
    decimal = 0
    j = 0
    while (j < (len(binary))): # conditional to calculate decimal equivalent
        decimal += bits[j]*(2**j) # e.g. 101 = bit[i]x2^i + bit[i+1]x2^(i+1) + bit[i+2]x2^(i+2); i=0
        j += 1
    
    print(f"\nThe binary number {binary} has the decimal equivalent {decimal} .\n") # Print result
binary_to_decimal()