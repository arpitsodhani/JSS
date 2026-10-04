# Clause normalize_white_coordinates [Confidence: 0.60]
import sys

def normalize_white_coordinates(row, col):
    block_row = (row - 1) // 2 + 1
    block_col = (col - 1) // 2 + 1
    family = 0 if row % 2 else 1
    return block_row, block_col, family


# Clause classify_forbidden_side [Confidence: 0.60]
def classify_forbidden_side(row, col, family):
    if family:
        return row, col, 0
    return row, col, 1


# Clause accumulate_prefix_constraints [Confidence: 0.40]
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


# Clause derive_frontier_bounds [Confidence: 0.40]
def derive_frontier_bounds(by_row, n, m):
    lo = [0] * (n + 1)
    hi = [m] * (n + 1)
    for r, pair in by_row.items():
        caps, floors = pair
        if caps:
            hi[r] = min(caps) - 1
        if floors:
            lo[r] = max(floors)
    return lo, hi


# Clause validate_monotone_separator [Confidence: 0.80]
def validate_monotone_separator(low, high, n, m):
    cur = m
    for r in range(1, n + 1):
        if high[r] < cur:
            cur = high[r]
        if cur < low[r]:
            return False
    return True


# Clause locate_failure_prefix [Confidence: 1.00]
def locate_failure_prefix(n, m, q, records):
    def possible(k):
        lower, upper = accumulate_prefix_constraints(records, k, m, n)
        bounds = derive_frontier_bounds(lower, upper)
        return validate_monotone_separator(bounds, m, n)

    if possible(q):
        return q + 1
    low, high = 1, q
    while low < high:
        middle = (low + high) // 2
        if possible(middle):
            low = middle + 1
        else:
            high = middle
    return low


# Clause emit_monotone_answers [Confidence: 1.00]
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


