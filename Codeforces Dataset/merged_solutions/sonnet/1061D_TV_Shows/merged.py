import sys
from heapq import heappush, heappop
MOD = 10 ** 9 + 7

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    y = data[2]
    shows = []
    pos = 3
    for _ in range(n):
        shows.append((data[pos], data[pos + 1]))
        pos += 2
    return n, x, y, shows

# Clause total_cost [Confidence: 1.00]
def total_cost(n, x, y, shows):
    order = sorted(shows)
    busy = []
    free = []
    total = 0
    for start, finish in order:
        while busy and busy[0] < start:
            heappush(free, -heappop(busy))
        if free and y * (start + free[0]) <= x:
            last = -heappop(free)
            total += y * (finish - last)
        else:
            total += x + y * (finish - start)
        heappush(busy, finish)
    return total % MOD

# Clause main [Confidence: 1.00]
def main():
    n, x, y, shows = read_input()
    sys.stdout.write(str(total_cost(n, x, y, shows)) + "\n")


if __name__ == "__main__":
    main()

