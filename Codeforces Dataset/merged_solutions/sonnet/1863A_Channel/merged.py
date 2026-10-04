import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        a = int(data[pos + 1])
        pos += 3
        cases.append((n, a, data[pos].decode()))
        pos += 1
    return cases

# Clause verdict [Confidence: 1.00]
def verdict(n, a, notes):
    online = a
    reached = a == n
    known = a
    for ch in notes:
        if ch == "+":
            online += 1
            known += 1
        else:
            online -= 1
        if online == n:
            reached = True
    if reached:
        return "YES"
    return "MAYBE" if known >= n else "NO"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, a, notes in read_input():
        out.append(verdict(n, a, notes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

