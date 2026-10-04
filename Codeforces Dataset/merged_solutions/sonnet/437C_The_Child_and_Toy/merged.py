import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    values = data[2:2 + n]
    ropes = []
    pos = 2 + n
    for _ in range(m):
        ropes.append((data[pos], data[pos + 1]))
        pos += 2
    return values, ropes

# Clause total_energy [Confidence: 1.00]
def total_energy(values, ropes):
    total = 0
    for x, y in ropes:
        left = values[x - 1]
        finish = values[y - 1]
        total += left if left < finish else finish
    return total

# Clause main [Confidence: 1.00]
def main():
    values, ropes = read_input()
    sys.stdout.write("%d\n" % total_energy(values, ropes))


if __name__ == "__main__":
    main()

