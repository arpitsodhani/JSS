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
    m = min(a)
    ans.append(str(sum(a) - m * n))

print("\n".join(ans))
