import random

low = 1
high = 10

print("Think of a number between 1 and 10, and I will try to guess it!")

while True:
    guess = random.randint(low, high)
    print(f"Is your number {guess}?")

    feedback = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if correct: ").lower()

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f"Finally, I guessed your number {guess} correctly")
        break
    else:
        print("Invalid input Please enter 'h' (too high) 'l' (too low) or 'c' (correct).")
