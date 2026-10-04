import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((n, x, data[pos:pos + n]))
        pos += n
    return cases

# Clause best_by_length [Confidence: 1.00]
def best_by_length(n, a):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        top = None
        for start in range(n - length + 1):
            here = prefix[start + length] - prefix[start]
            if top is None or here > top:
                top = here
        best[length] = top
    return best

# Clause answers [Confidence: 1.00]
def answers(n, x, a):
    best = best_by_length(n, a)
    out = []
    for k in range(n + 1):
        top = 0
        for length in range(1, n + 1):
            add = length if length < k else k
            here = best[length] + add * x
            if here > top:
                top = here
        out.append(top)
    return out

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, x, a in read_input():
        lines.append(" ".join(map(str, answers(n, x, a))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

