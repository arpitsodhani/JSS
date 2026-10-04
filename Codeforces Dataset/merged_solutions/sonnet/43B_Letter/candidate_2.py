# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    lines = sys.stdin.read().splitlines()
    heading = lines[0] if lines else ""
    text = lines[1] if len(lines) > 1 else ""

    available = Counter(ch for ch in heading if ch != " ")

    for ch in text:
        if ch != " ":
            if available[ch] <= 0:
                print("NO")
                return
            available[ch] -= 1

    print("YES")

# CLAUSE: finish_program
main()
