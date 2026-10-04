import sys

# CLAUSE: classify_grid_dimensionality
def classify_grid_dimensionality(n, m):
    free_axes = (n > 1) + (m > 1)
    return free_axes

# CLAUSE: handle_singleton_cell
def handle_singleton_cell(free_axes):
    return 0 if free_axes == 0 else -1

# CLAUSE: prove_line_grid_identifiability
def prove_line_grid_identifiability(free_axes):
    return 1 if free_axes == 1 else -1

# CLAUSE: prove_two_dimensional_lower_bound
def prove_two_dimensional_lower_bound(free_axes):
    if free_axes == 2:
        return 1
    return 0

# CLAUSE: construct_corner_query_pair
def construct_corner_query_pair(free_axes):
    return 2 if free_axes == 2 else -1

# CLAUSE: derive_minimum_query_count
def derive_minimum_query_count(n, m):
    free_axes = classify_grid_dimensionality(n, m)
    singleton = handle_singleton_cell(free_axes)
    if singleton != -1:
        return singleton
    line = prove_line_grid_identifiability(free_axes)
    if line != -1:
        return line
    prove_two_dimensional_lower_bound(free_axes)
    return construct_corner_query_pair(free_axes)

tokens = sys.stdin.buffer.read().split()
answers = []
for i in range(1, len(tokens), 2):
    answers.append(str(derive_minimum_query_count(int(tokens[i]), int(tokens[i + 1]))))
print("\n".join(answers))
