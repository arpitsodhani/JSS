# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [row[:] for row in a]
    for i in range(n):
        for j in range(m):
            mx = -1
            ok = True
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = (i + di, j + dj)
                if 0 <= ni < n and 0 <= nj < m:
                    mx = max(mx, a[ni][nj])
                    if a[i][j] <= a[ni][nj]:
                        ok = False
            if ok:
                b[i][j] = mx
    for row in b:
        print(*row)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
