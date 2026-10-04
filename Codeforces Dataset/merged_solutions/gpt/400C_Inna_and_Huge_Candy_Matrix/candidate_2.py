# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
n, m, x, y, z, p = data[:6]
coords = data[6:]

def rotate_cw(r, c, rows, cols):
    return (c, rows - r + 1, cols, rows)

def rotate_ccw(r, c, rows, cols):
    return (cols - c + 1, r, cols, rows)
out = []
for i in range(0, 2 * p, 2):
    r, c = (coords[i], coords[i + 1])
    rows, cols = (n, m)
    for _ in range(x % 4):
        r, c, rows, cols = rotate_cw(r, c, rows, cols)
    if y % 2:
        c = cols - c + 1
    for _ in range(z % 4):
        r, c, rows, cols = rotate_ccw(r, c, rows, cols)
    out.append(f'{r} {c}')
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
