# CLAUSE: setup_environment
import sys
from itertools import permutations

def score(secret, guess):
    bulls = sum(1 for i in range(4) if secret[i] == guess[i])
    common = sum(1 for ch in guess if ch in secret)
    return bulls, common - bulls

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    guesses = []
    pos = 1
    for _ in range(n):
        guesses.append((tokens[pos], int(tokens[pos + 1]), int(tokens[pos + 2])))
        pos += 3

    found = []
    for digits in permutations("0123456789", 4):
        candidate = "".join(digits)
        if all(score(candidate, guess) == (bulls, cows) for guess, bulls, cows in guesses):
            found.append(candidate)
            if len(found) == 2:
                break

    if not found:
        answer = "Incorrect data"
    elif len(found) == 1:
        answer = found[0]
    else:
        answer = "Need more data"
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
