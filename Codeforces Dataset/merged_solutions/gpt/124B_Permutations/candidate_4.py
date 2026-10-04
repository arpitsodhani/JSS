# CLAUSE: parse_digit_matrix
import sys
from itertools import permutations

def parse_digit_matrix():
    data = sys.stdin.readline().split()
    while len(data) < 2:
        data += sys.stdin.readline().split()
    n = int(data[0])
    k = int(data[1])
    rows = data[2:]
    while len(rows) < n:
        rows.extend(sys.stdin.readline().split())
    return n, k, rows[:n]

# CLAUSE: enumerate_column_permutations
def enumerate_column_permutations(k):
    indices = range(k)
    for order in permutations(indices):
        yield order

# CLAUSE: construct_permuted_values
def construct_permuted_values(rows, order):
    values = []
    for row in rows:
        values.append(handle_numeric_conversion([row[index] for index in order]))
    return values

# CLAUSE: track_extreme_values
def track_extreme_values(values):
    low = min(values)
    high = max(values)
    return low, high

# CLAUSE: minimize_range_score
def minimize_range_score(n, k, rows):
    minimum_range = None
    for order in enumerate_column_permutations(k):
        current_values = construct_permuted_values(rows, order)
        low, high = track_extreme_values(current_values)
        current_range = high - low
        if minimum_range is None:
            minimum_range = current_range
        elif current_range < minimum_range:
            minimum_range = current_range
    return minimum_range

# CLAUSE: handle_numeric_conversion
def handle_numeric_conversion(chars):
    number = 0
    for ch in chars:
        number = number * 10 + int(ch)
    return number

if __name__ == "__main__":
    n, k, rows = parse_digit_matrix()
    print(minimize_range_score(n, k, rows))
