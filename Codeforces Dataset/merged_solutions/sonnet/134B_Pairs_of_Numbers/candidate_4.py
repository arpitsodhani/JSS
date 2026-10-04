# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def needed_steps(a, b):
    result = 0
    while True:
        if a == b:
            return result if a == 1 else 10 ** 18
        if a < b:
            a, b = b, a
        amount, left = divmod(a - 1, b)
        a -= amount * b
        result += amount

def main():
    n = int(sys.stdin.readline().strip())
    if n < 2:
        print(0)
    else:
        values = []
        for second in range(1, n):
            if gcd(n, second) == 1:
                values.append(needed_steps(n, second))
        print(min(values))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
