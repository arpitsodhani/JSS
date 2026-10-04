# Clause initialize_reachable_segments [Confidence: 0.80]
import sys

def make_initial(m):
    return [(m, m)]


# Clause split_by_selected_position [Confidence: 0.60]
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


# Clause propagate_left_side_positions [Confidence: 0.40]
def emit_left(parts, n, out):
    for l, r in parts:
        nr = r + 1
        if nr > n:
            nr = n
        out.append([l, nr])


# Clause propagate_right_side_positions [Confidence: 0.40]
def push_right_bucket(bucket, target):
    for l, r in bucket:
        target.append((l - 1 if l > 1 else 1, r))


# Clause handle_joker_card_hit [Confidence: 0.60]
def add_hit(has_hit, n, pairs):
    if has_hit:
        pairs.append((1, 1))
        pairs.append((n, n))


# Clause merge_adjacent_intervals [Confidence: 0.60]
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


# Clause count_union_positions [Confidence: 1.00]
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


