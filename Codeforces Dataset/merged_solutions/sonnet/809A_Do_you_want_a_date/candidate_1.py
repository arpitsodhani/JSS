import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = [int(token) for token in data[1:n + 1]]
    return n, spots


# --- clause: total_spread :: (n: int, spots: list[int]) -> int ---
def total_spread(n, spots):
    spots.sort()
    total = 0
    high = 1
    low = pow(2, n - 1, MOD)
    inverse = pow(2, MOD - 2, MOD)
    for value in spots:
        total = (total + value * (high - low)) % MOD
        high = high * 2 % MOD
        low = low * inverse % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    sys.stdout.write(str(total_spread(n, spots)) + "\n")


if __name__ == "__main__":
    main()
