from typing import List, Dict

def get_word_ls(path):
    """ Returns a list of words from a given filepath """
    with open(path, 'r') as file:
        word_ls = [w.strip() for w in file.readlines()]
    return word_ls

def get_user_word(target_word:str, valid_words:list) -> str:
    """ Prompts User for Valid Guess Word and Returns that Word """
    
    # Prompt the user for their guess word and check if valid
    target_word_len = len(target_word)
    print(f"What is your {target_word_len}-letter guess? (Cheat: {target_word})")
    while True:
        try:
            user_word = input(">> ") # User's Guess
            user_word = user_word.lower() # Transform/Standardized to Lowercase
            
            conditions = len(user_word) > target_word_len or len(user_word) < target_word_len #or user_word not in valid_words
            
            if conditions:
                print("Invalid Guess! Please try again ...")
                continue
            return user_word
        except Exception as err:
            print(err)
            continue

def count_letters(word:str) -> Dict[str, int]:
    """ Returns a Dictionary of the Letter/Character Counts in the given Word """
    
    out_dict = {}
    
    for c in word:
        if c not in out_dict.keys():
            out_dict[c] = 1
        else:
            out_dict[c] += 1
            
    return out_dict

def get_score(user_word:str, target_word:str) -> List[str]:
    """ Returns the List of Scores """
    
    # Standardized to Lower Case
    user_word = user_word.lower()
    target_word = target_word.lower()
    
    word_len = len(target_word) # Length of Target/User Word. Don't want to recalculate.
    
    assert len(user_word) == word_len, "The length of the User and Target Words must be equal"
    
    score_ls = []  # Initialize Scores
    
    for i in range(word_len):
        if user_word[i] == target_word[i]:
            score_ls += ["+"]
        elif user_word[i] in target_word:
            score_ls += ["?"]
        else:
            score_ls += ["-"]
    
    return score_ls

def get_score_edge_cases(user_word:str, target_word:str) -> List[str]:
    # TODO: Implement Scoring Algorithm that includes edge cases.

    # Standardized to Lower Case
    user_word = user_word.lower()
    target_word = target_word.lower()

    word_len = len(target_word)  # Length of Target/User Word. Don't want to recalculate.

    # Check if there are repetitions in letters
    is_repeated_user_letter = any([count > 1 for _, count in count_letters(user_word).items()])
    is_repeated_target_letter = any([count > 1 for _, count in count_letters(target_word).items()])

    score_ls = [None]*word_len  # Initialize Scores

    # Use get_score if there are not repeated letters in either user or target words
    if not (is_repeated_user_letter or is_repeated_target_letter):
        return get_score(user_word, target_word)

    plus_indexes = []  # List to keep track of indexes with +'s

    # Fill up +'s
    for i in range(word_len):
        if user_word[i] == target_word[i]:
            score_ls[i] = "+"
            plus_indexes.append(i)

    # To Get List of Indexes of Correct Letters Guessed
    # Most of the time, this will either be empty or one element, but there could be repetitions.
    get_plus_idx = lambda letter: [idx for idx in plus_indexes if user_word[idx] == letter]

    # Fill up -'s
    for i in range(word_len):
        if score_ls[i] is None and user_word[i] not in target_word:  # Only consider None
            score_ls[i] = "-"

    if all([(score is not None) for score in score_ls]):  # Return if all are filled
        return score_ls

    # Fill up ?'s
    user_counts:Dict[str, int] = count_letters(user_word)
    target_counts:Dict[str, int] = count_letters(target_word)
    for i in range(word_len):
        if score_ls[i] is None:
            # Get Letters
            target_letter = target_word[i]
            user_letter = user_word[i]

            assert user_letter in target_word, "Logic Error!!!"
            assert target_letter != user_letter, "Both Target and User Letters are Equal!!!"

            # Get Counts
            target_letter_count = target_counts[target_letter]
            user_letter_count = user_counts[user_letter]
            user_letter_count_target = target_counts[user_letter]  # Count of User Guess Letter in Target Word

            num_correct_guesses = len(get_plus_idx(user_letter))  # Count how many times we previously guessed the letter

            num_question_marks = len([score for score in score_ls if score == "?"])

            # Scoring Criterions
            if user_letter_count == 1 and user_letter_count_target == 1:  # Letter exist but
                score_ls[i] = "?"
            elif user_letter_count > 1 and user_letter_count_target == 1:
                score_ls[i] = "-"
            elif user_letter_count == 1 and user_letter_count_target > 1:
                score_ls[i] = "?"
            else:   # user_letter_count > 1 and user_letter_count_target > 1
                if user_letter_count > user_letter_count_target:
                    # score_ls[i] = "-"
                    if num_correct_guesses < user_letter_count_target:
                        score_ls[i] = "?"
                    else:
                        score_ls[i] = "-"
                elif user_letter_count < user_letter_count_target:
                    score_ls[i] = "?"
                else:  # Both Equal and More than one repetition of the letter
                    if num_correct_guesses == 0:
                        score_ls[i] = "?"
                    else:
                        if num_correct_guesses < user_letter_count_target:
                            score_ls[i] = "?"
                        else:
                            score_ls[i] = "-"

    return score_ls

def did_user_win(score_ls) -> bool:
    """ Returns True of the User Correctly Guessed the Target Word, Otherwise False """
    return all([(True if score=="+" else False) for score in score_ls])


__all__ = ["get_word_ls", "get_user_word", "get_score", "did_user_win"]


if __name__ == "__main__":
    # test_user = "llllp"
    # test_target = "wolll"

    test_user = "llrdll"
    test_target = "hellol"

    test_scores = get_score_edge_cases(test_user, test_target)

    print(' '.join([*test_user.upper()]), "\tGuess")
    print(' '.join([*test_target.upper()]), "\tTarget")
    print(' '.join(test_scores))