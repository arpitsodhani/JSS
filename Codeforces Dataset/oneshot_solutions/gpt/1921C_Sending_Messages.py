import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    f = data[idx + 1]
    a = data[idx + 2]
    b = data[idx + 3]
    idx += 4

    prev = 0
    for i in range(n):
        m = data[idx + i]
        f -= min((m - prev) * a, b)
        prev = m

    idx += n
    ans.append("YES" if f > 0 else "NO")

print("\n".join(ans))
