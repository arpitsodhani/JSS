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

    best = sum(a)
    while len(a) > 1:
        a = [a[i + 1] - a[i] for i in range(len(a) - 1)]
        best = max(best, abs(sum(a)))

    ans.append(str(best))

print("\n".join(ans))
