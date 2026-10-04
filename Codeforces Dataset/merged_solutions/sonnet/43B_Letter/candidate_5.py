# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def cleaned(line):
    return (ch for ch in line if ch != " ")

def main():
    content = sys.stdin.read().splitlines()
    heading = content[0] if content else ""
    text = content[1] if len(content) > 1 else ""

    remaining = defaultdict(int)
    for letter in cleaned(heading):
        remaining[letter] += 1

    answer = "YES"
    for letter in cleaned(text):
        if remaining[letter] == 0:
            answer = "NO"
            break
        remaining[letter] -= 1

    print(answer)

# CLAUSE: finish_program
main()
