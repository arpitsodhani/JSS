# CLAUSE: setup_environment
import sys

MOD = 1000000007

def multiply_square(x, y):
    length = len(x)
    product = [[0] * length for _ in range(length)]
    columns = [[y[i][j] for i in range(length)] for j in range(length)]
    for i in range(length):
        row = x[i]
        for j in range(length):
            s = 0
            col = columns[j]
            for k in range(length):
                s += row[k] * col[k]
            product[i][j] = s % MOD
    return product

def multiply_by_vector(x, y):
    ans = []
    for row in x:
        s = 0
        for a, b in zip(row, y):
            s += a * b
        ans.append(s % MOD)
    return ans

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, x = data[:2]
    arr = data[2:2 + n]
    mx = max(arr)

    by_distance = {}
    for item in arr:
        by_distance[item] = by_distance.get(item, 0) + 1

    size = mx + 1
    base = [[0] * size for _ in range(size)]

    for distance in range(1, mx + 1):
        base[0][distance - 1] = by_distance.get(distance, 0) % MOD

    row = 1
    while row < mx:
        base[row][row - 1] = 1
        row += 1

    col = 0
    while col < mx:
        base[mx][col] = base[0][col]
        col += 1
    base[mx][mx] = 1

    current = [0] * size
    current[0] = 1
    current[mx] = 1

    bit = x
    while bit:
        if bit & 1:
            current = multiply_by_vector(base, current)
        bit >>= 1
        if bit:
            base = multiply_square(base, base)

    sys.stdout.write(str(current[mx] % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
