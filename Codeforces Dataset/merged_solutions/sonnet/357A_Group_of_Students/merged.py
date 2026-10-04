import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m = data[0]
    counts = data[1:1 + m]
    return counts, data[1 + m], data[2 + m]

# Clause best_rate [Confidence: 1.00]
def best_rate(counts, low, high):
    m = len(counts)
    best = 0
    gap = -1
    for k in range(1, m + 1):
        beginners = 0
        for item in range(k - 1):
            beginners += counts[item]
        rest = 0
        for item in range(k - 1, m):
            rest += counts[item]
        if beginners < low or beginners > high or rest < low or rest > high:
            continue
        here = beginners - rest
        if here < 0:
            here = -here
        if gap < 0 or here < gap:
            gap = here
            best = k
    return best if gap >= 0 else 0

# Clause main [Confidence: 1.00]
def main():
    counts, low, high = read_input()
    sys.stdout.write("%d\n" % best_rate(counts, low, high))


if __name__ == "__main__":
    main()

