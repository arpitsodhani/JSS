import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1].decode()
        pos += 2
        cases.append((n, s))
    return cases

# Clause build_permutation [Confidence: 1.00]
def build_permutation(n, s):
    p = list(range(1, n + 1))
    i = 0
    while i < n:
        if s[i] == "1":
            i += 1
            continue
        j = i
        while j < n and s[j] == "0":
            j += 1
        if j - i == 1:
            return None
        for slot in range(i, j - 1):
            p[slot] = slot + 2
        p[j - 1] = i + 1
        i = j
    return p

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, s in read_input():
        p = build_permutation(n, s)
        if p is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, p)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

