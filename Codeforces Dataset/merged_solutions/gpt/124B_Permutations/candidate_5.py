# CLAUSE: parse_digit_matrix
import sys
from itertools import permutations

def parse_digit_matrix():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    k = int(raw[1])
    rows = [raw[i] for i in range(2, 2 + n)]
    return n, k, rows

# CLAUSE: enumerate_column_permutations
def enumerate_column_permutations(k):
    perms = permutations(tuple(range(k)))
    return perms

# CLAUSE: construct_permuted_values
def construct_permuted_values(rows, order):
    values = []
    for row in rows:
        chosen = bytearray()
        for column in order:
            chosen.append(row[column])
        values.append(handle_numeric_conversion(chosen))
    return values

# CLAUSE: track_extreme_values
def track_extreme_values(values):
    iterator = iter(values)
    first = next(iterator)
    low = first
    high = first
    for value in iterator:
        low = value if value < low else low
        high = value if value > high else high
    return low, high

# CLAUSE: minimize_range_score
def minimize_range_score(n, k, rows):
    best_range = 10 ** 18
    for order in enumerate_column_permutations(k):
        transformed = construct_permuted_values(rows, order)
        low, high = track_extreme_values(transformed)
        diff = high - low
        if diff < best_range:
            best_range = diff
    return best_range

# CLAUSE: handle_numeric_conversion
def handle_numeric_conversion(buffer):
    return int(buffer.decode())

if __name__ == "__main__":
    n, k, rows = parse_digit_matrix()
    print(minimize_range_score(n, k, rows))
