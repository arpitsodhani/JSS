# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    items = sys.stdin.buffer.read().split()
    if not items:
        return
    n = int(items[0])
    m = int(items[1])
    k = int(items[2])
    line = b"".join(items[3:])

    grid = [[0] * m for _ in range(n)]
    at = 0
    for r in range(n):
        row = grid[r]
        for c in range(m):
            row[c] = line[at] == 49
            at += 1

    if n > m:
        grid = [[grid[r][c] for r in range(n)] for c in range(m)]
        n, m = m, n

    answer = 0
    for first in range(n):
        sums = [0] * m
        for last in range(first, n):
            source = grid[last]
            for idx in range(m):
                sums[idx] += source[idx]
            current = 0
            counts = {0: 1}
            for number in sums:
                current += number
                answer += counts.get(current - k, 0)
                counts[current] = counts.get(current, 0) + 1

    print(answer)

# CLAUSE: finish_program
solve()
