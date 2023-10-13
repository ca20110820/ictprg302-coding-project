import random

from utils import (get_word_list,
                   get_user_bool,
                   get_score,
                   get_score_advanced,
                   did_user_win,
                   get_user_word
                   )

# File Paths for the words
ALL_WORDS = r".\word-bank\all_words.txt"
TARGET_WORDS = r".\word-bank\target_words.txt"


def main():
    
    target_words = get_word_list(TARGET_WORDS)
    valid_words = get_word_list(ALL_WORDS)
    
    # Generate Random Target Word and Transform/Standardize to Lower Case
    target_word = random.choice(target_words).lower()
    
    # Welcome Message
    welcome_msg = "=======   Welcome to Wordle Console App!!!   ======="
    print("#" * len(welcome_msg))
    print(welcome_msg)
    print("#" * len(welcome_msg))
    
    attempts = 6  # Max Number of Trials

    # Prompt user if they want to check if their guess word is valid (i.e. word is in ALL_WORDS)
    check_all_words = get_user_bool("yes", "no", "Do you want to check if your guess word exist and valid? (yes/no)")

    # Prompt user if they want to use the advanced scoring algorithm
    use_adv_scoring = get_user_bool("yes", "no", "Do you want to use the advanced scoring algorithm? (yes/no)")

    while True:
        print(f"\n\nYou have {attempts} attempts remaining. Good luck!")
        
        user_word = get_user_word(target_word, valid_words, check_all_words=check_all_words)

        if use_adv_scoring:
            scores = get_score_advanced(user_word, target_word)
        else:
            scores = get_score(user_word, target_word)
        
        # Print Results
        print()
        print('Guess:\t' + ' '.join([*user_word.upper()]))
        print('Score:\t' + ' '.join(scores))
        
        # Check if User Won
        if did_user_win(scores):
            print("\nYou Won!")
            break
        
        attempts -= 1
        
        # Check if User Lost
        if attempts == 0:
            print(f"\nYou Lost!\nThe Correct word is: {target_word}")
            break


if __name__ == "__main__":
    main()
