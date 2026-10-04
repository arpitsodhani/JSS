import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    x = data[idx + 1]
    idx += 2
    a = data[idx:idx + n]
    idx += n

    total = sum(a)
    mn = (total + x - 1) // x
    mx = sum((v + x - 1) // x for v in a)
    out.append(f"{mn} {mx}")

print("\n".join(out))
