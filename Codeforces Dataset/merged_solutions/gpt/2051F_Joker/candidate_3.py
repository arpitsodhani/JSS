# CLAUSE: initialize_reachable_segments
import sys

def make_initial(m):
    return [(m, m)]

# CLAUSE: split_by_selected_position
def split_one_round(intervals, a):
    pieces = []
    found = False
    for l, r in intervals:
        left_l = l
        left_r = min(r, a - 1)
        if left_l <= left_r:
            pieces.append(("L", left_l, left_r))
        if l <= a <= r:
            found = True
        right_l = max(l, a + 1)
        right_r = r
        if right_l <= right_r:
            pieces.append(("R", right_l, right_r))
    return pieces, found

# CLAUSE: propagate_left_side_positions
def transform_left(l, r, n):
    end = r + 1
    if end > n:
        end = n
    return l, end

# CLAUSE: propagate_right_side_positions
def transform_right(l, r):
    begin = l - 1
    if begin < 1:
        begin = 1
    return begin, r

# CLAUSE: handle_joker_card_hit
def hit_ranges(found, n):
    return [(1, 1), (n, n)] if found else []

# CLAUSE: merge_adjacent_intervals
def compact(ranges):
    ranges = sorted(ranges)
    compacted = []
    for cur in ranges:
        if not compacted:
            compacted.append(cur)
            continue
        l, r = cur
        pl, pr = compacted[-1]
        if l <= pr + 1:
            compacted[-1] = (pl, max(pr, r))
        else:
            compacted.append(cur)
    return compacted

# CLAUSE: count_union_positions
def interval_size(ranges):
    return sum(b - a + 1 for a, b in ranges)

def solve_case(n, m, queries):
    intervals = make_initial(m)
    out = []
    for a in queries:
        pieces, found = split_one_round(intervals, a)
        generated = []
        for side, l, r in pieces:
            if side == "L":
                generated.append(transform_left(l, r, n))
            else:
                generated.append(transform_right(l, r))
        generated += hit_ranges(found, n)
        intervals = compact(generated)
        out.append(str(interval_size(intervals)))
    return " ".join(out)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    ans = []
    for _ in range(t):
        n, m, q = data[pos:pos + 3]
        pos += 3
        ans.append(solve_case(n, m, data[pos:pos + q]))
        pos += q
    sys.stdout.write("\n".join(ans))

main()
