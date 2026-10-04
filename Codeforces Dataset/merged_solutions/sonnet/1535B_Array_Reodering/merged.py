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

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause count_good [Confidence: 1.00]
def count_good(a):
    n = len(a)
    odds = [element for element in a if element % 2]
    evens = n - len(odds)
    total = 0
    for k in range(evens):
        total += n - 1 - k
    for i in range(len(odds)):
        for j in range(i + 1, len(odds)):
            if gcd_of(odds[i], odds[j]) > 1:
                total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(count_good(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

