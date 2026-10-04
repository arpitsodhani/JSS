import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
edges = []
p = 1
for _ in range(n - 1):
    u = data[p]
    v = data[p + 1]
    p += 2
    edges.append((u, v))

out = ["!"]
out.extend(f"{u} {v}" for u, v in edges)
sys.stdout.write("\n".join(out))
