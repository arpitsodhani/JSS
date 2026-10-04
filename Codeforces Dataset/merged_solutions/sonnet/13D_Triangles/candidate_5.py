# CLAUSE: setup_environment
import sys

def choose3(x):
    return x * (x - 1) * (x - 2) // 6

# CLAUSE: solve_logic
def run():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    if not data:
        return

    n = data[0]
    m = data[1]
    at = 2

    red = []
    for _ in range(n):
        red.append((data[at], data[at + 1]))
        at += 2

    blue = []
    for _ in range(m):
        blue.append((data[at], data[at + 1]))
        at += 2

    if m == 0:
        print(choose3(n))
        return

    full = (1 << m) - 1
    left = [[0] * n for _ in range(n)]

    for i, (ax, ay) in enumerate(red):
        for j in range(i + 1, n):
            bx, by = red[j]
            dx = bx - ax
            dy = by - ay
            bits = 0
            bit = 1
            for cx, cy in blue:
                if dx * (cy - ay) - dy * (cx - ax) > 0:
                    bits |= bit
                bit <<= 1
            left[i][j] = bits
            left[j][i] = full ^ bits

    count = 0
    for i in range(n):
        ax, ay = red[i]
        for j in range(i + 1, n):
            bx, by = red[j]
            first = left[i][j]
            reverse = left[j][i]
            dx = bx - ax
            dy = by - ay
            for k in range(j + 1, n):
                cx, cy = red[k]
                if dx * (cy - ay) - dy * (cx - ax) > 0:
                    inside = first & left[j][k] & left[k][i]
                else:
                    inside = reverse & left[k][j] & left[i][k]
                if inside == 0:
                    count += 1

    print(count)

# CLAUSE: finish_program
run()
