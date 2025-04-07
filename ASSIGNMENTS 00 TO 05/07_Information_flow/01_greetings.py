def greet(name):
    # Print the greeting message with the provided name
    print(f"Greetings {name}!")

def main():
    # Prompt the user to input their name
    name = input("What's your name? ")
    # Call the greet function with the inputted name
    greet(name)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
