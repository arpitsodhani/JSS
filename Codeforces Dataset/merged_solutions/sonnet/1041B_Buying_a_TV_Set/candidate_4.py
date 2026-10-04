# CLAUSE: setup_environment
from sys import stdin, stdout
from math import gcd

# CLAUSE: solve_logic
def solve(data):
    a, b, x, y = data
    divisor = gcd(x, y)
    scaled = (x // divisor, y // divisor)
    possible = [a // scaled[0], b // scaled[1]]
    return min(possible)

# CLAUSE: finish_program
numbers = tuple(map(int, stdin.buffer.read().split()))
stdout.write(f"{solve(numbers)}\n")
