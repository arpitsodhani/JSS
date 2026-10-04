import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    v = 0
    for _ in range(n):
        v |= data[idx]
        idx += 1
    ans.append(str(v))

print("\n".join(ans))
