import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])

# Clause residue_counts [Confidence: 1.00]
def residue_counts(l, r):
    counts = []
    for j in range(3):
        counts.append((r - j) // 3 - (l - 1 - j) // 3)
    return counts

# Clause count_arrays [Confidence: 1.00]
def count_arrays(n, counts):
    mod = 1000000007
    ways = [1, 0, 0]
    for _ in range(n):
        nxt = [0, 0, 0]
        for s in range(3):
            here = ways[s]
            if here:
                for j in range(3):
                    t = (s + j) % 3
                    nxt[t] = (nxt[t] + here * counts[j]) % mod
        ways = nxt
    return ways[0] % mod

# Clause main [Confidence: 1.00]
def main():
    n, l, r = read_input()
    counts = residue_counts(l, r)
    sys.stdout.write("%d\n" % count_arrays(n, counts))


if __name__ == "__main__":
    main()

