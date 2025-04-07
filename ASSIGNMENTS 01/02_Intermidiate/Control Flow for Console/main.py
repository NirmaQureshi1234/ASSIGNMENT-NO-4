import random

def main():
    print("Welcome to the High-Low Game!")
    num_rounds = int(input("How many rounds would you like to play? "))
    player_score = 0

    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number: {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()

        if (guess == "higher" and player_number > computer_number) or \
           (guess == "lower" and player_number < computer_number):
            print(f"Correct! The computer's number was {computer_number}.")
            player_score += 1
        else:
            print(f"Wrong! The computer's number was {computer_number}.")

    print("\n--- Game Over ---")
    print(f"Your final score: {player_score}/{num_rounds}")
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
