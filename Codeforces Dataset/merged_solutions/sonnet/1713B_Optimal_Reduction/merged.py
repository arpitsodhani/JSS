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

# Clause is_bitonic [Confidence: 0.80]
def is_bitonic(a):
    i = 0
    n = len(a)
    while i + 1 < n and a[i] <= a[i + 1]:
        i += 1
    while i + 1 < n and a[i] >= a[i + 1]:
        i += 1
    return i == n - 1

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for a in read_input():
        lines.append("YES" if is_bitonic(a) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

