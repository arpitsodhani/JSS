import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pos = 2
    chains = []
    for _ in range(k):
        length = data[pos]
        pos += 1
        chains.append(data[pos:pos + length])
        pos += length
    return n, chains

# Clause seconds_needed [Confidence: 1.00]
def seconds_needed(n, chains):
    kept = 0
    for chain in chains:
        if chain[0] != 1:
            continue
        kept = 1
        while kept < len(chain) and chain[kept] == kept + 1:
            kept += 1
    k = len(chains)
    return 2 * n - k - 2 * kept + 1

# Clause main [Confidence: 1.00]
def main():
    n, chains = read_input()
    sys.stdout.write("%d\n" % seconds_needed(n, chains))


if __name__ == "__main__":
    main()

