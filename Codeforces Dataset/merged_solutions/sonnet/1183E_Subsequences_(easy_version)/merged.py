import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2].decode()

# Clause distinct_counts [Confidence: 1.00]
def distinct_counts(n, s):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    last = {}
    for i in range(1, n + 1):
        ch = s[i - 1]
        table[i][0] = 1
        for length in range(1, i + 1):
            table[i][length] = table[i - 1][length] + table[i - 1][length - 1]
            if ch in last:
                previous = last[ch]
                table[i][length] -= table[previous - 1][length - 1]
        last[ch] = i
    return table[n]

# Clause cheapest_set [Confidence: 1.00]
def cheapest_set(n, k, s):
    counts = distinct_counts(n, s)
    left = k
    total = 0
    for length in range(n, -1, -1):
        if left == 0:
            break
        take = counts[length]
        if take > left:
            take = left
        total += take * (n - length)
        left -= take
    return -1 if left else total

# Clause main [Confidence: 1.00]
def main():
    n, k, s = read_input()
    sys.stdout.write(str(cheapest_set(n, k, s)) + "\n")


if __name__ == "__main__":
    main()

