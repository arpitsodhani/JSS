# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def ceil_div(a, b):
    return (a + b - 1) // b

def solve_case(n, x, y, d):
    if abs(x - y) % d == 0:
        return abs(x - y) // d
    ans = 10 ** 18
    if (y - 1) % d == 0:
        ans = min(ans, ceil_div(x - 1, d) + (y - 1) // d)
    if (n - y) % d == 0:
        ans = min(ans, ceil_div(n - x, d) + (n - y) // d)
    return -1 if ans == 10 ** 18 else ans
data = list(map(int, sys.stdin.read().split()))
t = data[0]
out = []
idx = 1
for _ in range(t):
    n, x, y, d = data[idx:idx + 4]
    idx += 4
    out.append(str(solve_case(n, x, y, d)))
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
