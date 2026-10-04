import sys

MOD = 998244353
LIMIT = 300005


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[i + 1]) for i in range(t)]


# --- clause: build_tables :: () -> tuple[list[int], list[int], list[int], list[int]] ---
def build_tables():
    involutions = [1] * LIMIT
    factorial = [1] * LIMIT
    for i in range(2, LIMIT):
        involutions[i] = (involutions[i - 1] + (i - 1) * involutions[i - 2]) % MOD
    for i in range(1, LIMIT):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse = [1] * LIMIT
    inverse[LIMIT - 1] = pow(factorial[LIMIT - 1], MOD - 2, MOD)
    i = LIMIT - 1
    while i > 0:
        inverse[i - 1] = inverse[i] * i % MOD
        i -= 1
    blocks = [0] * LIMIT
    for k in range(LIMIT):
        if 2 * k < LIMIT:
            blocks[k] = factorial[2 * k] * inverse[k] % MOD
        else:
            blocks[k] = 0
    return involutions, factorial, inverse, blocks


# --- clause: count_permutations :: (n: int, tables: tuple) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    tables = build_tables()
    answers = []
    for n in read_input():
        answers.append(str(count_permutations(n, tables)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
