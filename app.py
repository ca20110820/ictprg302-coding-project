import random

from utils import *
from data_processor import DataProcessor

# File Paths for the words
ALL_WORDS = "./word-bank/all_words.txt"
TARGET_WORDS = "./word-bank/target_words.txt"


def main():
    
    target_words = get_word_list(TARGET_WORDS)
    valid_words = get_word_list(ALL_WORDS)
    
    # Generate Random Target Word and Transform/Standardize to Lower Case
    target_word = random.choice(target_words).lower()
    
    # Welcome Message
    welcome_msg = "==============   Welcome to Wordle Console App!!!   =============="
    print("#" * len(welcome_msg))
    print(welcome_msg)
    print("#" * len(welcome_msg))

    user_name = get_user_name()

    attempts = get_difficulty_level()  # Max Number of Attempts
    initial_attempts = attempts

    match attempts:
        case 10:
            difficulty_level = "Easy"
        case 6:
            difficulty_level = "Normal"
        case 4:
            difficulty_level = "Hard"

    # Prompt user if they want to check if their guess word is valid (i.e. word is in ALL_WORDS)
    check_all_words = get_user_bool("yes", "no", "Do you want to check if your guess word exist and valid? (yes/no)")

    # Prompt user if they want to use the advanced scoring algorithm
    use_adv_scoring = get_user_bool("yes", "no", "Do you want to use the advanced scoring algorithm? (yes/no)")

    data_processor = DataProcessor()

    while True:
        print(f"\n\nYou have {attempts} attempts remaining. Good luck!")
        
        user_word = get_user_word(target_word, valid_words, check_all_words=check_all_words)

        scores = get_score_advanced(user_word, target_word) if use_adv_scoring else get_score(user_word, target_word)

        # Print Results
        print()
        print('Guess:\t' + ' '.join([*user_word.upper()]))
        print('Score:\t' + ' '.join(scores))

        attempts -= 1

        # Check if User Won
        if did_user_win(scores):
            game_result = "Won"
            print("\nYou Won!")
            break
        
        # Check if User Lost
        if attempts == 0:
            game_result = "Loss"
            print(f"\nYou Lost!\nThe Correct word is: {target_word}")
            break

    data_processor.write_data(user_name, target_word, difficulty_level, initial_attempts - attempts, game_result)
    data_processor.read_data()
    print(f"\nYour Average Attempts is {data_processor.get_user_avg_attempts(user_name)}")


if __name__ == "__main__":
    main()
