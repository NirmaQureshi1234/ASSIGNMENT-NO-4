"""
Program: Sum of Numbers
------------------------
This program defines a function that takes a list of numbers
and returns the sum of those numbers.
"""

def sum_of_numbers(numbers):
    """
    Function to calculate the sum of a list of numbers.
    Parameters:
    - numbers: A list of numeric values.

    Returns:
    - The sum of the numbers in the list.
    """
    return sum(numbers)

def main():
    """
    Main function to demonstrate the sum_of_numbers function.
    - Creates a list of numbers.
    - Calls the sum_of_numbers function to calculate the sum.
    - Prints the result.
    """
    # Step 1: Example list of numbers
    numbers = [10, 20, 30, 40, 50]

    # Step 2: Call the sum_of_numbers function
    total = sum_of_numbers(numbers)

    # Step 3: Print the result
    print(f"The list of numbers is: {numbers}")
    print(f"The sum of the numbers is: {total}")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
