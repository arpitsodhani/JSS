# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, m = (data[0], data[1])
rows = set()
cols = set()
ans = []
idx = 2
for _ in range(m):
    r = data[idx]
    c = data[idx + 1]
    idx += 2
    rows.add(r)
    cols.add(c)
    ans.append(str((n - len(rows)) * (n - len(cols))))
sys.stdout.write(' '.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
