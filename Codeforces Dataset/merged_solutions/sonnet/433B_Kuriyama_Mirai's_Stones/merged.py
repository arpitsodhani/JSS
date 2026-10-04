import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    stones = data[1:1 + n]
    m = data[1 + n]
    asked = []
    pos = 2 + n
    for _ in range(m):
        asked.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return stones, asked

# Clause prefix_sums [Confidence: 0.80]
def prefix_sums(stones):
    plain = [0] * (len(stones) + 1)
    for i in range(len(stones)):
        plain[i + 1] = plain[i] + stones[i]
    arranged = sorted(stones)
    ranked = [0] * (len(stones) + 1)
    for i in range(len(arranged)):
        ranked[i + 1] = ranked[i] + arranged[i]
    return plain, ranked

# Clause main [Confidence: 1.00]
def main():
    stones, asked = read_input()
    plain, ranked = prefix_sums(stones)
    out = []
    for kind, low, high in asked:
        table = plain if kind == 1 else ranked
        out.append(table[high] - table[low - 1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

