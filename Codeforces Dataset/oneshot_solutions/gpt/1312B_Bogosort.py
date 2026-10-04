import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    a.sort(reverse=True)
    out.append(" ".join(map(str, a)))

sys.stdout.write("\n".join(out))
