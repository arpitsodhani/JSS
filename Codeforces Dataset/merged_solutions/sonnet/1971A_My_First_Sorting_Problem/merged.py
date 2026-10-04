import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]

# Clause order_pair [Confidence: 0.80]
def order_pair(x, y):
    if x <= y:
        return x, y
    return y, x

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for x, y in read_input():
        collected.append("%d %d" % order_pair(x, y))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

