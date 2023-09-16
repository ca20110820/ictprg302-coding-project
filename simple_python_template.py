"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 6

# TODO: select target word at random from TARGET_WORDS
target_word = 'hello'

# TODO: repeat for MAX_TRIES valid attempts
# (start loop)
guess = input("Enter guess? ")

# TODO: ensure guess in VALID_WORDS

# TODO: provide clues for each character in the guess using your scoring algorithm
if guess == target_word:
    print("Your guess is correct!")
else:
    print("Your guess is wrong!")

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


def display_matching_characters(guess='hello', target_word='world'):
    """Get characters in guess that correspond to characters in the target_word"""
    i = 0
    for char in guess:
        print(char, target_word[i])
        i += 1

# Uncomment to run:
# display_matching_characters()
# print(pick_target_word())
