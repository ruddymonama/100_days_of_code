# 13 April 2023
# By Ruddy Starr
# Participating in the 100 Days of Coding
# First 30 days is coding in PYTHON
def _100DaysOfCoding(day):
    #enter day
    if (day < 50):
        if (day < 10):
            print("Only getting started. Let's push !!!")
        elif (day >= 10) and (day < 20): 
            print("Day 10 reached! 20 Here we come, keep pushing!")
        elif (day >= 20) and (day < 30):
            print("Day 20 reached! Almost 30, keep pushing!")
        elif (day >= 30):
            print("Day 30 reached! Done with Python. Onto next language!!! \n")
        print("\nDay 100? Not there YET! Keep pushing.\n")
    
    else:
        if (day >=50) and (day < 100):
            print("Milestone reached. 1 half done, 1 half to go. PUSH NANY PUSH!!")
        else:
            print("Congratulations on reaching day 100!!! #DoHardThings")

_100DaysOfCoding(1) 
