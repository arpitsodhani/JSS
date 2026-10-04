import sys
from math import gcd

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    birds = []
    pos = 2
    for _ in range(m):
        birds.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, birds

# Clause line_counts [Confidence: 1.00]
def line_counts(n, birds):
    m = len(birds)
    pairs = {}
    for i in range(m):
        x1, y1 = birds[i]
        for j in range(i + 1, m):
            x2, y2 = birds[j]
            if y1 == y2:
                continue
            num = x1 * y2 - x2 * y1
            den = y2 - y1
            if num % den:
                continue
            spot = num // den
            if spot < 1 or spot > n:
                continue
            dx = x1 - spot
            step = gcd(abs(dx), y1)
            key = (spot, dx // step, y1 // step)
            pairs[key] = pairs.get(key, 0) + 1
    return pairs

# Clause total_seen [Confidence: 1.00]
def total_seen(n, m, birds):
    pairs = line_counts(n, birds)
    best = {}
    for key, count in pairs.items():
        size = 2
        while size * (size - 1) // 2 < count:
            size += 1
        spot = key[0]
        if best.get(spot, 0) < size:
            best[spot] = size
    total = n
    for size in best.values():
        total += size - 1
    return total

# Clause main [Confidence: 1.00]
def main():
    n, m, birds = read_input()
    sys.stdout.write(str(total_seen(n, m, birds)) + "\n")


if __name__ == "__main__":
    main()

