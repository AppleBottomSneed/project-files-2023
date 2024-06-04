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

#Colour shortcuts
#RED = "\033[91m"
#GREEN = "\033[92m"
#YELLOW = "\033[93m"
#RESET = "\033[0m"

MISS = 0  # _-.: letter not found ⬜
MISSPLACED = 1  # O, ?: letter in wrong place 🟨
EXACT = 2  # X, +: right letter, right place 🟩


print("You have 6 attempts to guess the correct 5-letter word")
print("Yellow marks correct letters, whereas green marks correct letters in the correct placement")

# TODO: select target word at random from TARGET_WORDS
target_word = random.choice(TARGET_WORDS)

# Uncomment to pin target word
print(target_word)

# Enter the user's name
username = input("Enter your username: ").strip()

# Recording user into log
user_log = "user_log.txt"

def user_details_log(username, guess, result, target_word=()):
    log_instance = f"{username}: Target word:{target_word} \n Guess:{guess}, Score: {result}"
    # Need utf-8 to fix unicode error
    record_instance = open('user_log.txt', 'a', encoding="utf-8")
    record_instance.write(log_instance)


def display_matching_characters(guess=(), target_word=()):
    result = ['⬜'] * len(target_word)
    # Empty boxes as per length of target_word
    target_char_count = {}

    # Green per correct letter placement
    exact_matches = [False] * len(guess)
    for i in range(len(target_word)):
        if target_word[i] == guess[i]:
            result[i] = '🟩'
            exact_matches[i] = True

     # Counts non-exact letters
    for i in range(len(target_word)):
        # If +1 then is correct
        if not exact_matches[i]:
            if target_word[i] in target_char_count:
                target_char_count[target_word[i]] += 1
            else:
                target_char_count[target_word[i]] = 1

    # Yellow per correct letter not placement
    for i in range(len(guess)):
        if not exact_matches[i] and guess[i] in target_char_count and target_char_count[guess[i]] > 0:
            result[i] = '🟨'
            target_char_count[guess[i]] -= 1



    return ''.join(result)

# TODO: repeat for MAX_TRIES valid attempts
# (start loop)
class WordleMechanics:
    while ATTEMPTS_TRIED < MAX_TRIES:
        guess = input("What is your guess?: ").strip().lower()
        if guess in VALID_WORDS:
            ATTEMPTS_TRIED += 1
            if guess == target_word:
                result = '🟩' * len(guess)  # All correct
                print(f"{guess}")
                print(result)
                print("Your guess is correct!")
                user_details_log(username, guess, result, target_word)
                break
            else:
                result = display_matching_characters(guess, target_word)
                print(f"{guess}")
                print(result)
                print(f"You have {ATTEMPTS_TRIED} out of {MAX_TRIES} attempts")
                user_details_log(username, guess, result, target_word)

        else:
            print("Invalid word, please enter a 5 letter word")
    # (end loop)
    else:
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
