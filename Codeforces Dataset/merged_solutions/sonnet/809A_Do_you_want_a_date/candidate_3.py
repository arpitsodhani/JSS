import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = []
    for token in data[1:n + 1]:
        spots.append(int(token))
    return n, spots


# --- clause: total_spread :: (n: int, spots: list[int]) -> int ---
def total_spread(n, spots):
    spots.sort()
    highest = 0
    lowest = 0
    weight = 1
    for i in range(n):
        highest = (highest + spots[i] * weight) % MOD
        lowest = (lowest + spots[n - 1 - i] * weight) % MOD
        weight = weight * 2 % MOD
    return (highest - lowest) % MOD


# --- clause: main :: () -> None ---
def main():
    n, spots = read_input()
    print(total_spread(n, spots))


if __name__ == "__main__":
    main()
