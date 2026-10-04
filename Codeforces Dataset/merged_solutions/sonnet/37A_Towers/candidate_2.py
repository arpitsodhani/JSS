# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    bars = values[1:1 + n]
    freq = Counter(bars)
    tallest = max(freq.values())
    towers = len(freq)

# CLAUSE: finish_program
    sys.stdout.write(str(tallest) + " " + str(towers))

if __name__ == "__main__":
    main()
