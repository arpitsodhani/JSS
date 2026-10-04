import sys

# CLAUSE: classify_grid_dimensionality
def classify_grid_dimensionality(n, m):
    return (n == 1, m == 1)

# CLAUSE: handle_singleton_cell
def handle_singleton_cell(single_row, single_col):
    if single_row and single_col:
        return True, 0
    return False, 0

# CLAUSE: prove_line_grid_identifiability
def prove_line_grid_identifiability(single_row, single_col):
    if single_row != single_col:
        return True, 1
    return False, 0

# CLAUSE: prove_two_dimensional_lower_bound
def prove_two_dimensional_lower_bound(single_row, single_col):
    return not single_row and not single_col

# CLAUSE: construct_corner_query_pair
def construct_corner_query_pair(two_dimensional):
    if two_dimensional:
        return 2
    return 0

# CLAUSE: derive_minimum_query_count
def derive_minimum_query_count(n, m):
    single_row, single_col = classify_grid_dimensionality(n, m)
    done, value = handle_singleton_cell(single_row, single_col)
    if done:
        return value
    done, value = prove_line_grid_identifiability(single_row, single_col)
    if done:
        return value
    two_dimensional = prove_two_dimensional_lower_bound(single_row, single_col)
    return construct_corner_query_pair(two_dimensional)

def main():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    lines = []
    index = 1
    while count:
        n = int(data[index])
        m = int(data[index + 1])
        lines.append(str(derive_minimum_query_count(n, m)))
        index += 2
        count -= 1
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
