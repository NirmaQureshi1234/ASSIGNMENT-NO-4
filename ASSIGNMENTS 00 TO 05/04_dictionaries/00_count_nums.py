"""
Program: Count Occurrences in a List
------------------------------------
This program asks the user to enter numbers repeatedly, counts the occurrences of each number, 
and prints the result.
"""

def main():
    # Create an empty list to store numbers
    numbers = []
    
    # Continuously prompt the user for numbers
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        # Break the loop if the user presses Enter without typing anything
        if user_input == "":
            break
        
        # Add the entered number to the list
        numbers.append(int(user_input))
    
    # Create an empty dictionary to count occurrences
    occurrences = {}
    
    # Count the occurrences of each number
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    
    # Print the results
    for number, count in occurrences.items():
        print(f"{number} appears {count} times.")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
