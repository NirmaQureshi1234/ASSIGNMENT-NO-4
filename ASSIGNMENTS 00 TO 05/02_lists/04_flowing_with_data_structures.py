"""
Program: Mutability Example
----------------------------
This program demonstrates the concept of mutability by modifying
a list within a helper function without returning it.
"""

def add_three_copies(lst, data):
    """
    Adds three copies of 'data' to the given list 'lst'.
    Since lists are mutable, changes will persist outside this function.
    """
    for _ in range(3):
        lst.append(data)

def main():
    # Step 1: Get input from the user
    message = input("Enter a message to copy: ")

    # Step 2: Initialize an empty list
    my_list = []
    print("List before:", my_list)

    # Step 3: Add three copies of the message to the list
    add_three_copies(my_list, message)

    # Step 4: Print the list after modification
    print("List after:", my_list)

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
