import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append([(data[pos + 2 * i], data[pos + 2 * i + 1]) for i in range(n)])
        pos += 2 * n
    return cases

# Clause reachable [Confidence: 0.80]
def reachable(points):
    right = True
    left = True
    up = True
    down = True
    for x, y in points:
        if x < 0:
            right = False
        if x > 0:
            left = False
        if y < 0:
            up = False
        if y > 0:
            down = False
    return right or left or up or down

# Clause main [Confidence: 1.00]
def main():
    out = []
    for points in read_input():
        out.append("YES" if reachable(points) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

