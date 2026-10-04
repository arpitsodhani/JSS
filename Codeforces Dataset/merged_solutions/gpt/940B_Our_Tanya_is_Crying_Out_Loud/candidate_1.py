# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n, k, A, B = map(int, sys.stdin.read().split())

if k == 1:
    print((n - 1) * A)
else:
    ans = 0
    while n > 1:
        if n < k:
            ans += (n - 1) * A
            break
        r = n % k
        if r:
            ans += r * A
            n -= r
        else:
            nxt = n // k
            ans += min(B, (n - nxt) * A)
            n = nxt
    print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
