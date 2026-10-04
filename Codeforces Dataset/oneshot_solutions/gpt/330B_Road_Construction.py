import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
used = [False] * (n + 1)

idx = 2
for _ in range(m):
    a, b = data[idx], data[idx + 1]
    idx += 2
    used[a] = True
    used[b] = True

center = 1
for i in range(1, n + 1):
    if not used[i]:
        center = i
        break

out = [str(n - 1)]
for i in range(1, n + 1):
    if i != center:
        out.append(f"{center} {i}")

print("\n".join(out))
