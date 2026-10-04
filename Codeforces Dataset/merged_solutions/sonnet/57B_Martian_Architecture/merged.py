import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m = data[1]
    k = data[2]
    roads = []
    pos = 3
    for _ in range(m):
        roads.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return roads, data[pos:pos + k]

# Clause total_stones [Confidence: 1.00]
def total_stones(roads, asked):
    total = 0
    for spot in asked:
        for floor_value, high, first in roads:
            if floor_value <= spot <= high:
                total += first + spot - floor_value
    return total

# Clause main [Confidence: 1.00]
def main():
    roads, asked = read_input()
    sys.stdout.write("%d\n" % total_stones(roads, asked))


if __name__ == "__main__":
    main()

