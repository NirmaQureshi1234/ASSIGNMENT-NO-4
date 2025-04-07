"""
Program: Print 10 Random Numbers
--------------------------------
This program generates and prints 10 random numbers in the range 1 to 100.
"""

import random  # Importing the random module to generate random numbers

def main():
    # Generate and print 10 random numbers
    for _ in range(10):  # Loop 10 times
        number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(number, end=' ')  # Print the number with a space, keeping everything on the same line
    print()  # Move to the next line after printing all numbers

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
