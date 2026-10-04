import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    values = [int(token) for token in data[2:n + 2]]
    return n, k, values

# Clause maximise_sum [Confidence: 1.00]
def maximise_sum(n, k, values):
    flipped = list(values)
    left = k
    for i in range(n):
        if left == 0:
            break
        if flipped[i] < 0:
            flipped[i] = -flipped[i]
            left -= 1
    total = 0
    smallest = flipped[0]
    for value in flipped:
        total += value
        if value < smallest:
            smallest = value
    if left % 2 == 1:
        total -= 2 * smallest
    return total

# Clause main [Confidence: 1.00]
def main():
    n, k, values = read_input()
    sys.stdout.write(str(maximise_sum(n, k, values)) + "\n")


if __name__ == "__main__":
    main()

