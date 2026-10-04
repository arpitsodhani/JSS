import sys
MOD = 1000000007

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    names = [data[2 + i] for i in range(n)]
    return n, m, names

# Clause count_names [Confidence: 0.60]
def count_names(n, m, names):
    total = 1
    for col in range(m):
        seen = set()
        for row in names:
            seen.add(row[col])
        total = total * len(seen) % MOD
    return total

# Clause main [Confidence: 1.00]
def main():
    n, m, names = read_input()
    sys.stdout.write(str(count_names(n, m, names)) + "\n")


if __name__ == "__main__":
    main()

