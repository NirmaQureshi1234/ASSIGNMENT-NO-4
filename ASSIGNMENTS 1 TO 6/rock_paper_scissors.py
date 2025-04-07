import random

choices = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!")
while True:
    user_choice = input("Type rock, paper, or scissors (or 'q' to quit): ").lower()

    if user_choice == "q":
        print("Goodbye! Thanks for playing.")
        break

    if user_choice not in choices:
        print("That's not a valid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
