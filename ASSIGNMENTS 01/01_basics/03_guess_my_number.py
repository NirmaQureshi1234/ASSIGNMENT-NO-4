import random  # Importing the random module to generate a random number

def main():
    # Generate a random number between 0 and 99
    target_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    # Initialize a variable to store the user's guess
    guess = -1  # Starting with a value outside the valid range

    # Loop until the user guesses the correct number
    while guess != target_number:
        # Prompt the user to enter a guess
        guess = int(input("Enter a guess: "))
        
        # Provide feedback on the user's guess
        if guess > target_number:
            print("Your guess is too high.")
        elif guess < target_number:
            print("Your guess is too low.")
        else:
            print(f"Congrats! The number was: {target_number}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
