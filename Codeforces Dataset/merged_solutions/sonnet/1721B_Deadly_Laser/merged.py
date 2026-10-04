import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append(tuple(data[pos:pos + 5]))
        pos += 5
    return cases

# Clause shortest_walk [Confidence: 0.80]
def shortest_walk(n, m, sx, sy, d):
    top = sx - 1 > d
    bottom = n - sx > d
    leftmost = sy - 1 > d
    rightmost = m - sy > d
    if (top and rightmost) or (leftmost and bottom):
        return n + m - 2
    return -1

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, m, sx, sy, d in read_input():
        collected.append(shortest_walk(n, m, sx, sy, d))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

