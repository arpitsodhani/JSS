import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = [int(data[i + 1]) for i in range(n)]
    return n, spots


# --- clause: total_spread :: (n: int, spots: list[int]) -> int ---
def total_spread(n, spots):
    spots.sort()
    total = 0
    for i in range(n):
        as_max = pow(2, i, MOD)
        as_min = pow(2, n - 1 - i, MOD)
        total = (total + spots[i] * (as_max - as_min)) % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    answer = total_spread(n, spots)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
