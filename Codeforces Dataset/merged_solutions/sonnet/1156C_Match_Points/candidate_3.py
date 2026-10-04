import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    z = fields[1]
    return z, sorted(fields[2:2 + n])


# --- clause: fits :: (k: int, z: int, spots: list[int]) -> bool ---
def fits(k, z, spots):
    n = len(spots)
    for i in range(k):
        if spots[n - k + i] - spots[i] < z:
            return False
    return True


# --- clause: most_pairs :: (z: int, spots: list[int]) -> int ---
def most_pairs(z, spots):
    lower = 0
    large = len(spots) // 2
    while lower < large:
        mid = (lower + large + 1) // 2
        if fits(mid, z, spots):
            lower = mid
        else:
            large = mid - 1
    return lower


# --- clause: main :: () -> None ---
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()
