import sys

# CLAUSE: normalize_white_coordinates
def normalize_white_coordinates(x, y):
    row = (x + 1) >> 1
    col = (y + 1) >> 1
    family = x & 1
    return row, col, family

# CLAUSE: classify_forbidden_side
def classify_forbidden_side(row, col, family):
    if family:
        return row, col, 0
    return row, col, 1

# CLAUSE: accumulate_prefix_constraints
def accumulate_prefix_constraints(blocks, upto, n, m):
    touched = set()
    rows = [[0, m] for _ in range(n + 1)]
    for block in blocks[:upto]:
        r, c, side = block
        if block in touched:
            continue
        touched.add(block)
        if side:
            rows[r][0] = max(rows[r][0], c)
        else:
            rows[r][1] = min(rows[r][1], c - 1)
    return rows

# CLAUSE: derive_frontier_bounds
def derive_frontier_bounds(rows, n):
    prefix_caps = [0] * (n + 1)
    prefix_caps[0] = rows[0][1]
    for r in range(1, n + 1):
        prefix_caps[r] = min(prefix_caps[r - 1], rows[r][1])
    return prefix_caps, rows

# CLAUSE: validate_monotone_separator
def validate_monotone_separator(prefix_caps, rows, n):
    for r in range(1, n + 1):
        if rows[r][0] > prefix_caps[r]:
            return False
    return True

# CLAUSE: locate_failure_prefix
def locate_failure_prefix(n, m, q, blocks):
    def valid(k):
        rows = accumulate_prefix_constraints(blocks, k, n, m)
        prefix_caps, rows = derive_frontier_bounds(rows, n)
        return validate_monotone_separator(prefix_caps, rows, n)

    if valid(q):
        return q + 1

    a, b = 1, q
    while a < b:
        mid = (a + b) >> 1
        if valid(mid):
            a = mid + 1
        else:
            b = mid
    return a

# CLAUSE: emit_monotone_answers
def emit_monotone_answers(q, first_bad):
    sys.stdout.write("\n".join(("YES", "NO")[i >= first_bad] for i in range(1, q + 1)))

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n, m, q = nums[:3]
    blocks = []
    index = 3
    for _ in range(q):
        x = nums[index]
        y = nums[index + 1]
        index += 2
        blocks.append(classify_forbidden_side(*normalize_white_coordinates(x, y)))
    first_bad = locate_failure_prefix(n, m, q, blocks)
    emit_monotone_answers(q, first_bad)

main()
