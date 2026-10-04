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

# Clause can_sort [Confidence: 0.80]
def can_sort(a):
    ranked = sorted(a)
    here = {}
    there = {}
    for i in range(len(a)):
        key = (a[i], i % 2)
        here[key] = here.get(key, 0) + 1
        other = (ranked[i], i % 2)
        there[other] = there.get(other, 0) + 1
    return here == there

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for a in read_input():
        lines.append("YES" if can_sort(a) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

