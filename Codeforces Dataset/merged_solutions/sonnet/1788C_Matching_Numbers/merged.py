import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_pairs [Confidence: 1.00]
def build_pairs(n):
    if n % 2 == 0:
        return None
    k = (n - 1) // 2
    pairs = []
    for i in range(1, k + 2):
        pairs.append((2 * i - 1, 2 * n + 1 - i))
    for i in range(1, k + 1):
        pairs.append((2 * i, 2 * n - k - i))
    return pairs

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        pairs = build_pairs(n)
        if pairs is None:
            collected.append("No")
        else:
            collected.append("Yes")
            for a, b in pairs:
                collected.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

