import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, list(map(int, data[1:n + 1]))


# --- clause: total_spread :: (n: int, spots: list[int]) -> int ---
def total_spread(n, spots):
    spots = sorted(spots)
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = powers[i - 1] * 2 % MOD
    total = 0
    for i in range(n):
        total += spots[i] * (powers[i] - powers[n - 1 - i])
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    sys.stdout.write("%d\n" % total_spread(n, spots))


if __name__ == "__main__":
    main()
