import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    b = int(data[2])
    mod = int(data[3])
    bugs = [int(token) for token in data[4:n + 4]]
    return n, m, b, mod, bugs

# Clause count_plans [Confidence: 1.00]
def count_plans(n, m, b, mod, bugs):
    width = b + 1
    table = [[0] * width for _ in range(m + 1)]
    table[0][0] = 1 % mod
    for rate in bugs:
        if rate > b:
            continue
        for lines in range(1, m + 1):
            row = table[lines]
            prev = table[lines - 1]
            for cost in range(rate, b + 1):
                value = prev[cost - rate]
                if value:
                    row[cost] = (row[cost] + value) % mod
    total = 0
    for value in table[m]:
        total += value
    return total % mod

# Clause main [Confidence: 1.00]
def main():
    n, m, b, mod, bugs = read_input()
    sys.stdout.write(str(count_plans(n, m, b, mod, bugs)) + "\n")


if __name__ == "__main__":
    main()

