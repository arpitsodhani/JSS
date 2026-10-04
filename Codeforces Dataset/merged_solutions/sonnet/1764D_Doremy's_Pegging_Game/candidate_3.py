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
    limit = n // 2
    answer = 0
    for run in range(limit, n + 1):
        left = run - limit if run > limit else 0
        right = run - 1 if run - 1 < limit - 1 else limit - 1
        ways = right - left + 1
        if ways < 1:
            continue
        spare = n - run - 2
        if spare < 0:
            spare = 0
        block = 0
        base = fact[spare]
        for extra in range(spare + 1):
            block += base * inverse[extra] % p * inverse[spare - extra] % p * fact[run - 1 + extra]
            block %= p
        answer = (answer + ways * block) % p
    return answer * n % p

# --- clause: main :: () -> None ---
def main():
    n, p = read_input()
    sys.stdout.write(str(count_arrays(n, p)) + "\n")


if __name__ == "__main__":
    main()
