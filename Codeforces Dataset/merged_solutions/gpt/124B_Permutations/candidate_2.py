# CLAUSE: parse_digit_matrix
import sys
import itertools

def parse_digit_matrix():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    k = int(tokens[1])
    matrix = [list(token.decode()) for token in tokens[2:2 + n]]
    return n, k, matrix

# CLAUSE: enumerate_column_permutations
def enumerate_column_permutations(k):
    for perm in itertools.permutations(range(k)):
        yield perm

# CLAUSE: construct_permuted_values
def construct_permuted_values(matrix, perm):
    return [handle_numeric_conversion(row, perm) for row in matrix]

# CLAUSE: track_extreme_values
def track_extreme_values(values):
    smallest = values[0]
    largest = values[0]
    for value in values[1:]:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return smallest, largest

# CLAUSE: minimize_range_score
def minimize_range_score(n, k, matrix):
    answer = 10 ** 30
    for perm in enumerate_column_permutations(k):
        values = construct_permuted_values(matrix, perm)
        smallest, largest = track_extreme_values(values)
        answer = min(answer, largest - smallest)
    return answer

# CLAUSE: handle_numeric_conversion
def handle_numeric_conversion(row, perm):
    value = 0
    for column in perm:
        value = value * 10 + ord(row[column]) - 48
    return value

if __name__ == "__main__":
    n, k, matrix = parse_digit_matrix()
    sys.stdout.write(str(minimize_range_score(n, k, matrix)))
