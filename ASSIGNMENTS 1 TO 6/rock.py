import random

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play():

    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    

    while user not in ['r', 'p', 's']:
        user = input("Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissor: ")

    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")
    if user == computer:
        return "It's a tie!"
    if is_win(user, computer):
        return 'You win!'
    return 'You lost!'
print(play())