import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# Clause kth_card [Confidence: 0.60]
def kth_card(n, k):
    factor = 1
    while True:
        odds = (n + 1) // 2
        if k <= odds:
            return factor * (2 * k - 1)
        k -= odds
        n //= 2
        factor *= 2

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k in read_input():
        out.append(str(kth_card(n, k)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

