# CLAUSE: setup_environment
import sys

def ceiling_fraction(num, den):
    return -((-num) // den)

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    pts = []
    for j in range(n):
        pts.append((raw[1 + 2 * j], raw[2 + 2 * j]))

    columns = {}

    for a in range(n):
        x1, y1 = pts[a]
        x2, y2 = pts[(a + 1) % n]

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            old = columns.get(x1)
            if old is None:
                columns[x1] = [y1, y2]
            else:
                if y1 < old[0]:
                    old[0] = y1
                if y2 > old[1]:
                    old[1] = y2
            continue

        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        dx = x2 - x1
        dy = y2 - y1
        numerator = y1 * dx
        for x in range(x1, x2 + 1):
            bottom = ceiling_fraction(numerator, dx)
            top = numerator // dx
            old = columns.get(x)
            if old is None:
                columns[x] = [bottom, top]
            else:
                if bottom < old[0]:
                    old[0] = bottom
                if top > old[1]:
                    old[1] = top
            numerator += dy

    count = sum_x = sum_y = sum_square = 0

    for x, bounds in columns.items():
        lo, hi = bounds
        if lo <= hi:
            length = hi - lo + 1
            end = length - 1
            y_total = length * (lo + hi) // 2
            y_square = length * lo * lo + lo * length * end + length * end * (2 * end + 1) // 6
            count += length
            sum_x += x * length
            sum_y += y_total
            sum_square += x * x * length + y_square

    value = (count * sum_square - sum_x * sum_x - sum_y * sum_y) / (count * (count - 1))
    print("%.10f" % value)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
