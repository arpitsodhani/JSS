import sys

# CLAUSE: classify_grid_dimensionality
def classify_grid_dimensionality(n, m):
    one_cell = n * m == 1
    line_grid = not one_cell and (n == 1 or m == 1)
    plane_grid = n > 1 and m > 1
    return one_cell, line_grid, plane_grid

# CLAUSE: handle_singleton_cell
def handle_singleton_cell(flags):
    one_cell, _, _ = flags
    if one_cell:
        return 0

# CLAUSE: prove_line_grid_identifiability
def prove_line_grid_identifiability(flags):
    _, line_grid, _ = flags
    if line_grid:
        return 1

# CLAUSE: prove_two_dimensional_lower_bound
def prove_two_dimensional_lower_bound(flags):
    _, _, plane_grid = flags
    return plane_grid

# CLAUSE: construct_corner_query_pair
def construct_corner_query_pair(flags):
    _, _, plane_grid = flags
    if plane_grid:
        return 2

# CLAUSE: derive_minimum_query_count
def derive_minimum_query_count(n, m):
    flags = classify_grid_dimensionality(n, m)
    candidates = (
        handle_singleton_cell(flags),
        prove_line_grid_identifiability(flags),
        construct_corner_query_pair(flags) if prove_two_dimensional_lower_bound(flags) else None,
    )
    for value in candidates:
        if value is not None:
            return value

def main():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    t = values[0]
    result = [None] * t
    at = 1
    for case in range(t):
        result[case] = str(derive_minimum_query_count(values[at], values[at + 1]))
        at += 2
    sys.stdout.write("\n".join(result))

main()
