"""
Program: Leap Year Checker
--------------------------
This program reads a year from the user and checks whether it is a leap year or not
using the Gregorian calendar leap year rules.
"""

def main():
    # Prompt the user to input a year
    year = int(input("Enter a year: "))

    # Check leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
