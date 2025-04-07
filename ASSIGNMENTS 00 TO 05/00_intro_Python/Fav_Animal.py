"""
Program: Favorite Animal
------------------------
This program asks the user for their favorite animal
and responds by stating that it is also the program's favorite.
"""

def main():
    # Step 1: Prompt the user to enter their favorite animal
    # The input is stored as a string in the variable 'favorite_animal'
    favorite_animal = input("What's your favorite animal? ")

    # Step 2: Respond with a message that includes the user's input
    # The f-string is used for clean formatting and to insert the user input into the message
    print(f"My favorite animal is also {favorite_animal}!")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
