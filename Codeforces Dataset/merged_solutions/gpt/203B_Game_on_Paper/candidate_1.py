import sys

# CLAUSE: track_painted_cells
def new_state():
    return set(), {}

# CLAUSE: enumerate_affected_windows
def affected_windows(r, c):
    for top in range(r - 2, r + 1):
        for left in range(c - 2, c + 1):
            yield top, left

# CLAUSE: validate_window_bounds
def valid_anchor(top, left, n):
    return 1 <= top <= n - 2 and 1 <= left <= n - 2

# CLAUSE: update_window_occupancy
def apply_move(r, c, n, painted, occupied):
    if (r, c) in painted:
        return []
    painted.add((r, c))
    changed = []
    for top, left in affected_windows(r, c):
        if valid_anchor(top, left, n):
            key = (top, left)
            occupied[key] = occupied.get(key, 0) + 1
            changed.append(key)
    return changed

# CLAUSE: detect_completed_square
def completed(changed, occupied):
    return any(occupied[key] == 9 for key in changed)

# CLAUSE: preserve_earliest_move
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    painted, occupied = new_state()
    answer = -1
    p = 2
    for move in range(1, m + 1):
        r, c = data[p], data[p + 1]
        p += 2
        if answer == -1:
            changed = apply_move(r, c, n, painted, occupied)
            if completed(changed, occupied):
                answer = move
    print(answer)

main()
