from typing import List, Dict

def get_word_ls(path) -> List[str]:
    """ Returns a list of words from a given filepath """
    with open(path, 'r') as file:
        word_ls = [w.strip() for w in file.readlines()]
    return word_ls

def get_user_word(target_word:str, valid_words:List[str], check_all_words:bool=False) -> str:
    """ Prompts User for Valid Guess Word and Returns that Word """
    
    # Prompt the user for their guess word and check if valid
    target_word_len = len(target_word)
    print(f"What is your {target_word_len}-letter guess? (Cheat: {target_word})")
    while True:
        try:
            user_word = input(">>> ") # User's Guess
            user_word = user_word.lower() # Standardized to Lowercase
            user_word = user_word.strip().replace(" ", "")  # Strip the User Guess Word string
            
            # conditions = len(user_word) > target_word_len or len(user_word) < target_word_len or user_word not in valid_words
            if len(user_word) > target_word_len:
                print(f"The number of letters cannot exceed the number of letters in the target word ({target_word_len} letters)! Please try again ...")
                continue
            if len(user_word) < target_word_len:
                print(f"The number of letters cannot be less than the number of letters in the target word ({target_word_len} letters)! Please try again ...")
                continue
            if check_all_words:
                if user_word not in valid_words:
                    print(f"Your word is meaningless! Please try again ...")
                    continue

            return user_word

        except Exception as err:
            print(err)
            continue

def count_letters(word:str) -> Dict[str, int]:
    """ Returns a Dictionary of the Letter/Character Counts in the given Word """
    
    out_dict = {}
    
    for l in word:
        if l not in out_dict.keys():
            out_dict[l] = 1
        else:
            out_dict[l] += 1
            
    return out_dict

def num_letter_in_word(letter:str, word:str) -> int:
    """ Returns the number of occurences of a letter in a given word """
    assert len(letter) == 1, "letter must be a string with length 1"
    return count_letters(word).get(letter, 0)

def num_hits(guess:str, target:str) -> int:
    """ Returns the Number of Hits """
    assert len(guess) == len(target), "Length of Target and Guess Strings must be Equal"
    return len([tup for tup in zip(guess, target) if tup[0] == tup[1]])

def num_bullets(letter:str, guess:str, target:str) -> int:
    """ Returns the (initial static) number of Bullets """

    n_letter_guess = num_letter_in_word(letter, guess)
    n_letter_target = num_letter_in_word(letter, target)

    if n_letter_target >= n_letter_guess:
        return 0
    else:
        return n_letter_target - num_hits(guess, target)

def is_cheat_at_letter(user_word:str, target_word:str, letter:str) -> bool:
    guess = user_word.lower().strip()
    target = target_word.lower().strip()
    l = letter.lower().strip()

    assert len(guess) == len(target), "The length of the User and Target Words must be equal"
    assert len(l) == 1

    if num_letter_in_word(l, guess) > num_letter_in_word(l, target) and (l in guess) and (l in target):
        return True
    return False

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

    score_ls = [None] * word_len  # Initialize Scores

    # if all([num_letter_in_word(l, target_word)>=num_letter_in_word(l, user_word) for l in user_word if l in target_word]):
    #     print(f"Simple Scoring is same as Advanced Scoring |\tGuess: {user_word}\tTarget: {target_word}")
    #     return get_score(user_word, target_word)

    # Fill up `+`s
    for i in range(word_len):
        if user_word[i] == target_word[i]:
            score_ls[i] = "+"

    # Fill up `-`s
    for i in range(word_len):
        if score_ls[i] is None and user_word[i] not in target_word:  # Only consider None
            score_ls[i] = "-"

    if all([(score is not None) for score in score_ls]):  # Return if all are filled
        return score_ls

    # Create a (Initial) Dictionary for the Number of "Bullets", which may updated for each iteration
    num_bullets_dict = {}
    for l in user_word:
        num_bullets_dict[l] = num_bullets(l, user_word, target_word)

    # Fill up `?`s
    for i in range(word_len):
        if score_ls[i] is None:
            # Get Letters
            target_letter = target_word[i]
            user_letter = user_word[i]

            assert user_letter in target_word, "Logic Error!!!"
            assert target_letter != user_letter, "Both Target and User Letters are Equal!!!"

            # Get Counts
            user_letter_count = num_letter_in_word(user_letter, user_word)
            user_letter_count_target = num_letter_in_word(user_letter, target_word)  # Count of User Guess Letter in Target Word.

            assert user_letter_count_target > 0, "User letter does not exist in Target Word!!!"

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
                    if num_bullets_dict[user_letter] > 0:  # There's still some "bullets"
                        score_ls[i] = "?"
                        num_bullets_dict[user_letter] -= 1  # Update the number of bullets for the letter by decrementing
                    else:
                        score_ls[i] = "-"
                else:
                    score_ls[i] = "?"

    return score_ls

def did_user_win(score_ls) -> bool:
    """ Returns True of the User Correctly Guessed the Target Word, Otherwise False """
    return all([(True if score=="+" else False) for score in score_ls])


__all__ = ["get_word_ls", "get_user_word", "get_score", "get_score_advanced", "did_user_win", "is_cheat_at_letter"]


if __name__ == "__main__":
    test_user = "LLLLUL"
    test_target = "LELILL"

    test_scores = get_score_advanced(test_user, test_target)

    print(' '.join([*test_user.upper()]), "\tGuess")
    print(' '.join([*test_target.upper()]), "\tTarget")
    print(' '.join(test_scores))

    print(num_hits("a", "aaade", "aacyh"))
    print(num_letter_in_word("e", "eeesdfsdf"))