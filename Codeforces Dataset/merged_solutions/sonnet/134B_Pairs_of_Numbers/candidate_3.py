# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def reverse_distance(pair):
    a, b = pair
    moves = 0
    while a > 1 or b > 1:
        if a == b:
            return 10 ** 18
        if a > b:
            jump = (a - 1) // b
            a = a % b
            if a == 0:
                a = b
                jump -= 1
            moves += jump
        else:
            jump = (b - 1) // a
            b = b % a
            if b == 0:
                b = a
                jump -= 1
            moves += jump
    return moves

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    if n == 1:
        sys.stdout.write("0\n")
        return
    answer = n - 1
    candidates = ((n, x) for x in range(1, n) if gcd(n, x) == 1)
    for pair in candidates:
        distance = reverse_distance(pair)
        if distance < answer:
            answer = distance
    sys.stdout.write(str(answer) + "\n")

# CLAUSE: finish_program
main()
