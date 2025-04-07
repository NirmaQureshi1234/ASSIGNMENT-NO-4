"""
Program: Feet to Inches Converter
---------------------------------
This program converts a measurement in feet to inches.
There are 12 inches in one foot.
"""

def main():
    # Step 1: Prompt the user to enter a measurement in feet
    feet = float(input("Enter measurement in feet: "))

    # Step 2: Convert feet to inches
    inches = feet * 12

    # Step 3: Display the result
    print(f"{feet} feet is equal to {inches} inches.")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
