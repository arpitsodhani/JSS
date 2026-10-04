# Clause setup_environment [Confidence: 0.20]
import sys

def measure(secret_tuple, guess_tuple):
    bulls = 0
    for i in range(4):
        if secret_tuple[i] == guess_tuple[i]:
            bulls += 1
    cows = len(set(secret_tuple).intersection(guess_tuple)) - bulls
    return bulls, cows

def all_candidates():
    digits = range(10)
    for a in digits:
        for b in digits:
            if b == a:
                continue
            for c in digits:
                if c in (a, b):
                    continue
                for d in digits:
                    if d in (a, b, c):
                        continue
                    yield (a, b, c, d)


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


