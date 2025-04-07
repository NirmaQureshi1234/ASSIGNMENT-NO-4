"""
Program: Age-Related Riddle
---------------------------
This program calculates and displays the ages of Anton,
Beth, Chen, Drew, and Ethan based on the given relationships.
"""

def main():
    # Step 1: Define Anton's age
    anton_age = 21

    # Step 2: Calculate Beth's age
    beth_age = anton_age + 6

    # Step 3: Calculate Chen's age
    chen_age = beth_age + 20

    # Step 4: Calculate Drew's age
    drew_age = chen_age + anton_age

    # Step 5: Ethan's age is the same as Chen's age
    ethan_age = chen_age

    # Step 6: Print each person's name and age
    print(f"Anton is {anton_age}")
    print(f"Beth is {beth_age}")
    print(f"Chen is {chen_age}")
    print(f"Drew is {drew_age}")
    print(f"Ethan is {ethan_age}")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
