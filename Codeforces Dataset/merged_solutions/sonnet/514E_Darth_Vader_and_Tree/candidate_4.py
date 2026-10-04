# CLAUSE: setup_environment
import sys

MOD = 10 ** 9 + 7

def mul_sparse_rows(a, b):
    m = len(a)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        target = result[i]
        for k in range(m):
            coeff = a[i][k]
            if coeff == 0:
                continue
            source = b[k]
            for j, item in enumerate(source):
                if item:
                    target[j] = (target[j] + coeff * item) % MOD
    return result

def use_power(matrix, exponent, vector):
    while exponent:
        if exponent & 1:
            next_vector = []
            for row in matrix:
                acc = 0
                for value, old in zip(row, vector):
                    acc += value * old
                next_vector.append(acc % MOD)
            vector = next_vector
        matrix = mul_sparse_rows(matrix, matrix)
        exponent >>= 1
    return vector

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    x = int(raw[1])
    distances = [int(raw[i]) for i in range(2, 2 + n)]

    max_distance = max(distances)
    counts = [0] * (max_distance + 1)
    for distance in distances:
        counts[distance] += 1

    side = max_distance + 1
    transition = [[0] * side for _ in range(side)]

    for index, amount in enumerate(counts[1:], 0):
        transition[0][index] = amount % MOD

    for index in range(max_distance - 1):
        transition[index + 1][index] = 1

    transition[max_distance][:max_distance] = transition[0][:max_distance]
    transition[max_distance][max_distance] = 1

    initial = [0] * side
    initial[0] = 1
    initial[max_distance] = 1

    answer = use_power(transition, x, initial)[max_distance] % MOD
    sys.stdout.write(str(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
