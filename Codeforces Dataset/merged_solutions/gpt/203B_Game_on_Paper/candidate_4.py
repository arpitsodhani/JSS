import sys
from collections import defaultdict

# CLAUSE: track_painted_cells
def blank_state():
    painted = set()
    windows = defaultdict(int)
    return painted, windows

# CLAUSE: enumerate_affected_windows
def anchors_for_cell(r, c):
    starts = []
    for dr in range(3):
        for dc in range(3):
            starts.append((r - dr, c - dc))
    return starts

# CLAUSE: validate_window_bounds
def filter_valid(anchors, n):
    last = n - 2
    for top, left in anchors:
        if 1 <= top <= last and 1 <= left <= last:
            yield top, left

# CLAUSE: update_window_occupancy
def update_counts(r, c, n, painted, windows):
    if (r, c) in painted:
        return []
    painted.add((r, c))
    updated_values = []
    for top, left in filter_valid(anchors_for_cell(r, c), n):
        windows[(top, left)] += 1
        updated_values.append(windows[(top, left)])
    return updated_values

# CLAUSE: detect_completed_square
def found_completed(updated_values):
    return 9 in updated_values

# CLAUSE: preserve_earliest_move
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    painted, windows = blank_state()
    result = -1
    for i in range(m):
        r = int(raw[2 + 2 * i])
        c = int(raw[3 + 2 * i])
        if result == -1:
            values = update_counts(r, c, n, painted, windows)
            if found_completed(values):
                result = i + 1
    print(result)

main()
