"""
Program: Get Last Element
--------------------------
This program prompts the user to input elements into a list,
then prints the last element of the list using a helper function.
"""

def get_last_element(lst):
    """
    Prints the last element of the given list.
    Assumes the list is non-empty.
    """
    print(f"The last element in the list is: {lst[-1]}")

def main():
    # Step 1: Prompt the user for the number of elements
    num_elements = int(input("How many elements would you like to add to the list? "))

    # Step 2: Initialize an empty list
    my_list = []

    # Step 3: Prompt the user to input each element
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    # Step 4: Call the function to print the last element
    get_last_element(my_list)

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
