"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

read_target_words_file = open('./word-bank/target_words.txt', 'r')
read_all_words_file = open('./word-bank/all_words.txt', 'r')

TARGET_WORDS = read_target_words_file.read().split()
VALID_WORDS = read_all_words_file.read().split()

MAX_TRIES = 6
ATTEMPTS_TRIED = 0

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


print("You have 6 attempts to guess the correct 5-letter word")
print("Yellow marks correct letters, whereas green marks correct letters in the correct placement")

# TODO: select target word at random from TARGET_WORDS
target_word = random.choice(TARGET_WORDS)
print(target_word)

def display_matching_characters(guess=(), target_word=()):
    result = ''
    # Need to return empty otherwise None appears
    for i in range(len(guess)):
        char = guess[i]
        if char == target_word[i]:
            # Print green if letter placement correct
            result += GREEN + char + RESET
        elif char in target_word:
            # Print yellow if letter correct only
            result += YELLOW + char + RESET
        else:
            result += char
    return result




# TODO: repeat for MAX_TRIES valid attempts
# (start loop)
while True:
    if ATTEMPTS_TRIED < MAX_TRIES:


# TODO: ensure guess in VALID_WORDS
        guess = input("What is your guess?: ").strip().lower()
        if guess in VALID_WORDS:
            ATTEMPTS_TRIED += 1
            if guess == target_word:
                print(GREEN + "Your guess is correct!" + RESET)
            else:
                print(RED + "Your guess is wrong!" + RESET)
                # TODO: provide clues for each character in the guess using your scoring algorithm
                print(display_matching_characters(guess, target_word))
                print(f"You have {ATTEMPTS_TRIED} out of {MAX_TRIES} attempts")
        else:
            print("Invalid word, please enter a 5 letter word")




# (end loop)
print("Game Over")


# NOTES:
# ======
# - Add your own flair to the project
# - You will be required to add and refine features based on changing requirements
# - Ensure your code passes any tests you have defined for it.

# SNIPPETS
# ========
# A set of helpful snippets that may help you meet the project requirements.

def pick_target_word(words=None):
    """returns a random item from the list"""
    words = ['a', 'b', 'c']
    return random.choice(words)


def display_matching_characters(guess=(), target_word=()):
    """Get characters in guess that correspond to characters in the target_word"""
    i = 0
    for char in guess:
        print(char, target_word[i])
        i += 1
# Uncomment to run:
# display_matching_characters()
# print(pick_target_word())
