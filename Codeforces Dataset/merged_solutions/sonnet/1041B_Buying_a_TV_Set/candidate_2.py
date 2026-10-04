# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def main():
    a, b, x, y = map(int, sys.stdin.buffer.read().split())
    d = gcd(x, y)
    x //= d
    y //= d
    ans = min(a // x, b // y)

# CLAUSE: finish_program
    sys.stdout.write(str(ans))

main()
