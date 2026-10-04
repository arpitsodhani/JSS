# CLAUSE: setup_environment
import sys
from math import pi, tan

# CLAUSE: solve_logic
def polygon_square_side(n):
    return 1.0 / tan(pi / (2 * n))

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    results = ["%.9f" % polygon_square_side(n) for n in values[1:]]

# CLAUSE: finish_program
    print("\n".join(results))

main()
