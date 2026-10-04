import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []
idx = 1

for _ in range(t):
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    ans.append(str(max(n, m) + 1))

print("\n".join(ans))
