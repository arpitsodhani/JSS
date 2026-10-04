import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        l = data[pos + 1]
        r = data[pos + 2]
        pos += 3
        cases.append((l, r, data[pos:pos + n]))
        pos += n
    return cases

# Clause upper_bound [Confidence: 0.80]
def upper_bound(a, value):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= value:
            low = mid + 1
        else:
            high = mid
    return low

# Clause count_pairs [Confidence: 1.00]
def count_pairs(l, r, a):
    a = sorted(a)
    total = 0
    for value in a:
        total += upper_bound(a, r - value) - upper_bound(a, l - value - 1)
        if l <= 2 * value <= r:
            total -= 1
    return total // 2

# Clause main [Confidence: 1.00]
def main():
    out = []
    for l, r, a in read_input():
        out.append(count_pairs(l, r, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

