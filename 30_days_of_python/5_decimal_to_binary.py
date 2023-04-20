# 19 April 2023
# Day 5 of #100DaysOfCode and #30DaysOfPython
# By Ruddy Starr
# Code to convert decimal number (base10 - [0,1,2,3,4,5,6,7,8,9]) to a binary number (base2 - [0,1])


def decimal_to_binary(): # the method is based on repeated division by 2
    print("\n * _ * _ * WELCOME TO DECIMAL-TO-BINARY CONVERTER * _ * _ *")
    #prompt user to enter base10 decimal:
    num = eval(input("\nEnter the base10 decimal: "))
    # initalise counter and empty bit and remainder arrays
    i = 0
    bit = []
    num0 = num
    while (num0>0):
        rem = num0%2 # floor divide the number to find the remainder
        bit.append(rem) # the remainder is the bit item at index i and so add it to bit array
        num0 //= 2 # find the new quotient by integer divideing num0
        i += 1 # increment counter
    
    b_it = "" #initalise b_it string
    for j in range(-len(bit),0): # loop through array size of bit array backwards
        b_it += str(bit[j]) # extract bit array item as string and concatenate to b_it  string variable
        j += 1 # increment loop counter

    print(f"The decimal(base10) number {num} is represented in binary(base2) as {b_it[::-1]}\n")

decimal_to_binary()
