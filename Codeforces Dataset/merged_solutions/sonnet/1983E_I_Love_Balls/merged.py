import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause split_scores [Confidence: 1.00]
def split_scores(k, values):
    mod = 10 ** 9 + 7
    special = sum(values[:k]) % mod
    plain = sum(values[k:]) % mod
    gaps = len(values) - k + 1
    alice = special * ((gaps + 1) // 2) % mod * pow(gaps, mod - 2, mod) % mod
    if gaps > 1:
        share = gaps - 1
        alice = (alice + plain * ((share + 1) // 2) % mod * pow(share, mod - 2, mod)) % mod
    amount = (special + plain) % mod
    return alice, (amount - alice) % mod

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, values in read_input():
        alice, bob = split_scores(k, values)
        out.append("%d %d" % (alice, bob))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

