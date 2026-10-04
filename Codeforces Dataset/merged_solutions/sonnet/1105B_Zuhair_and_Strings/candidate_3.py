# CLAUSE: setup_environment
import sys
from itertools import groupby

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    k = int(data[1])
    s = data[2]
    best = 0
    for _, group in groupby(s):
        pieces = sum(1 for _ in group) // k
        if pieces > best:
            best = pieces

# CLAUSE: finish_program
    print(best)

if __name__ == "__main__":
    main()
