# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
t = data[0]
pos = 1
ans = []
for _ in range(t):
    n = data[pos]
    pos += 1
    a = data[pos:pos + n]
    pos += n
    res = 1
    for i, x in enumerate(a, 1):
        if i == x:
            res = i
            break
    ans.append(str(res))
sys.stdout.write('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
