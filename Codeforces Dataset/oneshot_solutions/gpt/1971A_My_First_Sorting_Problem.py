import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

idx = 1
for _ in range(t):
    x, y = data[idx], data[idx + 1]
    idx += 2
    if x > y:
        x, y = y, x
    ans.append(f"{x} {y}")

print("\n".join(ans))
