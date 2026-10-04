import sys

# CLAUSE: normalize_white_coordinates
def normalize_white_coordinates(x, y):
    return (x + 1) // 2, (y + 1) // 2, x & 1

# CLAUSE: classify_forbidden_side
def classify_forbidden_side(cell):
    r, c, odd_row = cell
    if odd_row:
        return 0, r, c
    return 1, r, c

# CLAUSE: accumulate_prefix_constraints
def accumulate_prefix_constraints(items, k, n, m):
    low = [0] * (n + 1)
    high = [m] * (n + 1)
    seen = set()
    for idx in range(k):
        kind, r, c = items[idx]
        key = (kind, r, c)
        if key in seen:
            continue
        seen.add(key)
        if kind == 0:
            if c - 1 < high[r]:
                high[r] = c - 1
        else:
            if c > low[r]:
                low[r] = c
    return low, high

# CLAUSE: derive_frontier_bounds
def derive_frontier_bounds(low, high):
    return low, high

# CLAUSE: validate_monotone_separator
def validate_monotone_separator(low, high, n, m):
    cur = m
    for r in range(1, n + 1):
        if high[r] < cur:
            cur = high[r]
        if cur < low[r]:
            return False
    return True

# CLAUSE: locate_failure_prefix
def locate_failure_prefix(n, m, q, constraints):
    def ok(k):
        low, high = accumulate_prefix_constraints(constraints, k, n, m)
        low, high = derive_frontier_bounds(low, high)
        return validate_monotone_separator(low, high, n, m)

    if ok(q):
        return q + 1
    left, right = 1, q
    while left < right:
        mid = (left + right) // 2
        if ok(mid):
            left = mid + 1
        else:
            right = mid
    return left

# CLAUSE: emit_monotone_answers
def emit_monotone_answers(q, first_bad):
    out = []
    for i in range(1, q + 1):
        out.append("YES" if i < first_bad else "NO")
    sys.stdout.write("\n".join(out))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, q = data[:3]
    constraints = []
    pos = 3
    for _ in range(q):
        x, y = data[pos], data[pos + 1]
        pos += 2
        constraints.append(classify_forbidden_side(normalize_white_coordinates(x, y)))
    first_bad = locate_failure_prefix(n, m, q, constraints)
    emit_monotone_answers(q, first_bad)

main()
