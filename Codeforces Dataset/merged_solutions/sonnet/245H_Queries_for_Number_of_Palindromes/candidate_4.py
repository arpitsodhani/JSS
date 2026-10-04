# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_tables(s):
    n = len(s)
    good = [[0] * n for _ in range(n)]
    counts = [[0] * n for _ in range(n)]
    for right in range(n):
        for left in range(right, -1, -1):
            if s[left] == s[right] and (right - left < 2 or good[left + 1][right - 1]):
                good[left][right] = 1
    for left in range(n - 1, -1, -1):
        for right in range(left, n):
            value = good[left][right]
            if left + 1 < n:
                value += counts[left + 1][right]
            if right:
                value += counts[left][right - 1]
            if left + 1 < n and right:
                value -= counts[left + 1][right - 1]
            counts[left][right] = value
    return counts

items = sys.stdin.read().strip().split()
s = items[0]
table = build_tables(s)
m = int(items[1])
result = []
k = 2
for _ in range(m):
    a = int(items[k]) - 1
    b = int(items[k + 1]) - 1
    k += 2
    result.append(str(table[a][b]))

# CLAUSE: finish_program
sys.stdout.write("\n".join(result))
