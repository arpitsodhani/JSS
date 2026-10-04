# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    edges = []
    for _ in range(m):
        v = data[idx]
        u = data[idx + 1]
        idx += 2
        edges.append((v, u))
    out.append(f'! {len(edges)}')
    for v, u in edges:
        out.append(f'{v} {u}')
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
