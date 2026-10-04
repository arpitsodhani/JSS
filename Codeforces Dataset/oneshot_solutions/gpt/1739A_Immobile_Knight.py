import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

t = data[0]
ans = []
idx = 1

for _ in range(t):
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    ans.append(f"{min(n, 2)} {min(m, 2)}")

print("\n".join(ans))
