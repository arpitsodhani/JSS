import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    kids = []
    for _ in range(n):
        k = data[pos]
        pos += 1
        kids.append(data[pos:pos + k])
        pos += k
    return kids

# Clause item_counts [Confidence: 1.00]
def item_counts(kids):
    tally = {}
    for wants in kids:
        for item in wants:
            tally[item] = tally.get(item, 0) + 1
    return tally

# Clause valid_chance [Confidence: 1.00]
def valid_chance(kids, tally):
    mod = 998244353
    n = len(kids)
    inverse_n = pow(n, mod - 2, mod)
    running = 0
    for wants in kids:
        share = pow(len(wants), mod - 2, mod)
        for item in wants:
            running = (running + share * tally[item]) % mod
    return running * inverse_n % mod * inverse_n % mod

# Clause main [Confidence: 1.00]
def main():
    kids = read_input()
    sys.stdout.write("%d\n" % valid_chance(kids, item_counts(kids)))


if __name__ == "__main__":
    main()

