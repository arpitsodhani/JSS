import sys
MOD = 998244353
LIMIT = 300005

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]

# Clause build_tables [Confidence: 1.00]
def build_tables():
    involutions = [1] * LIMIT
    for i in range(2, LIMIT):
        involutions[i] = (involutions[i - 1] + (i - 1) * involutions[i - 2]) % MOD
    factorial = [1] * LIMIT
    for i in range(1, LIMIT):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse = [1] * LIMIT
    inverse[LIMIT - 1] = pow(factorial[LIMIT - 1], MOD - 2, MOD)
    for i in range(LIMIT - 1, 0, -1):
        inverse[i - 1] = inverse[i] * i % MOD
    weights = [1] * LIMIT
    for k in range(1, LIMIT):
        weights[k] = weights[k - 1] * (4 * k - 2) % MOD
    return involutions, factorial, inverse, weights

# Clause count_permutations [Confidence: 1.00]
def count_permutations(n, tables):
    involutions, factorial, inverse, blocks = tables
    total = 0
    k = 0
    while 4 * k <= n:
        free = n - 2 * k
        choose = factorial[free] * inverse[2 * k] % MOD * inverse[free - 2 * k] % MOD
        total = (total + choose * blocks[k] % MOD * involutions[n - 4 * k]) % MOD
        k += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    tables = build_tables()
    answers = []
    for n in read_input():
        answers.append(str(count_permutations(n, tables)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()

