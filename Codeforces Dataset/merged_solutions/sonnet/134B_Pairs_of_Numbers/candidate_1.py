# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

def steps_to_one(a, b):
    steps = 0
    
    while a != b:
        if a < b:
            a, b = b, a
        
        q = (a - 1) // b
        a -= q * b
        steps += q
    
    return steps if a == 1 else 10**18

def main():
    n = int(sys.stdin.readline())
    
    if n == 1:
        print(0)
        return
    
    answer = n - 1
    
    for other in range(1, n):
        if gcd(n, other) == 1:
            answer = min(answer, steps_to_one(n, other))
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
