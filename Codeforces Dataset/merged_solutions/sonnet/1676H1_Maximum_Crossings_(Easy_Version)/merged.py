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

# Clause count_crossings [Confidence: 0.60]
def count_crossings(a):
    n = len(a)
    total = 0
    for i in range(n):
        left = a[i]
        for j in range(i + 1, n):
            if left >= a[j]:
                total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(count_crossings(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

