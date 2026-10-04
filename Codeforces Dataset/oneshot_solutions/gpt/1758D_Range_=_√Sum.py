import sys

def build(n):
    if n % 2 == 0:
        m = n // 2
        skip = n // 2
        return [m + x for x in range(n + 1) if x != skip]
    else:
        m = (n + 3) // 2
        return [m + x for x in range(n + 2) if x != 1 and x != n - 1]

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

if len(data) == data[0] + 1:
    ns = data[1:]
else:
    ns = data

out = []
for n in ns:
    out.append(" ".join(map(str, build(n))))

sys.stdout.write("\n".join(out))
