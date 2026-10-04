import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    asked = []
    for i in range(q):
        asked.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, asked

# Clause cell_value [Confidence: 0.80]
def cell_value(n, x, y):
    place = (x - 1) * n + y - 1
    half = (n * n + 1) // 2
    if (x + y) % 2 == 0:
        return place // 2 + 1
    return half + place // 2 + 1

# Clause main [Confidence: 1.00]
def main():
    n, asked = read_input()
    collected = []
    for x, y in asked:
        collected.append(cell_value(n, x, y))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

