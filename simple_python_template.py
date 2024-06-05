"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal
import random

read_target_words_file = open('./word-bank/target_words.txt', 'r')
read_all_words_file = open('./word-bank/all_words.txt', 'r')

TARGET_WORDS = read_target_words_file.read().split()
VALID_WORDS = read_all_words_file.read().split()




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




# Recording user into log
user_log = "user_log.txt"




def user_details_log(username, target_word):
    log_header = f"\nUsername: {username} \nTarget word: {target_word} \n"
    # Need utf-8 to fix unicode error
    record_header = open('user_log.txt', 'a', encoding="utf-8")
    record_header.write(log_header)

def user_guess(guess, result):
    log_instance = f"Guess: {guess}  Score: {result}\n"
    record_guess = open('user_log.txt', 'a', encoding="utf-8")
    record_guess.write(log_instance)

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





def wordle_mechanics():
    # Enter the user's name
    username = input("Enter your username: ").strip()
    play_again = True

    while play_again:
        # TODO: select target word at random from TARGET_WORDS
        target_word = random.choice(TARGET_WORDS)
        MAX_TRIES = 6
        ATTEMPTS_TRIED = 0

        # user_details_log prints out log_header once
        user_details_log(username, target_word)

        while ATTEMPTS_TRIED < MAX_TRIES:
            guess = input("What is your guess?: ").strip().lower()
            if guess in VALID_WORDS:
                ATTEMPTS_TRIED += 1
                if guess == target_word:
                    result = '🟩' * len(guess)
                    print(f"{guess}")
                    print(result)
                    print("Your guess is correct!")
                    user_guess(guess, result)
                    print("Would you like to play again?")
                    break

                else:
                    result = display_matching_characters(guess, target_word)
                    print(f"{guess}")
                    print(result)
                    print(f"You have {ATTEMPTS_TRIED} out of {MAX_TRIES} attempts")
                    user_guess(guess, result)

            else:
                print("Invalid word, please enter a 5 letter word")
        # (end loop)
        else:
            print("Game Over")
    # TODO: repeat for MAX_TRIES valid attempts
    # Ask user to play again
        play_again_input = input("Would you like to play again?(Y/N): ").lower()
        play_again = (play_again_input == 'y')
wordle_mechanics()




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
