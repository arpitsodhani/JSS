import sys

MOD = 998244353


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: primes_upto :: (n: int) -> list[bool] ---
def primes_upto(n):
    flags = [True] * (n + 1)
    if n >= 0:
        flags[0] = False
    if n >= 1:
        flags[1] = False
    step = 2
    while step * step <= n:
        if flags[step]:
            for multiple in range(step * step, n + 1, step):
                flags[multiple] = False
        step += 1
    return flags


# --- clause: count_ambiguous :: (n: int, m: int) -> int ---
def count_ambiguous(n, m):
    flags = primes_upto(n)
    total = 0
    power = 1
    strict = 1
    guard = 1
    for length in range(1, n + 1):
        if length > 1 and flags[length]:
            if guard <= m:
                guard *= length
        choices = m // guard if guard <= m else 0
        strict = strict * (choices % MOD) % MOD
        power = power * (m % MOD) % MOD
        total = (total + power - strict) % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write(str(count_ambiguous(n, m)) + "\n")


if __name__ == "__main__":
    main()
