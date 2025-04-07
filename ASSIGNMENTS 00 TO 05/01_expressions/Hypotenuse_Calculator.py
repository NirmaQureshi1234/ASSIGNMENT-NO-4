"""
Program: Hypotenuse Calculator
-------------------------------
This program calculates the length of the hypotenuse of a right triangle
using the Pythagorean theorem: BC^2 = AB^2 + AC^2.
"""

import math  # Importing the math module for square root function

def main():
    # Step 1: Prompt the user for the lengths of the two perpendicular sides
    side_ab = float(input("Enter the length of AB: "))
    side_ac = float(input("Enter the length of AC: "))

    # Step 2: Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse_bc = math.sqrt(side_ab**2 + side_ac**2)

    # Step 3: Display the result
    print(f"The length of BC (the hypotenuse) is: {hypotenuse_bc:.2f}")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
