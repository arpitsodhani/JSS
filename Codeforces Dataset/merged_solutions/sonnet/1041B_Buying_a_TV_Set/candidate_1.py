# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

def main():
    a, b, x, y = map(int, sys.stdin.read().split())
    
    g = gcd(x, y)
    x //= g
    y //= g
    
    print(min(a // x, b // y))

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
