# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, k):
    cnt = 1
    ans = 0
    while n >= k:
        if n & 1:
            ans += cnt * ((n + 1) // 2)
        n //= 2
        cnt *= 2
    return ans

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    out.append(str(solve_case(n, k)))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
