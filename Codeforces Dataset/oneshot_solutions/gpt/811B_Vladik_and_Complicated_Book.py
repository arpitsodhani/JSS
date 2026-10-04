import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
p = [0] + data[2:2 + n]
idx = 2 + n
ans = []

for _ in range(m):
    l, r, x = data[idx], data[idx + 1], data[idx + 2]
    idx += 3

    if x < l or x > r:
        ans.append("Yes")
        continue

    smaller = 0
    value = p[x]
    for i in range(l, r + 1):
        if p[i] < value:
            smaller += 1

    ans.append("Yes" if l + smaller == x else "No")

sys.stdout.write("\n".join(ans))
