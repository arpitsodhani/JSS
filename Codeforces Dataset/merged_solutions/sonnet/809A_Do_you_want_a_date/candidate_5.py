import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = list(map(int, data[1:1 + n]))
    return n, spots


# --- clause: total_spread :: (n: int, spots: list[int]) -> int ---
def total_spread(n, spots):
    ordered = sorted(spots, reverse=True)
    total = 0
    weight = pow(2, n - 1, MOD)
    inverse = pow(2, MOD - 2, MOD)
    small = 1
    for value in ordered:
        total = (total + value * (weight - small)) % MOD
        weight = weight * inverse % MOD
        small = small * 2 % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    sys.stdout.write(str(total_spread(n, spots)) + "\n")


if __name__ == "__main__":
    main()
