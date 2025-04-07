"""
Program: Double Each Element in a List
--------------------------------------
This program takes a list of numbers and doubles each element in the list.
"""

def double_elements(numbers):
    """
    Function to double each element in a list of numbers.
    Parameters:
    - numbers: A list of numeric values.

    Returns:
    - A new list with each element doubled.
    """
    return [number * 2 for number in numbers]

def main():
    """
    Main function to demonstrate the double_elements function.
    - Creates a list of numbers.
    - Calls the double_elements function to double each element.
    - Prints the original and modified lists.
    """
    # Step 1: Example list of numbers
    numbers = [1, 2, 3, 4]

    # Step 2: Call the double_elements function
    doubled_numbers = double_elements(numbers)

    # Step 3: Print the results
    print(f"Original list of numbers: {numbers}")
    print(f"List after doubling each element: {doubled_numbers}")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
