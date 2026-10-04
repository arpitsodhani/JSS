import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]

# Clause count_layouts [Confidence: 1.00]
def count_layouts(rows):
    mod = 1000000007
    n = len(rows)
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n):
        fresh = [0] * (n + 1)
        if rows[i - 1] == "f":
            for level in range(1, n + 1):
                fresh[level] = ways[level - 1]
        else:
            running = 0
            for level in range(n, -1, -1):
                running = (running + ways[level]) % mod
                fresh[level] = running
        ways = fresh
    summed = 0
    for element in ways:
        summed = (summed + element) % mod
    return summed

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % count_layouts(read_input()))


if __name__ == "__main__":
    main()

