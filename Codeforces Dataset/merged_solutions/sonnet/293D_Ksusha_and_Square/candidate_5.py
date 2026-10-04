# CLAUSE: setup_environment
import sys

def ceil_ratio(a, b):
    q, r = divmod(a, b)
    return q + (1 if r else 0)

def feed_edge(low, high, shift, x1, y1, x2, y2):
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        pos = x1 + shift
        low[pos] = min(low[pos], y1)
        high[pos] = max(high[pos], y2)
        return

    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    dx = x2 - x1
    dy = y2 - y1
    start = y1 * dx
    pos = x1 + shift
    for add in range(dx + 1):
        cur = start + dy * add
        low[pos + add] = min(low[pos + add], ceil_ratio(cur, dx))
        high[pos + add] = max(high[pos + add], cur // dx)

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    coords = data[1:]
    points = list(zip(coords[0::2], coords[1::2]))

    min_x = points[0][0]
    max_x = points[0][0]
    for x, y in points:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

    shift = -min_x
    width = max_x - min_x + 1
    inf = 10 ** 25
    low = [inf for _ in range(width)]
    high = [-inf for _ in range(width)]

    prev_x, prev_y = points[-1]
    for cur_x, cur_y in points:
        feed_edge(low, high, shift, prev_x, prev_y, cur_x, cur_y)
        prev_x, prev_y = cur_x, cur_y

    count = 0
    sx = 0
    sy = 0
    sq = 0

    for pos in range(width):
        lo = low[pos]
        hi = high[pos]
        if lo <= hi:
            x = pos - shift
            c = hi - lo + 1
            y_sum = (lo + hi) * c // 2
            a = lo - 1
            y_sq = hi * (hi + 1) * (2 * hi + 1) // 6 - a * (a + 1) * (2 * a + 1) // 6
            count += c
            sx += x * c
            sy += y_sum
            sq += x * x * c + y_sq

    result = (count * sq - sx * sx - sy * sy) / (count * (count - 1))
    sys.stdout.write("{:.10f}\n".format(result))

# CLAUSE: finish_program
main()
