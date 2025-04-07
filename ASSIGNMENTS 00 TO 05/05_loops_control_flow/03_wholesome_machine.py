def main():
    affirmation = "I am capable of doing anything I put my mind to."
    while True:
        user_input = input(f"Please type the following affirmation: {affirmation} ")
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm, that was not the affirmation. Please try again.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
