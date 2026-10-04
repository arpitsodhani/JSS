import sys

# CLAUSE: track_painted_cells
def create_tables(n):
    black = [[False] * (n + 2) for _ in range(n + 2)]
    count = [[0] * (n + 2) for _ in range(n + 2)]
    return black, count

# CLAUSE: enumerate_affected_windows
def local_anchor_ranges(r, c):
    return range(r - 2, r + 1), range(c - 2, c + 1)

# CLAUSE: validate_window_bounds
def anchor_inside(top, left, limit):
    return 1 <= top and top + 2 <= limit and 1 <= left and left + 2 <= limit

# CLAUSE: update_window_occupancy
def paint_cell(r, c, n, black, count):
    if black[r][c]:
        return ()
    black[r][c] = True
    touched = []
    rows, cols = local_anchor_ranges(r, c)
    for top in rows:
        for left in cols:
            if anchor_inside(top, left, n):
                count[top][left] += 1
                touched.append((top, left))
    return touched

# CLAUSE: detect_completed_square
def has_full_square(touched, count):
    for top, left in touched:
        if count[top][left] == 9:
            return True
    return False

# CLAUSE: preserve_earliest_move
def main():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    if not values:
        return
    n, m = values[:2]
    black, count = create_tables(n)
    ans = -1
    idx = 2
    for step in range(1, m + 1):
        r = values[idx]
        c = values[idx + 1]
        idx += 2
        if ans < 0:
            touched = paint_cell(r, c, n, black, count)
            if has_full_square(touched, count):
                ans = step
    sys.stdout.write(str(ans))

main()
