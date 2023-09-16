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

# DEPRECATED
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
    
    word_len = len(target_word) # Length of Target/User Word. Dont want to recalculate.
    
    assert len(user_word) == word_len, "The length of the User and Target Words must be equal"
    
    score_ls = [] # Initialize Scores
    
    for i in range(word_len):
        if user_word[i] == target_word[i]:
            score_ls += ["+"]
        elif user_word[i] in target_word:
            score_ls += ["?"]
        else:
            score_ls += ["-"]
    
    return score_ls

def did_user_win(score_ls) -> bool:
    """ Returns True of the User Correctly Guessed the Target Word, Otherwise False """
    return all([(True if score=="+" else False) for score in score_ls])


__all__ = ["get_word_ls", "get_score", "did_user_win"]