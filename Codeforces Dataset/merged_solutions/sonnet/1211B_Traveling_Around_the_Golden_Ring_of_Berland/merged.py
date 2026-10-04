import sys

# Clause read_input [Confidence: 0.40]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    wanted = list(map(int, data[1:n + 1]))
    return n, wanted

# Clause count_visits [Confidence: 1.00]
def count_visits(n, wanted):
    most = 0
    for value in wanted:
        if value > most:
            most = value
    last = 0
    for i in range(n):
        if wanted[i] == most:
            last = i + 1
    return (most - 1) * n + last

# Clause main [Confidence: 0.40]
def main():
    n, wanted = read_input()
    sys.stdout.write(str(count_visits(n, wanted)) + "\n")


if __name__ == "__main__":
    main()

