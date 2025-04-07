def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Double the value and print until the value is 100 or greater
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")  # Print the doubled value with a space
    
    print()  # Add a newline at the end

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
