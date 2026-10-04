# CLAUSE: initialize_reachable_segments
import sys

def start_segments(m):
    return [(m, m)]

# CLAUSE: split_by_selected_position
def split_segments(segments, a):
    left = []
    right = []
    hit = False
    for l, r in segments:
        if l < a:
            left.append((l, min(r, a - 1)))
        if l <= a <= r:
            hit = True
        if a < r:
            right.append((max(l, a + 1), r))
    return left, hit, right

# CLAUSE: propagate_left_side_positions
def move_left_parts(parts, n):
    return [(l, min(n, r + 1)) for l, r in parts]

# CLAUSE: propagate_right_side_positions
def move_right_parts(parts):
    return [(max(1, l - 1), r) for l, r in parts]

# CLAUSE: handle_joker_card_hit
def add_hit_intervals(hit, n):
    if hit:
        return [(1, 1), (n, n)]
    return []

# CLAUSE: merge_adjacent_intervals
def merge_intervals(items):
    if not items:
        return []
    items.sort()
    merged = [items[0]]
    for l, r in items[1:]:
        last_l, last_r = merged[-1]
        if l <= last_r + 1:
            if r > last_r:
                merged[-1] = (last_l, r)
        else:
            merged.append((l, r))
    return merged

# CLAUSE: count_union_positions
def total_positions(segments):
    return sum(r - l + 1 for l, r in segments)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    answers = []
    for _ in range(t):
        n, m, q = data[ptr], data[ptr + 1], data[ptr + 2]
        ptr += 3
        segments = start_segments(m)
        row = []
        for a in data[ptr:ptr + q]:
            left, hit, right = split_segments(segments, a)
            produced = move_left_parts(left, n)
            produced.extend(move_right_parts(right))
            produced.extend(add_hit_intervals(hit, n))
            segments = merge_intervals(produced)
            row.append(str(total_positions(segments)))
        ptr += q
        answers.append(" ".join(row))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
