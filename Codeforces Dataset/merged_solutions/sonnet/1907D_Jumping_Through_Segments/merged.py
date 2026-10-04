import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        bounds = [int(token) for token in data[pos:pos + 2 * n]]
        pos += 2 * n
        cases.append(bounds)
    return cases

# Clause reachable [Confidence: 0.80]
def reachable(bounds, k):
    low = 0
    high = 0
    for i in range(0, len(bounds), 2):
        low -= k
        high += k
        if low < bounds[i]:
            low = bounds[i]
        if high > bounds[i + 1]:
            high = bounds[i + 1]
        if low > high:
            return False
    return True

# Clause smallest_reach [Confidence: 1.00]
def smallest_reach(bounds):
    lo = 0
    hi = 1000000000
    while lo < hi:
        mid = (lo + hi) // 2
        if reachable(bounds, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# Clause main [Confidence: 1.00]
def main():
    out = []
    for bounds in read_input():
        out.append(str(smallest_reach(bounds)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

