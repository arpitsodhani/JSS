import sys

data = sys.stdin.buffer.read().decode().split()
idx = 0

n = int(data[idx])
idx += 1
m = int(data[idx])
idx += 1

v = [0] * (n + 1)
for i in range(1, n + 1):
    v[i] = int(data[idx])
    idx += 1

total = 0
for _ in range(m):
    x = int(data[idx])
    idx += 1
    y = int(data[idx])
    idx += 1
    total += min(v[x], v[y])

print(total)
