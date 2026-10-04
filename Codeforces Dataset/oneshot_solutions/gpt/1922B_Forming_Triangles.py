import sys
from collections import Counter

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    cnt = Counter(a)
    total = 0
    prev = 0

    for x in sorted(cnt):
        c = cnt[x]
        if c >= 2:
            total += c * (c - 1) // 2 * prev
        if c >= 3:
            total += c * (c - 1) * (c - 2) // 6
        prev += c

    ans.append(str(total))

sys.stdout.write("\n".join(ans))
