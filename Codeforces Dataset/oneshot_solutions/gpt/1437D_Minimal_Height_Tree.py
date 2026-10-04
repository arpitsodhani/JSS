import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    q = deque([1])
    pos = 1
    height = 0

    while pos < n:
        height += 1
        cnt = 0
        for _ in range(len(q)):
            if pos >= n:
                break
            cnt += 1
            pos += 1
            while pos < n and a[pos - 1] < a[pos]:
                cnt += 1
                pos += 1
        q = deque([1] * cnt)

    out.append(str(height))

sys.stdout.write("\n".join(out))
