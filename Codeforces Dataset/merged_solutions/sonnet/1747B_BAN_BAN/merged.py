import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]

# Clause plan_swaps [Confidence: 0.80]
def plan_swaps(n):
    moves = (n + 1) // 2
    out = [str(moves)]
    for i in range(moves):
        left = 3 * i + 2
        right = 3 * (n - 1 - i) + 3
        out.append("%d %d" % (left, right))
    return out

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.extend(plan_swaps(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

