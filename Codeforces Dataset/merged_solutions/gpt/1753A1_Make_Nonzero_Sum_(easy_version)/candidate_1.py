# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    if n % 2:
        out.append("-1")
        continue

    ans = []
    for i in range(0, n, 2):
        if a[i] == a[i + 1]:
            ans.append((i + 1, i + 2))
        else:
            ans.append((i + 1, i + 1))
            ans.append((i + 2, i + 2))

    out.append(str(len(ans)))
    out.extend(f"{l} {r}" for l, r in ans)

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
