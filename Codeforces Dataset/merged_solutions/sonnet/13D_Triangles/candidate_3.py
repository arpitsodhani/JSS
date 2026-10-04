# CLAUSE: setup_environment
import sys

def det(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

# CLAUSE: solve_logic
def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n, m = values[0], values[1]
    coords = values[2:]
    rx = [0] * n
    ry = [0] * n
    pos = 0
    for i in range(n):
        rx[i] = coords[pos]
        ry[i] = coords[pos + 1]
        pos += 2

    bx = [0] * m
    by = [0] * m
    for i in range(m):
        bx[i] = coords[pos]
        by[i] = coords[pos + 1]
        pos += 2

    if m == 0:
        sys.stdout.write(str(n * (n - 1) * (n - 2) // 6))
        return

    all_bits = (1 << m) - 1
    side = [0] * (n * n)

    for i in range(n):
        ax = rx[i]
        ay = ry[i]
        row = i * n
        for j in range(i + 1, n):
            mask = 0
            xj = rx[j]
            yj = ry[j]
            for b in range(m):
                if det(ax, ay, xj, yj, bx[b], by[b]) > 0:
                    mask |= 1 << b
            side[row + j] = mask
            side[j * n + i] = all_bits ^ mask

    total = 0
    for i in range(n - 2):
        ai = rx[i]
        bi = ry[i]
        base_i = i * n
        for j in range(i + 1, n - 1):
            aj = rx[j]
            bj = ry[j]
            base_j = j * n
            ij = side[base_i + j]
            ji = side[base_j + i]
            for k in range(j + 1, n):
                if det(ai, bi, aj, bj, rx[k], ry[k]) > 0:
                    mask = ij & side[base_j + k] & side[k * n + i]
                else:
                    mask = ji & side[k * n + j] & side[base_i + k]
                total += mask == 0

    sys.stdout.write(str(total))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
