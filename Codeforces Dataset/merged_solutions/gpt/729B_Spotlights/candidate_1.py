# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
vals = data[2:]

grid = []
idx = 0

if len(vals) == n and all(len(x) == m and set(x) <= {"0", "1"} for x in vals):
    for s in vals:
        grid.append([int(c) for c in s])
else:
    for i in range(n):
        row = []
        while len(row) < m and idx < len(vals):
            token = vals[idx]
            idx += 1
            if len(token) == 1:
                row.append(int(token))
            else:
                row.extend(int(c) for c in token if c in "01")
        grid.append(row[:m])

ans = 0

for i in range(n):
    seen = False
    for j in range(m):
        if grid[i][j] == 1:
            seen = True
        elif seen:
            ans += 1

    seen = False
    for j in range(m - 1, -1, -1):
        if grid[i][j] == 1:
            seen = True
        elif seen:
            ans += 1

for j in range(m):
    seen = False
    for i in range(n):
        if grid[i][j] == 1:
            seen = True
        elif seen:
            ans += 1

    seen = False
    for i in range(n - 1, -1, -1):
        if grid[i][j] == 1:
            seen = True
        elif seen:
            ans += 1

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
