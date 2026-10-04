import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    m = int(data[1])
    s = data[2].decode()
    asked = []
    for i in range(m):
        asked.append((int(data[3 + 2 * i]), int(data[4 + 2 * i])))
    return s, asked

# Clause mismatch_tables [Confidence: 1.00]
def mismatch_tables(s):
    orders = ["abc", "acb", "bac", "bca", "cab", "cba"]
    tables = []
    for arranged in orders:
        run = [0] * (len(s) + 1)
        for i in range(len(s)):
            run[i + 1] = run[i] + (0 if s[i] == arranged[i % 3] else 1)
        tables.append(run)
    return tables

# Clause cheapest [Confidence: 1.00]
def cheapest(tables, low, high):
    best = high - low + 1
    for run in tables:
        here = run[high] - run[low - 1]
        if here < best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    s, asked = read_input()
    tables = mismatch_tables(s)
    out = []
    for low, high in asked:
        out.append(cheapest(tables, low, high))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

