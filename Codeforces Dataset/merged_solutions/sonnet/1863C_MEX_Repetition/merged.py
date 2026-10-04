import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause spin [Confidence: 0.80]
def spin(k, a):
    n = len(a)
    seen = [False] * (n + 2)
    for element in a:
        seen[element] = True
    missing = 0
    while seen[missing]:
        missing += 1
    circle = a + [missing]
    shift = k % (n + 1)
    if shift:
        circle = circle[-shift:] + circle[:-shift]
    return circle[:n]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a in read_input():
        out.append(" ".join(map(str, spin(k, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

