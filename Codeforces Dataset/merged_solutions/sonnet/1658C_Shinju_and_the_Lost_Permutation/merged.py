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

# Clause is_possible [Confidence: 0.80]
def is_possible(c):
    n = len(c)
    start = -1
    ones = 0
    for i in range(n):
        if c[i] == 1:
            ones += 1
            start = i
    if ones != 1:
        return False
    for advance in range(n):
        here = c[(start + advance) % n]
        nxt = c[(start + advance + 1) % n]
        if nxt - here > 1:
            return False
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for c in read_input():
        out.append("YES" if is_possible(c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

