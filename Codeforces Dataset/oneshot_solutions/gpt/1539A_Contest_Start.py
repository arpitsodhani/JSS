import sys

data = list(map(int, sys.stdin.buffer.read().split()))
q = data[0]
ans = []
idx = 1

for _ in range(q):
    n, x, t = data[idx], data[idx + 1], data[idx + 2]
    idx += 3
    m = min(n - 1, t // x)
    ans.append(str(m * n - m * (m + 1) // 2))

sys.stdout.write("\n".join(ans))
