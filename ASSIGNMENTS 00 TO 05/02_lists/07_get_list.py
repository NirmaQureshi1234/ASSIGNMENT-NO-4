"""
Program: Continuous List Input
------------------------------
This program continuously asks the user to input values
and adds them to a list. The process stops when the user
presses enter without typing anything, and the program
then prints the final list.
"""

def main():
    # Step 1: Initialize an empty list
    values_list = []

    # Step 2: Continuously ask for user input
    while True:
        value = input("Enter a value (press Enter to finish): ")

        # Step 3: Check if the user pressed enter without typing
        if value == "":
            break  # Exit the loop

        # Step 4: Add the value to the list
        values_list.append(value)

    # Step 5: Print the final list
    print("Here's the list:", values_list)

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
