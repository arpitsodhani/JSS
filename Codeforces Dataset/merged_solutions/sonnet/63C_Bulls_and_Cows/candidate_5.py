# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.read().split()
    if not raw:
        return

    n = int(raw[0])
    constraints = []
    at = 1
    for _ in range(n):
        guess_text = raw[at]
        guess_tuple = tuple(int(ch) for ch in guess_text)
        constraints.append((guess_tuple, int(raw[at + 1]), int(raw[at + 2])))
        at += 3

    answer = None
    many = False

    for candidate in all_candidates():
        for guess_tuple, bulls, cows in constraints:
            if measure(candidate, guess_tuple) != (bulls, cows):
                break
        else:
            if answer is None:
                answer = "".join(str(x) for x in candidate)
            else:
                many = True
                break

    if many:
        print("Need more data")
    elif answer is None:
        print("Incorrect data")
    else:
        print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
