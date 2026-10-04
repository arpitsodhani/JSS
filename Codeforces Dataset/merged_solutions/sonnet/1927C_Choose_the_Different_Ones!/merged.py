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
        k = data[pos + 2]
        pos += 3
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        cases.append((k, a, b))
    return cases

# Clause can_pick [Confidence: 0.80]
def can_pick(k, a, b):
    left = set(value for value in a if value <= k)
    finish = set(value for value in b if value <= k)
    only_left = 0
    only_right = 0
    for value in range(1, k + 1):
        here = value in left
        there = value in finish
        if not here and not there:
            return False
        if here and not there:
            only_left += 1
        elif there and not here:
            only_right += 1
    half = k // 2
    return only_left <= half and only_right <= half

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a, b in read_input():
        out.append("YES" if can_pick(k, a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

