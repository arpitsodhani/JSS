import sys

# CLAUSE: normalize_white_coordinates
def normalize_white_coordinates(x, y):
    return {
        "r": (x + 1) // 2,
        "c": (y + 1) // 2,
        "family": x % 2,
    }

# CLAUSE: classify_forbidden_side
def classify_forbidden_side(cell):
    if cell["family"] == 1:
        return ("cap", cell["r"], cell["c"])
    return ("floor", cell["r"], cell["c"])

# CLAUSE: accumulate_prefix_constraints
def accumulate_prefix_constraints(queries, prefix):
    by_row = {}
    for i in range(prefix):
        tag, r, c = queries[i]
        pack = by_row.get(r)
        if pack is None:
            pack = [set(), set()]
            by_row[r] = pack
        if tag == "cap":
            pack[0].add(c)
        else:
            pack[1].add(c)
    return by_row

# CLAUSE: derive_frontier_bounds
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

# CLAUSE: validate_monotone_separator
def validate_monotone_separator(lo, hi, n, m):
    best = m
    for r in range(1, n + 1):
        best = min(best, hi[r])
        if lo[r] > best:
            return False
    return True

# CLAUSE: locate_failure_prefix
def locate_failure_prefix(n, m, q, queries):
    def check(prefix):
        rows = accumulate_prefix_constraints(queries, prefix)
        lo, hi = derive_frontier_bounds(rows, n, m)
        return validate_monotone_separator(lo, hi, n, m)

    if check(q):
        return q + 1

    left = 1
    right = q
    while left != right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid
    return left

# CLAUSE: emit_monotone_answers
def emit_monotone_answers(q, first_no):
    lines = []
    i = 1
    while i <= q:
        lines.append("YES" if i < first_no else "NO")
        i += 1
    sys.stdout.write("\n".join(lines))

def main():
    stream = sys.stdin.buffer
    first = stream.readline().split()
    if not first:
        return
    n, m, q = map(int, first)
    queries = []
    for _ in range(q):
        x, y = map(int, stream.readline().split())
        queries.append(classify_forbidden_side(normalize_white_coordinates(x, y)))
    emit_monotone_answers(q, locate_failure_prefix(n, m, q, queries))

main()
