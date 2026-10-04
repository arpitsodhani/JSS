# CLAUSE: setup_environment
import sys
from itertools import permutations

def parse_input(items):
    total = int(items[0])
    parsed = []
    cursor = 1
    for _ in range(total):
        guess = items[cursor]
        parsed.append((guess, set(guess), int(items[cursor + 1]), int(items[cursor + 2])))
        cursor += 3
    return parsed

def fits(candidate, candidate_set, facts):
    for guess, guess_set, bulls_needed, cows_needed in facts:
        bulls = 0
        for i in range(4):
            if candidate[i] == guess[i]:
                bulls += 1
        common = len(candidate_set & guess_set)
        if bulls != bulls_needed or common - bulls != cows_needed:
            return False
    return True

# CLAUSE: solve_logic
def main():
    items = sys.stdin.read().split()
    if not items:
        return

    facts = parse_input(items)
    unique_answer = None
    count = 0

    for perm in permutations("0123456789", 4):
        candidate = "".join(perm)
        if fits(candidate, set(candidate), facts):
            count += 1
            if count == 1:
                unique_answer = candidate
            else:
                break

    if count == 0:
        sys.stdout.write("Incorrect data\n")
    elif count == 1:
        sys.stdout.write(unique_answer + "\n")
    else:
        sys.stdout.write("Need more data\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
