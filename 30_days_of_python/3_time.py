# 17 April 2023
# Day 3 of #100DaysOfCode and #30DaysOfPython
# Program to convert an  amount in minutes into an equivalent amount 
# of days, hours and minutes

# create time function
def time():

    # prompt user for input
    prompt = eval(input("\nEnter the quantity in minutes: "))

    # time conversions. 1 day = 24 hours, 1 hour = 60 minutes
    minutes = prompt%60 # divide prompt minutes by 60: the remainder is the num of minutes
    hours = prompt//60 # divide the minutes by 60: the quotient is the num of hours
    days = hours//24 # divide the hours by 24: the quotient is the num of days
    hours = hours%24 # divide the quotient by 24: the remainder is the desired hours

    # print out conversion
    print("\nThe number of days is {0}, the number of hours is {1} and the number of minutes is {2}.".format(days, hours, minutes))

# start function
time()
