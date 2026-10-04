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

# Clause is_shuffle [Confidence: 1.00]
def is_shuffle(a):
    n = len(a)
    known = [False] * n
    for k in range(n):
        spot = (k + a[k]) % n
        if known[spot]:
            return False
        known[spot] = True
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if is_shuffle(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

