import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return cases

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause widest_pair [Confidence: 1.00]
def widest_pair(l, r, g):
    bottom = (l + g - 1) // g
    high = r // g
    if bottom > high:
        return -1, -1
    span = high - bottom
    while span >= 0:
        start = bottom
        while start + span <= high:
            if gcd_of(start, start + span) == 1:
                return start * g, (start + span) * g
            start += 1
        span -= 1
    return -1, -1

# Clause main [Confidence: 1.00]
def main():
    out = []
    for l, r, g in read_input():
        out.append("%d %d" % widest_pair(l, r, g))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

