import sys
from collections import Counter

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    cnt = Counter(a)
    if len(cnt) == 1:
        ans.append("Yes")
    elif len(cnt) == 2:
        c = sorted(cnt.values())
        ans.append("Yes" if c[1] - c[0] <= 1 else "No")
    else:
        ans.append("No")

print("\n".join(ans))
