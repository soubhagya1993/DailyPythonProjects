# you'll create a simple Python program that calculates a person's age based on their birth year and the current year. 
# This project is a great exercise for working with user input, integers, and basic arithmetic.


import datetime


try:
    birth_year = int(input("Enter your Birth Year: "))
    x = datetime.datetime.now().year  # o/p of datetime.datetime.now() is 2025-04-21 21:06:29.021531
    # x = 2025
    print(f"You are {x - birth_year} years old.")

except Exception as e:
    print(f"Error occured: {e}")