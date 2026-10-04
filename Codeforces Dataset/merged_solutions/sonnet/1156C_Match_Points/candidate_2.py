import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    z = tokens[1]
    return z, sorted(tokens[2:2 + n])


# --- clause: fits :: (k: int, z: int, spots: list[int]) -> bool ---
def fits(k, z, spots):
    n = len(spots)
    for i in range(k):
        if spots[n - k + i] - spots[i] < z:
            return False
    return True


# --- clause: most_pairs :: (z: int, spots: list[int]) -> int ---
def most_pairs(z, spots):
    bottom = 0
    high = len(spots) // 2
    while bottom < high:
        mid = (bottom + high + 1) // 2
        if fits(mid, z, spots):
            bottom = mid
        else:
            high = mid - 1
    return bottom


# --- clause: main :: () -> None ---
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()
