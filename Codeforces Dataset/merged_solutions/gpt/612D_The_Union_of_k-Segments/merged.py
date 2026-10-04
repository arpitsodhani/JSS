# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[0], data[1]

events = []
idx = 2
for _ in range(n):
    l, r = data[idx], data[idx + 1]
    idx += 2
    events.append((l, -1))
    events.append((r, 1))

events.sort()

cnt = 0
start = None
ans = []

for x, typ in events:
    if typ == -1:
        cnt += 1
        if cnt == k:
            start = x
    else:
        cnt -= 1
        if cnt == k - 1:
            ans.append((start, x))

out = [str(len(ans))]
out.extend(f"{l} {r}" for l, r in ans)
sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
