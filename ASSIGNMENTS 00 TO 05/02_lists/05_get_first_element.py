"""
Program: Get First Element
--------------------------
This program prompts the user to input elements into a list,
then prints the first element of the list using a helper function.
"""

def get_first_element(lst):
    """
    Prints the first element of the given list.
    Assumes the list is non-empty.
    """
    print(f"The first element in the list is: {lst[0]}")

def main():
    # Step 1: Prompt the user for the number of elements
    num_elements = int(input("How many elements would you like to add to the list? "))

    # Step 2: Initialize an empty list
    my_list = []

    # Step 3: Prompt the user to input each element
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    # Step 4: Call the function to print the first element
    get_first_element(my_list)

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
