import random

def main():
    # Generate a random number between 0 and 99
    target_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Prompt the user to guess a number
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue
        
        # Check if the guess is too high, too low, or correct
        if guess > target_number:
            print("Your guess is too high.")
        elif guess < target_number:
            print("Your guess is too low.")
        else:
            print(f"Congrats! The number was: {target_number}")
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
