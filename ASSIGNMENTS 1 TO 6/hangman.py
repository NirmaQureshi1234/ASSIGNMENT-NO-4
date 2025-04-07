import random

words = ["apple", "banana", "grapes", "orange", "mango"]
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("_ " * len(word_to_guess))

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
    print(" ".join(display_word))

    if "_" not in display_word:
        print(f"Congratulations! You guessed the word '{word_to_guess}'.")
        break

if "_" in display_word:
    print(f"Game over! The word was '{word_to_guess}'.")
