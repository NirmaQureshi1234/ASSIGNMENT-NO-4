# The age considered as legally adult in the United States
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Prompt the user to input an age
    age = int(input("How old is this person?: "))
    # Call the is_adult function and print the result
    print(is_adult(age))

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
