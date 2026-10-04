# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
