# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
points = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]
ans = 0
for x, y in points:
    left = right = upper = lower = False
    for x2, y2 in points:
        if y2 == y:
            if x2 < x:
                left = True
            elif x2 > x:
                right = True
        if x2 == x:
            if y2 < y:
                lower = True
            elif y2 > y:
                upper = True
    if left and right and upper and lower:
        ans += 1
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
