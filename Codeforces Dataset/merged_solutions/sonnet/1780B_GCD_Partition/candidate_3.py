# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def best_partition_score(items):
    total = sum(items)
    suffix = total
    prefix = 0
    best = 0
    for value in items[:-1]:
        prefix += value
        suffix -= value
        candidate = gcd(prefix, suffix)
        if candidate > best:
            best = candidate
    return best

def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(tokens)
    answers = []
    for _ in range(t):
        n = next(tokens)
        a = [next(tokens) for _ in range(n)]
        answers.append(str(best_partition_score(a)))
    print("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
