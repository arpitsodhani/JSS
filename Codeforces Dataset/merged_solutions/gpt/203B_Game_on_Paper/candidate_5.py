import sys

# CLAUSE: track_painted_cells
def initialize(n):
    painted = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    occupied = {}
    return painted, occupied

# CLAUSE: enumerate_affected_windows
def walk_windows(r, c):
    top = r - 2
    while top <= r:
        left = c - 2
        while left <= c:
            yield top, left
            left += 1
        top += 1

# CLAUSE: validate_window_bounds
def clipped(top, left, n):
    if top < 1 or left < 1:
        return False
    if top > n - 2 or left > n - 2:
        return False
    return True

# CLAUSE: update_window_occupancy
def add_black_cell(r, c, n, painted, occupied):
    if painted[r][c]:
        return None
    painted[r][c] = True
    best = 0
    for top, left in walk_windows(r, c):
        if clipped(top, left, n):
            old = occupied.get((top, left), 0)
            now = old + 1
            occupied[(top, left)] = now
            if now > best:
                best = now
    return best

# CLAUSE: detect_completed_square
def square_is_complete(best_count):
    return best_count == 9

# CLAUSE: preserve_earliest_move
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if len(nums) < 2:
        return
    n = nums[0]
    m = nums[1]
    painted, occupied = initialize(n)
    earliest = -1
    cursor = 2
    for move_no in range(1, m + 1):
        r, c = nums[cursor], nums[cursor + 1]
        cursor += 2
        if earliest != -1:
            continue
        best_count = add_black_cell(r, c, n, painted, occupied)
        if square_is_complete(best_count):
            earliest = move_no
    print(earliest)

main()
