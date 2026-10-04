import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    values = list(map(int, data[1:count + 1]))
    return count, values

# Clause sort_values [Confidence: 1.00]
def sort_values(n, values):
    counts = [0] * 61
    for value in values:
        counts[value] += 1
    ordered = []
    for value in range(1, 61):
        for _ in range(counts[value]):
            ordered.append(value)
    return ordered

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    ordered = sort_values(n, values)
    sys.stdout.write(" ".join(map(str, ordered)) + "\n")


if __name__ == "__main__":
    main()

