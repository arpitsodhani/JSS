import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]

# Clause cheapest_path [Confidence: 1.00]
def cheapest_path(n, k, a, b):
    if k == 1:
        return (n - 1) * a
    amount = 0
    x = n
    while x > 1:
        if x < k:
            amount += (x - 1) * a
            break
        rest = x % k
        amount += rest * a
        x -= rest
        if x == 0:
            break
        drop = (x - x // k) * a
        amount += b if b < drop else drop
        x //= k
    return amount

# Clause main [Confidence: 1.00]
def main():
    n, k, a, b = read_input()
    sys.stdout.write("%d\n" % cheapest_path(n, k, a, b))


if __name__ == "__main__":
    main()

