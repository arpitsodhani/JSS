import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        s = data[pos + 3]
        pos += 4
        cases.append((n, m, k, s))
    return cases

# Clause timar_uses [Confidence: 1.00]
def timar_uses(n, m, k, s):
    used = 0
    run = 0
    i = 0
    while i < n:
        if s[i] == 48:
            run += 1
            if run == m:
                used += 1
                i += k
                run = 0
                continue
        else:
            run = 0
        i += 1
    return used

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, m, k, s in read_input():
        out.append(str(timar_uses(n, m, k, s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

