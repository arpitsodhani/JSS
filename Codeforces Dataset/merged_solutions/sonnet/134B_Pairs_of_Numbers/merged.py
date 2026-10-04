# Clause setup_environment [Confidence: 0.75]
import sys
from math import gcd


# Clause solve_logic [Confidence: 0.75]
def count_steps(x, y):
    total = 0
    while x != y:
        if x < y:
            x, y = y, x
        take = (x - 1) // y
        x -= take * y
        total += take
    if x == 1:
        return total
    return 10 ** 18

def main():
    n = int(sys.stdin.readline())
    best = 0 if n == 1 else n - 1
    for value in range(1, n):
        if gcd(n, value) == 1:
            got = count_steps(n, value)
            if got < best:
                best = got
    print(best)


# Clause finish_program [Confidence: 0.75]
if __name__ == "__main__":
    main()


