# CLAUSE: setup_environment
import sys
from functools import lru_cache

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
x0, y0, n, d = data[:4]
moves = [(data[i], data[i + 1]) for i in range(4, 4 + 2 * n, 2)]
d2 = d * d

@lru_cache(None)
def win(x, y, cur, other):
    if not cur:
        if not win(y, x, other, 1):
            return True
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if nx * nx + ny * ny <= d2:
            if not win(nx, ny, other, cur):
                return True
    return False
print('Anton' if win(x0, y0, 0, 0) else 'Dasha')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
