"""
Program: Division Result and Remainder
--------------------------------------
This program asks the user for two integers, divides the first number by the second,
and prints both the result of the division and the remainder.
"""

def main():
    # Step 1: Prompt the user for the first number (dividend)
    dividend = int(input("Please enter an integer to be divided: "))

    # Step 2: Prompt the user for the second number (divisor)
    divisor = int(input("Please enter an integer to divide by: "))

    # Step 3: Calculate the quotient and remainder
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulo operation

    # Step 4: Display the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
