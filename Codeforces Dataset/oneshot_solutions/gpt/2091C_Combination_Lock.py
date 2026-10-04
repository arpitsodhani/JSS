import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    if n % 2 == 0:
        ans.append("-1")
    else:
        ans.append(" ".join(str((2 * i) % n + 1) for i in range(n)))

print("\n".join(ans))
