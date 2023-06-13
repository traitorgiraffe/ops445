#!/usr/bin/env python3

# The instructions were confusing, it asked to take an input from a user and
# calculate birth year. Why not ask for the year? What am I calculating? 

import datetime

year = input("Year you were born: ")

def age_calc():
    try:
        clock = datetime.datetime.now().year
        fixedyear = int(year)
        age = clock - fixedyear
        return age
    except ValueError:
        print("It needs to be a number. Try again.")

end = age_calc()
print("You are " + str(end) + " years old.")


# this should be right? 


def helloWorld():
    print("Hello World")

helloWorld()
