import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        cases.append((a, b))
    return cases

# Clause can_sort [Confidence: 1.00]
def can_sort(a, b):
    ranked = sorted(b)
    previous = -(1 << 62)
    for value in a:
        best = 1 << 62
        if value >= previous:
            best = value
        want = previous + value
        low = 0
        high = len(ranked)
        while low < high:
            mid = (low + high) // 2
            if ranked[mid] < want:
                low = mid + 1
            else:
                high = mid
        if low < len(ranked):
            flipped = ranked[low] - value
            if flipped < best:
                best = flipped
        if best == (1 << 62):
            return False
        previous = best
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b in read_input():
        out.append("YES" if can_sort(a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

