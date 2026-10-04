import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    s = 0
    ok = True
    for i in range(n - 1):
        s += a[i]
        if s < 0:
            ok = False
    s += a[-1]

    ans.append("Yes" if ok and s == 0 else "No")

print("\n".join(ans))
