# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
x = int(sys.stdin.readline())

ans = []
ops = 0

def good(v):
    return v & (v + 1) == 0

while not good(x):
    m = x.bit_length()
    p = -1
    for i in range(m - 1, -1, -1):
        if not (x >> i) & 1:
            p = i + 1
            break

    ans.append(p)
    ops += 1
    x ^= (1 << p) - 1

    if good(x):
        break

    x += 1
    ops += 1

print(ops)
if ans:
    print(*ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
