import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
p = 2
a = []
for _ in range(n):
    x, y = data[p], data[p + 1]
    p += 2
    a.append((x, y))

b = []
for _ in range(m):
    x, y = data[p], data[p + 1]
    p += 2
    b.append((x, y))

possible = set()
bad = False

for x, y in a:
    cur = set()
    for u, v in b:
        s = {x, y} & {u, v}
        if len(s) == 1:
            cur.add(next(iter(s)))
    if len(cur) > 1:
        bad = True
    possible |= cur

for u, v in b:
    cur = set()
    for x, y in a:
        s = {x, y} & {u, v}
        if len(s) == 1:
            cur.add(next(iter(s)))
    if len(cur) > 1:
        bad = True

if bad:
    print(-1)
elif len(possible) == 1:
    print(next(iter(possible)))
else:
    print(0)
