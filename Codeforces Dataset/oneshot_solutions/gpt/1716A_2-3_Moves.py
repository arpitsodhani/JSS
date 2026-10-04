import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    if n == 1:
        ans.append("2")
    else:
        ans.append(str((n + 2) // 3))

print("\n".join(ans))
