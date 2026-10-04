# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
cnt = Counter()
ok = True
p = 1
for _ in range(n - 1):
    a, b = (data[p], data[p + 1])
    p += 2
    if a != n and b != n:
        ok = False
    else:
        x = b if a == n else a
        if x == n:
            ok = False
        cnt[x] += 1
if not ok:
    print('NO')
    sys.exit()
used = set(cnt)
free = [i for i in range(1, n) if i not in used]
ptr = 0
edges = []
for x in sorted(cnt):
    need = cnt[x] - 1
    chain = []
    while need:
        if ptr == len(free) or free[ptr] >= x:
            print('NO')
            sys.exit()
        chain.append(free[ptr])
        ptr += 1
        need -= 1
    prev = n
    for v in chain:
        edges.append((prev, v))
        prev = v
    edges.append((prev, x))
print('YES')
print('\n'.join((f'{u} {v}' for u, v in edges)))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
