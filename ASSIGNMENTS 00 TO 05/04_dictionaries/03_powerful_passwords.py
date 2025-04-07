import hashlib

# Function to hash the password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check login credentials
def login(email, password_to_check, stored_logins):
    """
    This function checks if the hashed password for the given email matches
    the stored hashed password in the stored_logins dictionary.

    Args:
        email (str): The email address to check.
        password_to_check (str): The password to verify.
        stored_logins (dict): A dictionary of emails and their hashed passwords.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    # Hash the input password
    hashed_password = hash_password(password_to_check)
    # Check if the email exists in stored_logins and the hashed password matches
    return stored_logins.get(email) == hashed_password

def main():
    # Example stored logins with email and hashed passwords
    stored_logins = {
        "user1@example.com": hash_password("password123"),
        "user2@example.com": hash_password("mysecurepassword"),
        "user3@example.com": hash_password("1234abcd")
    }

    # Example test cases
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
