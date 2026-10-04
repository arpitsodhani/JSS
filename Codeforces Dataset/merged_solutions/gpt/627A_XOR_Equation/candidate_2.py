# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s, x = map(int, input().split())
d = s - x
if d < 0 or d % 2:
    print(0)
else:
    c = d // 2
    if c & x:
        print(0)
    else:
        ans = 1 << x.bit_count()
        if c == 0:
            ans -= 2
        print(max(ans, 0))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
