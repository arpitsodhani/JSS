# CLAUSE: setup_environment
import sys

DIGITS = "0123456789"

def response(number, trial):
    bulls = 0
    shared = 0
    present = set(number)
    for index, digit in enumerate(trial):
        if number[index] == digit:
            bulls += 1
        if digit in present:
            shared += 1
    return bulls, shared - bulls

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    if len(data) == 0:
        return

    n = int(data[0])
    records = []
    for i in range(n):
        base = 1 + i * 3
        records.append((data[base], int(data[base + 1]), int(data[base + 2])))

    matches = []
    for a in DIGITS:
        for b in DIGITS:
            if b == a:
                continue
            for c in DIGITS:
                if c == a or c == b:
                    continue
                for d in DIGITS:
                    if d == a or d == b or d == c:
                        continue
                    candidate = a + b + c + d
                    valid = True
                    for guess, bulls, cows in records:
                        if response(candidate, guess) != (bulls, cows):
                            valid = False
                            break
                    if valid:
                        matches.append(candidate)
                        if len(matches) > 1:
                            print("Need more data")
                            return

    if len(matches) == 1:
        print(matches[0])
    else:
        print("Incorrect data")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
