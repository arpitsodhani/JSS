import sys

MOD = 998244353


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: primes_upto :: (n: int) -> list[bool] ---
def primes_upto(n):
    flags = [False, False] + [True] * (n - 1) if n >= 1 else [False] * (n + 1)
    for step in range(2, int(n ** 0.5) + 1):
        if flags[step]:
            flags[step * step::step] = [False] * len(flags[step * step::step])
    return flags


# --- clause: count_ambiguous :: (n: int, m: int) -> int ---
def count_ambiguous(n, m):
    flags = primes_upto(n)
    answer = 0
    all_arrays = 1
    clean = 1
    product = 1
    for length in range(1, n + 1):
        if length > 1 and flags[length] and product <= m:
            product *= length
        room = 0 if product > m else m // product
        clean = clean * room % MOD
        all_arrays = all_arrays * (m % MOD) % MOD
        answer += all_arrays - clean
    return answer % MOD


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write(str(count_ambiguous(n, m)) + "\n")


if __name__ == "__main__":
    main()
