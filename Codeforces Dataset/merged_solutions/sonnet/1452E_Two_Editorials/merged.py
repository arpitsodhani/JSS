import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    segments = []
    pos = 3
    for _ in range(m):
        segments.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, k, segments

# Clause best_total [Confidence: 0.80]
def best_total(n, m, k, segments):
    order = sorted(segments, key=lambda seg: seg[0] + seg[1])
    prefix = [0] * (m + 1)
    suffix = [0] * (m + 1)
    for start in range(1, n - k + 2):
        end = start + k - 1
        running = 0
        for i in range(m):
            l, r = order[i]
            lo = l if l > start else start
            hi = r if r < end else end
            if hi >= lo:
                running += hi - lo + 1
            if running > prefix[i + 1]:
                prefix[i + 1] = running
        running = 0
        for i in range(m - 1, -1, -1):
            l, r = order[i]
            lo = l if l > start else start
            hi = r if r < end else end
            if hi >= lo:
                running += hi - lo + 1
            if running > suffix[i]:
                suffix[i] = running
    best = 0
    for i in range(m + 1):
        total = prefix[i] + suffix[i]
        if total > best:
            best = total
    return best

# Clause main [Confidence: 1.00]
def main():
    n, m, k, segments = read_input()
    sys.stdout.write(str(best_total(n, m, k, segments)) + "\n")


if __name__ == "__main__":
    main()

