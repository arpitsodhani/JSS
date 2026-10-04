# Clause track_painted_cells [Confidence: 0.40]
import sys

def create_tables(n):
    black = [[False] * (n + 2) for _ in range(n + 2)]
    count = [[0] * (n + 2) for _ in range(n + 2)]
    return black, count


# Clause enumerate_affected_windows [Confidence: 0.40]
def affected_windows(r, c):
    for top in range(r - 2, r + 1):
        for left in range(c - 2, c + 1):
            yield top, left


# Clause validate_window_bounds [Confidence: 0.60]
def anchor_inside(top, left, limit):
    return 1 <= top and top + 2 <= limit and 1 <= left and left + 2 <= limit


# Clause update_window_occupancy [Confidence: 0.80]
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


# Clause detect_completed_square [Confidence: 0.40]
def found_completed(updated_values):
    return 9 in updated_values


# Clause preserve_earliest_move [Confidence: 1.00]
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


