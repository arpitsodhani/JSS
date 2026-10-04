import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    d = int(data[0])
    n = int(data[1])
    months = [int(token) for token in data[2:n + 2]]
    return d, n, months

# Clause manual_clicks [Confidence: 0.60]
def manual_clicks(d, n, months):
    total = 0
    for i in range(n - 1):
        total += d - months[i]
    return total

# Clause main [Confidence: 1.00]
def main():
    d, n, months = read_input()
    sys.stdout.write(str(manual_clicks(d, n, months)) + "\n")


if __name__ == "__main__":
    main()

