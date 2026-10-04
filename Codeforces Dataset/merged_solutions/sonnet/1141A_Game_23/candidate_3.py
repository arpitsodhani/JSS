# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def reduce_factor(value, factor):
    count = 0
    while value > 1 and value % factor == 0:
        value //= factor
        count += 1
    return value, count

def main():
    n, m = [int(x) for x in sys.stdin.buffer.read().split()]
    answer = -1
    if m % n == 0:
        ratio, threes = reduce_factor(m // n, 3)
        ratio, twos = reduce_factor(ratio, 2)
        if ratio == 1:
            answer = threes + twos
    print(answer)

# CLAUSE: finish_program
main()
