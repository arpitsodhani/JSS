# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def measure(first, second):
    steps = 0
    stack = [[first, second]]
    while stack:
        a, b = stack.pop()
        if a == b:
            if a == 1:
                return steps
            return 10 ** 18
        if a < b:
            a, b = b, a
        delta = (a - 1) // b
        steps += delta
        stack.append([a - delta * b, b])
    return 10 ** 18

def main():
    raw = sys.stdin.read().strip()
    n = int(raw)
    answer = 0
    if n != 1:
        answer = n - 1
        other = 1
        while other < n:
            if gcd(n, other) == 1:
                current = measure(n, other)
                answer = current if current < answer else answer
            other += 1
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
