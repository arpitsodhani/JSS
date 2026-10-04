# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
out = []
p = 1

for _ in range(t):
    l, r, G = data[p], data[p + 1], data[p + 2]
    p += 3

    L = (l + G - 1) // G
    R = r // G

    if L > R:
        out.append("-1 -1")
        continue

    best_x = -1
    best_y = -1
    best_d = -1

    lim = min(R - L + 1, 2000)

    for x in range(L, L + lim):
        if R - x < best_d:
            break
        for y in range(R, R - lim, -1):
            if y < x:
                break
            d = y - x
            if d < best_d:
                break
            if gcd(x, y) == 1:
                if d > best_d or (d == best_d and x < best_x):
                    best_d = d
                    best_x = x
                    best_y = y
                break

    if best_x == -1:
        out.append("-1 -1")
    else:
        out.append(f"{best_x * G} {best_y * G}")

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
