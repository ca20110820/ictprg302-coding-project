import random

from utils import (get_word_ls, 
                   get_score, 
                   did_user_win, 
                   get_user_word
                   )

# File Paths for the words
ALL_WORDS = r".\word-bank\all_words.txt"
TARGET_WORDS = r".\word-bank\target_words.txt"

def main():
    global ALL_WORDS
    global TARGET_WORDS
    
    target_words = get_word_ls(TARGET_WORDS)
    valid_words = get_word_ls(ALL_WORDS)
    
    # Generate Random Target Word and Transform/Standardize to Lower Case
    target_word = random.choice(target_words).lower() 
    
    # Target Word Properties
    # target_word_len = len(target_word)
    
    # Welcome Message
    welcome_msg = "=======   Welcome to Wordle Console App!!!   ======="
    print("#"*len(welcome_msg))
    print(welcome_msg)
    print("#"*len(welcome_msg))
    
    trials = 6 # Max Number of Trials
    
    while True:
        print(f"\nYou have {trials} tries remaining. Good luck!")
        
        user_word = get_user_word(target_word, valid_words) # Get User Guess Word
        
        scores = get_score(user_word, target_word) # Evaluate User Score
        
        # Print Results
        print(' '.join([*user_word.upper()]))
        print(' '.join(scores))
        
        # Check if User Won
        if did_user_win(scores):
            print("You Won!")
            break
        
        trials -= 1 # Update/Decrement Trials
        
        # Check if User Lost
        if trials == 0:
            print(f"You Lost!\nThe Correct word is: {target_word}")
            break


if __name__ == "__main__":
    main()