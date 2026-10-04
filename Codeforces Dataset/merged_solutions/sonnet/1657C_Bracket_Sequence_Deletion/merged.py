import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append(data[2 + 2 * i].decode())
    return cases

# Clause strip_prefixes [Confidence: 1.00]
def strip_prefixes(s):
    n = len(s)
    at = 0
    steps = 0
    while at + 1 < n:
        if s[at] == s[at + 1] or s[at] == "(":
            steps += 1
            at += 2
            continue
        j = at + 2
        while j < n and s[j] == "(":
            j += 1
        if j == n:
            break
        steps += 1
        at = j + 1
    return steps, n - at

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        steps, rest = strip_prefixes(s)
        collected.append("%d %d" % (steps, rest))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

