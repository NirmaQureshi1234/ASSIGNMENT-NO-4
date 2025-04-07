"""
Program: Mad Libs Sentence Generator
------------------------------------
This program prompts the user for an adjective, a noun, and a verb,
then constructs a fun sentence using those inputs.
"""

def main():
    # Constant for the beginning of the sentence
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Prompt the user for inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct and print the full sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print(sentence)

# This provided line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
