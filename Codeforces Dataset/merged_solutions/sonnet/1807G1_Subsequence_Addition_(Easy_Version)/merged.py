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
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause can_build [Confidence: 1.00]
def can_build(c):
    order = sorted(c)
    if order[0] != 1:
        return False
    reached = 1
    for i in range(1, len(order)):
        if order[i] > reached:
            return False
        reached += order[i]
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for c in read_input():
        out.append("YES" if can_build(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

