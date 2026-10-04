# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def reduce_pair(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    values = list(map(int, sys.stdin.read().split()))
    limit_w, limit_h, ratio_w, ratio_h = values
    common = reduce_pair(ratio_w, ratio_h)
    base_w = ratio_w // common
    base_h = ratio_h // common
    count_w = limit_w // base_w
    count_h = limit_h // base_h
    result = count_w if count_w < count_h else count_h

# CLAUSE: finish_program
    print(result)

main()
