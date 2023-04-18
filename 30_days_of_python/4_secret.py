import random
# 18 April 2023
# Day 4 of #100DaysOfCode and #30DaysOfPython
# Program to simulate guessing secret number

# define secret function
def secret():

    # set secret number and create guess variable
    secret_num = random.sample(range(0,100),1) # choose a number between 0 & 100 and returns it in an array
    secret_num = secret_num[0] # extract the single number from the array
    guess = 0

    # prompt user for guess
    prompt = eval(input("\nCan you guess what the secret number is between 0 and 100? "))
    guess = prompt # set input to guess

    # loop through a while loop for incorrect guess
    while guess != secret_num:
        #get new guess
        guess = eval(input("\nWrong guess. Try again and I will give you a clue: "))
        # set conditionals
        # a lower guess
        if (guess < secret_num):
            print("Your guess is too low!")
        # a higher guess
        elif (guess > secret_num):
            print("Your guess is too high!")

    # for correct guess
    print("\nCongratulations!!! You are spot on!")

# start function
secret()