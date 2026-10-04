# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def enough_letters(heading, text):
    counts = {}
    for ch in heading:
        if ch != " ":
            counts[ch] = counts.get(ch, 0) + 1

    needed = {}
    for ch in text:
        if ch != " ":
            needed[ch] = needed.get(ch, 0) + 1

    for ch, amount in needed.items():
        if counts.get(ch, 0) < amount:
            return False
    return True

def main():
    data = sys.stdin.read().splitlines()
    heading = data[0] if data else ""
    text = data[1] if len(data) > 1 else ""
    print("YES" if enough_letters(heading, text) else "NO")

# CLAUSE: finish_program
main()
