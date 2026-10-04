import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    values = list(map(int, data[1:count + 1]))
    return count, values

# Clause count_sums [Confidence: 0.80]
def count_sums(n, values):
    counts = [0] * 200001
    for i in range(n):
        first = values[i]
        for j in range(i + 1, n):
            counts[first + values[j]] += 1
    return counts

# Clause compute_answer [Confidence: 1.00]
def compute_answer(counts):
    best = 0
    for value in counts:
        if value > best:
            best = value
    return best

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    counts = count_sums(n, values)
    sys.stdout.write(str(compute_answer(counts)) + "\n")


if __name__ == "__main__":
    main()

