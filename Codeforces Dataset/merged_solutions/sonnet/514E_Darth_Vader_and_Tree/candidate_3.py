# CLAUSE: setup_environment
import sys

MOD = 1000000007

def combine(a, b):
    m = len(a)
    c = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            total = 0
            for k in range(m):
                total += a[i][k] * b[k][j]
            c[i][j] = total % MOD
    return c

def transform_vector(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) % MOD for i in range(len(vector))]

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.read().split()))
    if not values:
        return

    n = values[0]
    x = values[1]
    ds = values[2:2 + n]
    limit = 0
    for d in ds:
        if d > limit:
            limit = d

    freq = [0] * (limit + 1)
    for d in ds:
        freq[d] = (freq[d] + 1) % MOD

    width = limit + 1
    matrix = [[0] * width for _ in range(width)]

    first = matrix[0]
    for pos in range(limit):
        first[pos] = freq[pos + 1]

    for row in range(1, limit):
        matrix[row][row - 1] = 1

    last = matrix[limit]
    for pos, value in enumerate(first[:limit]):
        last[pos] = value
    last[limit] = 1

    vector = [0] * width
    vector[0] = 1
    vector[-1] = 1

    power = x
    while power > 0:
        if power % 2 == 1:
            vector = transform_vector(matrix, vector)
        matrix = combine(matrix, matrix)
        power //= 2

    print(vector[-1] % MOD)

# CLAUSE: finish_program
main()
