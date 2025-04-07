"""
Program: Height Checker for Ride Eligibility
--------------------------------------------
This program asks the user how tall they are and checks if they meet the minimum height
requirement of 50 units to ride. The program stops when the user provides no input.
"""

def main():
    MIN_HEIGHT = 50  # Minimum height requirement
    
    while True:
        # Ask the user for their height
        height = input("How tall are you? (Press Enter to stop): ")

        # Stop the loop if no height is entered
        if not height:
            print("Goodbye!")
            break

        # Convert the height to an integer and check eligibility
        height = int(height)
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
