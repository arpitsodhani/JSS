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

# Clause best_jog [Confidence: 0.80]
def best_jog(b):
    n = len(b)
    ahead = [0] * n
    behind = [0] * n
    ahead[0] = b[0] + 0
    for i in range(1, n):
        here = b[i] + i
        ahead[i] = here if here > ahead[i - 1] else ahead[i - 1]
    behind[n - 1] = b[n - 1] - (n - 1)
    for i in range(n - 2, -1, -1):
        here = b[i] - i
        behind[i] = here if here > behind[i + 1] else behind[i + 1]
    best = -(1 << 62)
    for j in range(1, n - 1):
        amount = ahead[j - 1] + b[j] + behind[j + 1]
        if amount > best:
            best = amount
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for b in read_input():
        out.append(best_jog(b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

