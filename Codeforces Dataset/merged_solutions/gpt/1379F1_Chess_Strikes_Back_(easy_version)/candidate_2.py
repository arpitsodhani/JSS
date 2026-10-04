import sys

# CLAUSE: normalize_white_coordinates
def normalize_white_coordinates(row, col):
    block_row = (row - 1) // 2 + 1
    block_col = (col - 1) // 2 + 1
    family = 0 if row % 2 else 1
    return block_row, block_col, family

# CLAUSE: classify_forbidden_side
def classify_forbidden_side(r, c, family):
    if family == 0:
        return r, c, -1
    return r, c, 1

# CLAUSE: accumulate_prefix_constraints
def accumulate_prefix_constraints(events, length):
    active = {}
    for i in range(length):
        r, c, side = events[i]
        active[(r, c, side)] = side
    return active

# CLAUSE: derive_frontier_bounds
def derive_frontier_bounds(active, n, m):
    bottom = [0] * (n + 2)
    top = [m] * (n + 2)
    for r, c, side in active:
        if side < 0:
            top[r] = min(top[r], c - 1)
        else:
            bottom[r] = max(bottom[r], c)
    return bottom, top

# CLAUSE: validate_monotone_separator
def validate_monotone_separator(bottom, top, n, m):
    allowed = m
    row = 1
    while row <= n:
        allowed = min(allowed, top[row])
        if bottom[row] > allowed:
            return False
        row += 1
    return True

# CLAUSE: locate_failure_prefix
def locate_failure_prefix(n, m, q, events):
    def feasible(taken):
        active = accumulate_prefix_constraints(events, taken)
        bottom, top = derive_frontier_bounds(active, n, m)
        return validate_monotone_separator(bottom, top, n, m)

    if feasible(q):
        return q + 1

    lo, hi = 0, q
    while hi - lo > 1:
        mid = (lo + hi) >> 1
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    return hi

# CLAUSE: emit_monotone_answers
def emit_monotone_answers(count, failure):
    sys.stdout.write("\n".join("YES" if i < failure else "NO" for i in range(1, count + 1)))

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    m = int(raw[1])
    q = int(raw[2])
    events = []
    p = 3
    for _ in range(q):
        x = int(raw[p])
        y = int(raw[p + 1])
        p += 2
        events.append(classify_forbidden_side(*normalize_white_coordinates(x, y)))
    emit_monotone_answers(q, locate_failure_prefix(n, m, q, events))

main()
