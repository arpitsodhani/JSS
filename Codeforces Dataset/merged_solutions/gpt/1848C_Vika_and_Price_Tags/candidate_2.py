# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def residue(a, b):
    if a == 0 and b == 0:
        return -1
    ans = 0
    while a and b:
        if a < b:
            a, b = (b, a)
            ans += 1
        q = a // b
        ans += q
        a %= b
    if a == 0:
        return ans % 3
    return (ans + 2) % 3
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
p = 1
out = []
for _ in range(t):
    n = data[p]
    p += 1
    a = data[p:p + n]
    p += n
    b = data[p:p + n]
    p += n
    need = -1
    ok = True
    for x, y in zip(a, b):
        r = residue(x, y)
        if r == -1:
            continue
        if need == -1:
            need = r
        elif need != r:
            ok = False
            break
    out.append('YES' if ok else 'NO')
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
