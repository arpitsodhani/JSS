# CLAUSE: initialize_reachable_segments
import sys

def initial_state(m):
    segs = [[m, m]]
    return segs

# CLAUSE: split_by_selected_position
def append_split_parts(segs, a, left_parts, right_parts):
    touched = False
    for bounds in segs:
        l = bounds[0]
        r = bounds[1]
        if l <= a - 1:
            left_parts.append([l, a - 1 if a - 1 < r else r])
        if l <= a and a <= r:
            touched = True
        if a + 1 <= r:
            right_parts.append([a + 1 if a + 1 > l else l, r])
    return touched

# CLAUSE: propagate_left_side_positions
def emit_left(parts, n, out):
    for l, r in parts:
        nr = r + 1
        if nr > n:
            nr = n
        out.append([l, nr])

# CLAUSE: propagate_right_side_positions
def emit_right(parts, out):
    for l, r in parts:
        nl = l - 1
        if nl < 1:
            nl = 1
        out.append([nl, r])

# CLAUSE: handle_joker_card_hit
def emit_hit(was_hit, n, out):
    if was_hit:
        out.append([1, 1])
        out.append([n, n])

# CLAUSE: merge_adjacent_intervals
def normalize(segs):
    segs.sort(key=lambda p: (p[0], p[1]))
    res = []
    for l, r in segs:
        if res and l <= res[-1][1] + 1:
            if r > res[-1][1]:
                res[-1][1] = r
        else:
            res.append([l, r])
    return res

# CLAUSE: count_union_positions
def covered_count(segs):
    ans = 0
    for l, r in segs:
        ans += r - l + 1
    return ans

def solve():
    vals = list(map(int, sys.stdin.buffer.read().split()))
    t = vals[0]
    at = 1
    lines = []
    for _ in range(t):
        n = vals[at]
        m = vals[at + 1]
        q = vals[at + 2]
        at += 3
        segs = initial_state(m)
        counts = []
        for _ in range(q):
            a = vals[at]
            at += 1
            left_parts = []
            right_parts = []
            was_hit = append_split_parts(segs, a, left_parts, right_parts)
            nxt = []
            emit_left(left_parts, n, nxt)
            emit_right(right_parts, nxt)
            emit_hit(was_hit, n, nxt)
            segs = normalize(nxt)
            counts.append(str(covered_count(segs)))
        lines.append(" ".join(counts))
    print("\n".join(lines))

solve()
