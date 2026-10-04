# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def main():
    text = sys.stdin.buffer.read()
    a, b, x, y = (int(part) for part in text.split())
    g = math.gcd(x, y)
    unit_width = x // g
    unit_height = y // g
    by_width = a // unit_width
    by_height = b // unit_height
    if by_width <= by_height:
        answer = by_width
    else:
        answer = by_height

# CLAUSE: finish_program
    sys.stdout.write(str(answer) + "\n")

main()
