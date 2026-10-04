import sys

# CLAUSE: classify_grid_dimensionality
def classify_grid_dimensionality(n, m):
    if n == 1 and m == 1:
        return 0
    if n == 1 or m == 1:
        return 1
    return 2

# CLAUSE: handle_singleton_cell
def handle_singleton_cell(kind):
    if kind == 0:
        return 0
    return None

# CLAUSE: prove_line_grid_identifiability
def prove_line_grid_identifiability(kind):
    if kind == 1:
        return 1
    return None

# CLAUSE: prove_two_dimensional_lower_bound
def prove_two_dimensional_lower_bound(kind):
    return kind == 2

# CLAUSE: construct_corner_query_pair
def construct_corner_query_pair(kind):
    if kind == 2:
        return 2
    return None

# CLAUSE: derive_minimum_query_count
def derive_minimum_query_count(n, m):
    kind = classify_grid_dimensionality(n, m)
    answer = handle_singleton_cell(kind)
    if answer is not None:
        return answer
    answer = prove_line_grid_identifiability(kind)
    if answer is not None:
        return answer
    prove_two_dimensional_lower_bound(kind)
    return construct_corner_query_pair(kind)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    p = 1
    for _ in range(t):
        n, m = data[p], data[p + 1]
        p += 2
        out.append(str(derive_minimum_query_count(n, m)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
