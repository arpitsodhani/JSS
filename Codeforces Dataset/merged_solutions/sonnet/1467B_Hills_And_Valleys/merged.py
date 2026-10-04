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

# Clause bumpiness [Confidence: 1.00]
def bumpiness(a, j):
    if j <= 0 or j >= len(a) - 1:
        return 0
    if a[j] > a[j - 1] and a[j] > a[j + 1]:
        return 1
    if a[j] < a[j - 1] and a[j] < a[j + 1]:
        return 1
    return 0

# Clause least_value [Confidence: 1.00]
def least_value(a):
    n = len(a)
    amount = 0
    for j in range(n):
        amount += bumpiness(a, j)
    saved = 0
    for i in range(n):
        before = bumpiness(a, i - 1) + bumpiness(a, i) + bumpiness(a, i + 1)
        keep = a[i]
        for j in (i - 1, i + 1):
            if j < 0 or j >= n:
                continue
            a[i] = a[j]
            after = bumpiness(a, i - 1) + bumpiness(a, i) + bumpiness(a, i + 1)
            if before - after > saved:
                saved = before - after
        a[i] = keep
    return amount - saved

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(least_value(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

