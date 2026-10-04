# CLAUSE: initialize_reachable_segments
import sys

def initialize(m):
    starts = [m]
    ends = [m]
    return starts, ends

# CLAUSE: split_by_selected_position
def split(starts, ends, a):
    left_starts = []
    left_ends = []
    right_starts = []
    right_ends = []
    has_hit = False
    for i in range(len(starts)):
        l = starts[i]
        r = ends[i]
        if l < a:
            left_starts.append(l)
            left_ends.append(min(r, a - 1))
        if l <= a <= r:
            has_hit = True
        if a < r:
            right_starts.append(max(l, a + 1))
            right_ends.append(r)
    return left_starts, left_ends, has_hit, right_starts, right_ends

# CLAUSE: propagate_left_side_positions
def add_left(left_starts, left_ends, n, pairs):
    for i in range(len(left_starts)):
        l = left_starts[i]
        r = left_ends[i] + 1
        if r > n:
            r = n
        pairs.append((l, r))

# CLAUSE: propagate_right_side_positions
def add_right(right_starts, right_ends, pairs):
    for i in range(len(right_starts)):
        l = right_starts[i] - 1
        if l < 1:
            l = 1
        pairs.append((l, right_ends[i]))

# CLAUSE: handle_joker_card_hit
def add_hit(has_hit, n, pairs):
    if has_hit:
        pairs.append((1, 1))
        pairs.append((n, n))

# CLAUSE: merge_adjacent_intervals
def merge_to_arrays(pairs):
    pairs.sort()
    starts = []
    ends = []
    for l, r in pairs:
        if starts and l <= ends[-1] + 1:
            if r > ends[-1]:
                ends[-1] = r
        else:
            starts.append(l)
            ends.append(r)
    return starts, ends

# CLAUSE: count_union_positions
def count(starts, ends):
    s = 0
    for i in range(len(starts)):
        s += ends[i] - starts[i] + 1
    return s

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    lines = []
    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        q = data[p + 2]
        p += 3
        starts, ends = initialize(m)
        line = []
        for a in data[p:p + q]:
            ls, le, hit, rs, re = split(starts, ends, a)
            pairs = []
            add_left(ls, le, n, pairs)
            add_right(rs, re, pairs)
            add_hit(hit, n, pairs)
            starts, ends = merge_to_arrays(pairs)
            line.append(str(count(starts, ends)))
        p += q
        lines.append(" ".join(line))
    sys.stdout.write("\n".join(lines))

solve()
