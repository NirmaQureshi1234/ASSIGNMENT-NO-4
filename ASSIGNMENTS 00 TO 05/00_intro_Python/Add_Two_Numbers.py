"""
Program: Add Two Numbers
------------------------
This program takes two integers as input from the user,
calculates their sum, and prints the result.
"""

def main():
    # Step 1: Briefly explain what the program does
    print("Welcome! This program adds two numbers.")

    # Step 2: Prompt the user to input the first number
    # The input function takes the input as a string, so we convert it to an integer
    first_number = int(input("Please enter the first number: "))

    # Step 3: Prompt the user to input the second number
    # Again, the input is converted to an integer
    second_number = int(input("Please enter the second number: "))

    # Step 4: Calculate the sum of the two numbers
    # Use the "+" operator to add the two numbers
    total_sum = first_number + second_number

    # Step 5: Display the result with a clear message
    print(f"The sum of {first_number} and {second_number} is: {total_sum}")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
