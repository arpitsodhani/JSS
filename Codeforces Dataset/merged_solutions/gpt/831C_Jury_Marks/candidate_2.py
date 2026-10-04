# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
k, n = (data[0], data[1])
a = data[2:2 + k]
b = data[2 + k:2 + k + n]
pref = []
cur = 0
for x in a:
    cur += x
    pref.append(cur)
pref_set = set(pref)
ans = set()
for p in pref:
    start = b[0] - p
    ok = True
    for val in b:
        if val - start not in pref_set:
            ok = False
            break
    if ok:
        ans.add(start)
print(len(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
