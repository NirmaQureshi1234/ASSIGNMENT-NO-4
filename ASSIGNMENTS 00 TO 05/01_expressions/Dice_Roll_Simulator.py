"""
Program: Dice Roll Simulator
----------------------------
This program simulates rolling two dice three times
and prints the results of each roll.
"""

import random  # Importing the random module to generate random numbers

def main():
    # Step 1: Simulate rolling the dice three times
    for roll in range(1, 4):  # Looping 3 times for three rolls
        die1 = random.randint(1, 6)  # Generate a random number between 1 and 6 for die 1
        die2 = random.randint(1, 6)  # Generate a random number between 1 and 6 for die 2

        # Step 2: Print the result of each roll
        print(f"Roll {roll}: Die 1 = {die1}, Die 2 = {die2}")

    # Demonstrating scope: 'die1' and 'die2' are local variables within the loop
    # They cannot be accessed outside this block.

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
