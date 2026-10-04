import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause total_segments [Confidence: 0.40]
def total_segments(a, b):
    per_digit = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    running = [0] * (b + 1)
    for number in range(1, b + 1):
        running[number] = running[number // 10] + per_digit[number % 10]
    return sum(running[a:b + 1])

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    sys.stdout.write(str(total_segments(a, b)) + "\n")


if __name__ == "__main__":
    main()

