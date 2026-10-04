# CLAUSE: parse_digit_matrix
import sys
from itertools import permutations

def parse_digit_matrix():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    rows = data[2:2 + n]
    return n, k, rows

# CLAUSE: enumerate_column_permutations
def enumerate_column_permutations(k):
    return permutations(range(k))

# CLAUSE: construct_permuted_values
def construct_permuted_values(rows, order):
    values = []
    for row in rows:
        values.append(handle_numeric_conversion(row[i] for i in order))
    return values

# CLAUSE: track_extreme_values
def track_extreme_values(values):
    return min(values), max(values)

# CLAUSE: minimize_range_score
def minimize_range_score(n, k, rows):
    best = None
    for order in enumerate_column_permutations(k):
        values = construct_permuted_values(rows, order)
        low, high = track_extreme_values(values)
        score = high - low
        if best is None or score < best:
            best = score
    return best

# CLAUSE: handle_numeric_conversion
def handle_numeric_conversion(chars):
    return int(''.join(chars))

if __name__ == "__main__":
    n, k, rows = parse_digit_matrix()
    print(minimize_range_score(n, k, rows))
