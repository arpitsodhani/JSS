# CLAUSE: setup_environment
import sys

def up_div(a, b):
    return -((-a) // b)

def add_interval(lo, hi, pos, a, b):
    if a < lo[pos]:
        lo[pos] = a
    if b > hi[pos]:
        hi[pos] = b

# CLAUSE: solve_logic
def collect_columns(points):
    xs = [p[0] for p in points]
    base = min(xs)
    size = max(xs) - base + 1
    big = 10 ** 30
    lo = [big] * size
    hi = [-big] * size

    m = len(points)
    for i in range(m):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % m]

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            add_interval(lo, hi, x1 - base, y1, y2)
            continue

        if x2 < x1:
            x1, y1, x2, y2 = x2, y2, x1, y1

        dx = x2 - x1
        dy = y2 - y1
        pos = x1 - base
        for step in range(dx + 1):
            value = y1 * dx + dy * step
            add_interval(lo, hi, pos + step, up_div(value, dx), value // dx)

    return base, lo, hi

def solve(points):
    base, lo, hi = collect_columns(points)
    total = sum_x = sum_y = sum_norm = 0

    for pos, left in enumerate(lo):
        right = hi[pos]
        if left > right:
            continue
        x = base + pos
        amount = right - left + 1
        last = amount - 1
        y_sum = amount * (left + right) // 2
        y_sq_sum = amount * left * left + left * amount * last + amount * last * (2 * last + 1) // 6

        total += amount
        sum_x += x * amount
        sum_y += y_sum
        sum_norm += x * x * amount + y_sq_sum

    return (total * sum_norm - sum_x * sum_x - sum_y * sum_y) / (total * (total - 1))

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    points = [(values[i], values[i + 1]) for i in range(1, 2 * n, 2)]
    sys.stdout.write(f"{solve(points):.10f}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
