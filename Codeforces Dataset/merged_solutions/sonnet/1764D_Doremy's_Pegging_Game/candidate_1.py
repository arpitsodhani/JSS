import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: factorial_tables :: (n: int, p: int) -> tuple[list[int], list[int]] ---
def factorial_tables(n, p):
    fact = [1] * (n + 2)
    for i in range(1, n + 2):
        fact[i] = fact[i - 1] * i % p
    inverse = [1] * (n + 2)
    inverse[n + 1] = pow(fact[n + 1], p - 2, p)
    for i in range(n + 1, 0, -1):
        inverse[i - 1] = inverse[i] * i % p
    return fact, inverse


# --- clause: count_arrays :: (n: int, p: int) -> int ---
def count_arrays(n, p):
    fact, inverse = factorial_tables(n + 1, p)
    half = n // 2
    total = 0
    for run in range(half, n + 1):
        low = run - half
        if low < 0:
            low = 0
        high = half - 1 if half - 1 < run - 1 else run - 1
        pairs = high - low + 1
        if pairs <= 0:
            continue
        free = n - run - 2
        if free < 0:
            free = 0
        inner = 0
        for extra in range(free + 1):
            ways = fact[free] * inverse[extra] % p * inverse[free - extra] % p
            inner = (inner + ways * fact[run - 1 + extra]) % p
        total = (total + pairs * inner) % p
    return total * n % p


# --- clause: main :: () -> None ---
def main():
    n, p = read_input()
    sys.stdout.write(str(count_arrays(n, p)) + "\n")


if __name__ == "__main__":
    main()
