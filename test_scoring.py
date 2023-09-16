from utils import get_score

if __name__ == "__main__":
    guess = "hello"
    targets = ["hello", "crane", "hzzzz", "zhzzz", "HELLO", "world"]
    
    for target in targets:
        print(guess, "\t Guess")
        print(target, "\t Target")
        result = ''.join(get_score(guess, target))
        print(result)
        print()