# CLAUSE: setup_environment
import sys
from collections import Counter

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x = data[0], data[1]
    values = data[2:2 + n]
    total = sum(values)
    counts = Counter(total - value for value in values)

    carry = 0
    current = None

    for exponent in sorted(counts):
        if current is not None:
            while carry and current < exponent:
                if carry % x:
                    print(pow(x, min(current, total), MOD))
                    return
                carry //= x
                current += 1

        current = exponent
        carry += counts[exponent]

        if carry % x:
            print(pow(x, min(current, total), MOD))
            return
        carry //= x
        current += 1

    while carry:
        if carry % x:
            print(pow(x, min(current, total), MOD))
            return
        carry //= x
        current += 1

    print(pow(x, total, MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
