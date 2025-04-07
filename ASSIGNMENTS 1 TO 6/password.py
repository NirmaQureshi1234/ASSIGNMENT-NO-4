import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))

if length < 4:
    print("Password length should be at least 4 characters.")
else:
    print("Generated Password:", generate_password(length))
