import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    if n % 2 == 0:
        ans.append("-1")
    else:
        p = [1, n]
        p.extend(range(2, n))
        ans.append(" ".join(map(str, p)))

print("\n".join(ans))
