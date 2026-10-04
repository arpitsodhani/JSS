import sys

# CLAUSE: classify_grid_dimensionality
def classify_grid_dimensionality(n, m):
    if min(n, m) > 1:
        return "area"
    if max(n, m) == 1:
        return "point"
    return "line"

# CLAUSE: handle_singleton_cell
def handle_singleton_cell(shape):
    table = {"point": 0}
    return table.get(shape)

# CLAUSE: prove_line_grid_identifiability
def prove_line_grid_identifiability(shape):
    table = {"line": 1}
    return table.get(shape)

# CLAUSE: prove_two_dimensional_lower_bound
def prove_two_dimensional_lower_bound(shape):
    return shape == "area"

# CLAUSE: construct_corner_query_pair
def construct_corner_query_pair(shape):
    table = {"area": 2}
    return table.get(shape)

# CLAUSE: derive_minimum_query_count
def derive_minimum_query_count(n, m):
    shape = classify_grid_dimensionality(n, m)
    for rule in (handle_singleton_cell, prove_line_grid_identifiability, construct_corner_query_pair):
        if rule is construct_corner_query_pair and not prove_two_dimensional_lower_bound(shape):
            continue
        value = rule(shape)
        if value is not None:
            return value

def main():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        out.append(str(derive_minimum_query_count(n, m)))
    sys.stdout.write("\n".join(out))

main()
