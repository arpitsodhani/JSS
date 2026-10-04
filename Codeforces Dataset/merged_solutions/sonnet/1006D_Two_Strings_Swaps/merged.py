import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode(), data[2].decode()

# Clause pair_cost [Confidence: 0.80]
def pair_cost(x, y, p, q):
    if p == q:
        return 0 if x == y else 1
    matched = 0
    pool = [p, q]
    for ch in (x, y):
        if ch in pool:
            pool.remove(ch)
            matched += 1
    return 2 - matched

# Clause preprocess_moves [Confidence: 1.00]
def preprocess_moves(a, b):
    n = len(a)
    amount = 0
    for i in range(n // 2):
        j = n - 1 - i
        amount += pair_cost(a[i], a[j], b[i], b[j])
    if n % 2 and a[n // 2] != b[n // 2]:
        amount += 1
    return amount

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % preprocess_moves(a, b))


if __name__ == "__main__":
    main()

