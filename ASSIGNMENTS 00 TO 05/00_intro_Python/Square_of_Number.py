"""
Program: Square of a Number
---------------------------
This program asks the user for a number, calculates its square,
and prints the result.
"""

def main():
    # Step 1: Prompt the user to input a number
    number = float(input("Type a number to see its square: "))

    # Step 2: Calculate the square of the number
    square = number * number

    # Step 3: Print the result with a formatted message
    print(f"{number} squared is {square}")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
