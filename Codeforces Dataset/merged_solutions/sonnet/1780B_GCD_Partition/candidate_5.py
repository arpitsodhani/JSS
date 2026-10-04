# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def solve_case(a):
    total = sum(a)
    running = 0
    candidates = []
    for value in a:
        running += value
        candidates.append(running)
    best = 0
    for left_sum in candidates[:-1]:
        g = gcd(left_sum, total - left_sum)
        best = g if g > best else best
    return best

def main():
    numbers = [int(x) for x in sys.stdin.buffer.read().split()]
    t = numbers[0]
    cursor = 1
    lines = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        lines.append(str(solve_case(numbers[cursor:cursor + n])))
        cursor += n
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
