# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right

def load():
    items = list(map(int, sys.stdin.buffer.read().split()))
    return items[0], items[1], items[2:]

# CLAUSE: solve_logic
def can_make(divisor, values, k):
    start = 0
    size = len(values)
    multiple = divisor
    largest = values[-1]
    while multiple <= largest:
        right = multiple + k
        cap = multiple + divisor - 1
        if right > cap:
            right = cap
        left_index = bisect_left(values, multiple, start)
        right_index = bisect_right(values, right, left_index)
        if left_index != start:
            return False
        start = right_index
        if start == size:
            return True
        multiple += divisor
    return start == size

def main():
    n, k, values = load()
    values.sort()
    limit = values[0]
    for divisor in range(limit, 0, -1):
        if can_make(divisor, values, k):
            sys.stdout.write(str(divisor))
            return

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
