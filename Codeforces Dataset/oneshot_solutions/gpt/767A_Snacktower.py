import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr = data[1:]

seen = [False] * (n + 1)
need = n
out = []

for x in arr:
    seen[x] = True
    line = []
    while need > 0 and seen[need]:
        line.append(str(need))
        need -= 1
    out.append(" ".join(line))

sys.stdout.write("\n".join(out))
