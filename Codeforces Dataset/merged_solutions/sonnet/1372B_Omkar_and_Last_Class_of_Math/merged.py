import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause split_pair [Confidence: 1.00]
def split_pair(n):
    factor = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            factor = d
            break
        d += 1
    if factor == 1:
        return 1, n - 1
    part = n // factor
    return part, n - part

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        collected.append("%d %d" % split_pair(n))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

