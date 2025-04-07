"""
Program: Triangle Perimeter Calculator
---------------------------------------
This program prompts the user to enter the lengths of each side of a triangle,
calculates the perimeter, and prints the result.
"""

def main():
    # Step 1: Prompt the user to enter the lengths of each side of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Step 2: Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3

    # Step 3: Print the calculated perimeter
    print(f"The perimeter of the triangle is {perimeter}")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
