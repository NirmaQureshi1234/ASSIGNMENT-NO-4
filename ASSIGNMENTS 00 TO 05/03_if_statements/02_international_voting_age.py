"""
Program: Voting Eligibility Checker
-----------------------------------
This program asks the user for their age and checks if they can vote in the fictional countries of 
Peturksbouipo, Stanlau, and Mayengua, based on their respective voting ages.
"""

def main():
    # Prompt the user for their age
    age = int(input("How old are you? "))

    # Define voting ages for the three fictional countries
    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48

    # Check voting eligibility in each country and print the results
    if age >= peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")

    if age >= stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

    if age >= mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
