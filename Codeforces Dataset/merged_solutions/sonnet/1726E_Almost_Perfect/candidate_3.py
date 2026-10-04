import sys

MOD = 998244353
LIMIT = 300005


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    pos = 1
    while len(sizes) < t:
        sizes.append(int(data[pos]))
        pos += 1
    return sizes


# --- clause: build_tables :: () -> tuple[list[int], list[int], list[int], list[int]] ---
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
    blocks = [1] * LIMIT
    for k in range(1, LIMIT):
        blocks[k] = blocks[k - 1] * (2 * (2 * k - 1)) % MOD
    return involutions, factorial, inverse, blocks


# --- clause: count_permutations :: (n: int, tables: tuple) -> int ---
def count_permutations(n, tables):
    involutions, factorial, inverse, blocks = tables
    total = 0
    for k in range(0, n // 4 + 1):
        free = n - 2 * k
        choose = factorial[free] * inverse[2 * k] % MOD * inverse[free - 2 * k] % MOD
        total += choose * blocks[k] % MOD * involutions[n - 4 * k] % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    tables = build_tables()
    out = []
    for n in read_input():
        out.append(str(count_permutations(n, tables)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
