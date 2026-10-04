# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def can_make(s, t):
    i = len(s) - 1
    for j in range(len(t) - 1, -1, -1):
        while i >= 0 and s[i] != t[j]:
            i -= 2
        if i < 0:
            return False
        i -= 1
    return True
data = sys.stdin.read().strip().split()
q = int(data[0])
out = []
p = 1
for _ in range(q):
    s = data[p]
    t = data[p + 1]
    p += 2
    out.append('YES' if can_make(s, t) else 'NO')
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
