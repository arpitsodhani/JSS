import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

t = data[0]
ans = []
idx = 1

for _ in range(t):
    n, m = data[idx], data[idx + 1]
    idx += 2
    if n == 1 and m == 1:
        ans.append("0")
    elif n == 1 or m == 1:
        ans.append("1")
    else:
        ans.append("2")

print("\n".join(ans))
