# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    pos = [0] * (n + 1)
    for i, x in enumerate(p):
        pos[x] = i

    ans = 0
    l = r = pos[1]
    for x in range(2, n + 1):
        if l < pos[x] < r:
            continue
        ans += 1
        l = min(l, pos[x])
        r = max(r, pos[x])

    print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
