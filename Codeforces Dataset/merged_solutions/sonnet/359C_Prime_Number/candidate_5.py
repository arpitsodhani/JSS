# CLAUSE: setup_environment
import sys
from itertools import groupby

MOD = 1000000007

# CLAUSE: solve_logic
def reduce_until(x, carry, start, stop):
    level = start
    while carry and level < stop:
        if carry % x != 0:
            return level, carry, False
        carry //= x
        level += 1
    return level, carry, True

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n, x = raw[:2]
    arr = raw[2:2 + n]
    total = sum(arr)
    ordered = sorted(total - value for value in arr)

    carry = 0
    level = None

    for exponent, block in groupby(ordered):
        amount = sum(1 for _ in block)

        if level is None:
            level = exponent
        else:
            level, carry, ok = reduce_until(x, carry, level, exponent)
            if not ok:
                sys.stdout.write(str(pow(x, min(level, total), MOD)))
                return
            level = exponent

        carry += amount
        if carry % x:
            sys.stdout.write(str(pow(x, min(level, total), MOD)))
            return
        carry //= x
        level += 1

    while carry:
        if carry % x:
            sys.stdout.write(str(pow(x, min(level, total), MOD)))
            return
        carry //= x
        level += 1

    sys.stdout.write(str(pow(x, total, MOD)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
