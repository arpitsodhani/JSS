# CLAUSE: parse_digit_matrix
import sys
from itertools import permutations

def parse_digit_matrix():
    parts = sys.stdin.read().strip().split()
    n, k = map(int, parts[:2])
    digits = tuple(parts[2:2 + n])
    return n, k, digits

# CLAUSE: enumerate_column_permutations
def enumerate_column_permutations(k):
    return list(permutations(range(k)))

# CLAUSE: construct_permuted_values
def construct_permuted_values(digits, order):
    built = []
    for number in digits:
        text = ''.join(number[position] for position in order)
        built.append(handle_numeric_conversion(text))
    return built

# CLAUSE: track_extreme_values
def track_extreme_values(values):
    return min(values), max(values)

# CLAUSE: minimize_range_score
def minimize_range_score(n, k, digits):
    result = float("inf")
    orders = enumerate_column_permutations(k)
    for order in orders:
        values = construct_permuted_values(digits, order)
        lo, hi = track_extreme_values(values)
        if hi - lo < result:
            result = hi - lo
    return result

# CLAUSE: handle_numeric_conversion
def handle_numeric_conversion(text):
    return int(text)

if __name__ == "__main__":
    n, k, digits = parse_digit_matrix()
    print(minimize_range_score(n, k, digits))
