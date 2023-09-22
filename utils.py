from typing import List, Dict

def get_word_ls(path) -> List[str]:
    """ Returns a list of words from a given filepath """
    with open(path, 'r') as file:
        word_ls = [w.strip() for w in file.readlines()]
    return word_ls

def get_user_word(target_word:str, valid_words:List[str]) -> str:
    """ Prompts User for Valid Guess Word and Returns that Word """
    
    # Prompt the user for their guess word and check if valid
    target_word_len = len(target_word)
    print(f"What is your {target_word_len}-letter guess? (Cheat: {target_word})")
    while True:
        try:
            user_word = input(">> ") # User's Guess
            user_word = user_word.lower() # Standardized to Lowercase
            user_word = user_word.strip().replace(" ", "")  # Strip the User Guess Word string
            
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

def get_score_advanced(user_word:str, target_word:str) -> List[str]:

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

    num_hits:Dict[str,int] = {}  # Number of "hits" or `+`s for a letter

    # Fill up +'s
    for i in range(word_len):
        if user_word[i] == target_word[i]:
            score_ls[i] = "+"

            if user_word[i] in num_hits.keys():  # If letter already exists in num_hits dictionary
                num_hits[user_word[i]] += 1
            else:  # If letter does not exist in num_hits dictionary
                num_hits[user_word[i]] = 1

            plus_indexes.append(i)

    # To Get List of Indexes of Correct Letters Guessed
    # Most of the time, this will either be empty or one element, but there could be repetitions.
    get_plus_idx = lambda letter: [idx for idx in plus_indexes if user_word[idx] == letter]  # Corresponds to number of "hits"

    # Fill up -'s
    for i in range(word_len):
        if score_ls[i] is None and user_word[i] not in target_word:  # Only consider None
            score_ls[i] = "-"

    if all([(score is not None) for score in score_ls]):  # Return if all are filled
        return score_ls

    # Create a Dictionary for the Count of each letter in a Word (User and Target Words)
    user_counts: Dict[str, int] = count_letters(user_word)
    target_counts: Dict[str, int] = count_letters(target_word)

    # Create a (Initial) Dictionary for the Number of "Bullets", which may updated for each iteration
    # num_bullets = {l:target_counts.get(l, 0) - num_hits.get(l,0) for l in user_word}
    num_bullets = {}
    for l in user_word:
        if target_counts.get(l, 0) >= num_hits.get(l, 0):
            num_bullets[l] = target_counts.get(l, 0) - num_hits.get(l, 0)

    # Fill up ?'s
    for i in range(word_len):
        if score_ls[i] is None:
            # Get Letters
            target_letter = target_word[i]
            user_letter = user_word[i]

            assert user_letter in target_word, "Logic Error!!!"
            assert target_letter != user_letter, "Both Target and User Letters are Equal!!!"

            # Get Counts
            # target_letter_count = target_counts[target_letter]
            user_letter_count = user_counts[user_letter]
            # user_letter_count_target = target_counts[user_letter]  # Count of User Guess Letter in Target Word.
            user_letter_count_target = target_counts.get(user_letter, 0)  # Count of User Guess Letter in Target Word.

            assert user_letter_count_target > 0, "User letter does not exist in Target Word!!!"

            # num_correct_guesses = len(get_plus_idx(user_letter))  # Count how many times we previously guessed the letter, i.e. Number of "hits" for a letter
            # num_question_marks = len([score for score in score_ls if score == "?"])  # `?` in total, not for a specific letter

            # Scoring Criterions
            if user_letter_count == 1 and user_letter_count_target == 1:  # Letter exist but in wrong index
                score_ls[i] = "?"
            elif user_letter_count > 1 and user_letter_count_target == 1:  # The "Cheating" Scenario
                score_ls[i] = "-"
            elif user_letter_count == 1 and user_letter_count_target > 1:
                score_ls[i] = "?"
            else:   # user_letter_count > 1 and user_letter_count_target > 1
                if user_letter_count > user_letter_count_target:  # The "Cheating" Scenario
                    # Check how many bullets left
                    if num_bullets[user_letter] > 0:  # There's still some "bullets"
                        # Update the number of bullets for the letter
                        score_ls[i] = "?"
                        num_bullets[user_letter] -= 1  # Update the number of bullets for the letter
                    else:
                        score_ls[i] = "-"
                elif user_letter_count < user_letter_count_target:
                    score_ls[i] = "?"
                else:  # Both Equal and More than one repetition of the letter
                    # Check how many bullets left
                    if num_bullets[user_letter] > 0:  # There's still some "bullets"
                        # Update the number of bullets for the letter
                        score_ls[i] = "?"
                        num_bullets[user_letter] -= 1  # Update the number of bullets for the letter
                    else:
                        score_ls[i] = "-"

    return score_ls

def did_user_win(score_ls) -> bool:
    """ Returns True of the User Correctly Guessed the Target Word, Otherwise False """
    return all([(True if score=="+" else False) for score in score_ls])


__all__ = ["get_word_ls", "get_user_word", "get_score", "did_user_win"]


if __name__ == "__main__":
    test_user = "LLLLUL"
    test_target = "LELILL"

    test_scores = get_score_advanced(test_user, test_target)

    print(' '.join([*test_user.upper()]), "\tGuess")
    print(' '.join([*test_target.upper()]), "\tTarget")
    print(' '.join(test_scores))