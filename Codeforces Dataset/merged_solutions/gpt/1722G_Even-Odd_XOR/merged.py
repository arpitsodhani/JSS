# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    res = []
    base = 1 << 20

    while n > 0:
        if n == 3:
            res.extend([base, base + 1, 1])
            n -= 3
            base += 1 << 20
        else:
            res.extend([0 + base, 1 + base, 2 + base, 3 + base])
            n -= 4
            base += 1 << 20

    ans.append(" ".join(map(str, res)))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
