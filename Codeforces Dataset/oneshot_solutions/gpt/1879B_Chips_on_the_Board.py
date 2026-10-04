import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    b = data[idx:idx + n]
    idx += n

    ans.append(str(min(sum(a) + n * min(b), sum(b) + n * min(a))))

print("\n".join(ans))
