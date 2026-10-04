import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    x = data[2]
    return k, x, data[3:3 + n]

# Clause run_rounds [Confidence: 1.00]
def run_rounds(k, x, strengths):
    top = 1024
    counts = [0] * top
    for value in strengths:
        counts[value] += 1
    met = {}
    stride = 0
    while stride < k:
        key = tuple(counts)
        if key in met:
            period = stride - met[key]
            left = (k - stride) % period
            for _ in range(left):
                counts = one_round(counts, x, top)
            return counts
        met[key] = stride
        counts = one_round(counts, x, top)
        stride += 1
    return counts

# Clause one_round [Confidence: 1.00]
def one_round(counts, x, top):
    fresh = [0] * top
    parity = 0
    for value in range(top):
        here = counts[value]
        if here == 0:
            continue
        moved = (here + 1) // 2 if parity == 0 else here // 2
        fresh[value ^ x] += moved
        fresh[value] += here - moved
        parity = (parity + here) % 2
    return fresh

# Clause main [Confidence: 1.00]
def main():
    k, x, strengths = read_input()
    counts = run_rounds(k, x, strengths)
    low = -1
    high = 0
    for value in range(len(counts)):
        if counts[value]:
            if low < 0:
                low = value
            high = value
    sys.stdout.write("%d %d\n" % (high, low))


if __name__ == "__main__":
    main()

