import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause gaps_of [Confidence: 1.00]
def gaps_of(a):
    gaps = []
    for i in range(len(a) - 1):
        advance = a[i] - a[i + 1]
        gaps.append(advance if advance > 0 else -advance)
    return gaps

# Clause best_run [Confidence: 1.00]
def best_run(gaps):
    best = None
    for from_here in (0, 1):
        running = 0
        for i in range(len(gaps)):
            value = gaps[i] if (i - from_here) % 2 == 0 else -gaps[i]
            running += value
            if running < 0:
                running = 0
            if best is None or running > best:
                best = running
    return best

# Clause main [Confidence: 1.00]
def main():
    gaps = gaps_of(read_input())
    sys.stdout.write("%d\n" % best_run(gaps))


if __name__ == "__main__":
    main()

