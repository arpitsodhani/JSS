import sys

# CLAUSE: normalize_white_coordinates
def normalize_white_coordinates(i, j):
    a = i // 2 + i % 2
    b = j // 2 + j % 2
    return a, b, i % 2 == 1

# CLAUSE: classify_forbidden_side
def classify_forbidden_side(mapped):
    r, c, first_family = mapped
    if first_family:
        return c, r - 1, None
    return c, None, r

# CLAUSE: accumulate_prefix_constraints
def accumulate_prefix_constraints(records, upto, m, n):
    upper = [n] * (m + 1)
    lower = [0] * (m + 1)
    used = set()
    for t in range(upto):
        col, high_value, low_value = records[t]
        if high_value is None:
            key = (col, 1, low_value)
            if key not in used:
                used.add(key)
                lower[col] = max(lower[col], low_value)
        else:
            key = (col, 0, high_value)
            if key not in used:
                used.add(key)
                upper[col] = min(upper[col], high_value)
    return lower, upper

# CLAUSE: derive_frontier_bounds
def derive_frontier_bounds(lower, upper):
    return list(zip(lower, upper))

# CLAUSE: validate_monotone_separator
def validate_monotone_separator(bounds, m, n):
    height = n
    for col in range(1, m + 1):
        lo, hi = bounds[col]
        if hi < height:
            height = hi
        if height < lo:
            return False
    return True

# CLAUSE: locate_failure_prefix
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

# CLAUSE: emit_monotone_answers
def emit_monotone_answers(q, bad):
    answer = ["NO"] * q
    for i in range(min(q, bad - 1)):
        answer[i] = "YES"
    print("\n".join(answer))

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n, m, q = values[0], values[1], values[2]
    records = []
    for z in range(q):
        x = values[3 + 2 * z]
        y = values[4 + 2 * z]
        records.append(classify_forbidden_side(normalize_white_coordinates(x, y)))
    bad = locate_failure_prefix(n, m, q, records)
    emit_monotone_answers(q, bad)

main()
