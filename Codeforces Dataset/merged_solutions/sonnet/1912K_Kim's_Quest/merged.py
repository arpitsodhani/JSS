import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause count_runs [Confidence: 1.00]
def count_runs(values):
    mod = 998244353
    pairs = [[0, 0], [0, 0]]
    singles = [0, 0]
    amount = 0
    for value in values:
        p = value & 1
        fresh = [[0, 0], [0, 0]]
        for x in (0, 1):
            for y in (0, 1):
                here = pairs[x][y]
                if here and (x + y + p) % 2 == 0:
                    amount = (amount + here) % mod
                    fresh[y][p] = (fresh[y][p] + here) % mod
        for x in (0, 1):
            if singles[x]:
                fresh[x][p] = (fresh[x][p] + singles[x]) % mod
        for x in (0, 1):
            for y in (0, 1):
                pairs[x][y] = (pairs[x][y] + fresh[x][y]) % mod
        singles[p] += 1
    return amount % mod

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % count_runs(read_input()))


if __name__ == "__main__":
    main()

